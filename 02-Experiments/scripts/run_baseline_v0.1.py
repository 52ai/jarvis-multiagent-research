#!/usr/bin/env python3
"""
033 Phase 2 · 实验启动器 v0.1

功能：
- 读取 task_set_v0.1.json 的 5 个任务 × 12 种架构 = 60 种实验配置
- 每次实验重复 3 次（控制随机性）
- 调用 OpenClaw 内置多 agent 模式 或 加载 OWL 框架
- 输出结构化结果到 results/ 目录

注意：当前 v0.1 是「启动器骨架」，实际的多 agent 调度逻辑在 W27 启动实验时迭代。

用法：
  python3 run_baseline_v0.1.py --task T1 --architecture single
  python3 run_baseline_v0.1.py --all  # 全量跑 180 次
  python3 run_baseline_v0.1.py --dry-run  # 只打印实验计划
"""
import sys
import os
import json
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path

WORKSPACE = Path("/workspace")
EXP_DIR = WORKSPACE / "033-MultiAgentResearch" / "02-Experiments"
RESULTS_DIR = EXP_DIR / "results"
TASK_SET = EXP_DIR / "benchmarks" / "task_set_v0.1.json"


def cst_now_str() -> str:
    return datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S CST")


def load_task_set() -> dict:
    with open(TASK_SET, "r", encoding="utf-8") as f:
        return json.load(f)


# 12 种实验配置（来自 design-v0.1.md）
ARCHITECTURES = [
    {"id": "single", "name": "Single Agent", "n_agents": 1, "model": "opus-4", "type": "baseline"},
    {"id": "equal-2", "name": "Equal 2x2", "n_agents": 2, "model": "sonnet-4", "type": "equal"},
    {"id": "equal-3", "name": "Equal 3x3", "n_agents": 3, "model": "sonnet-4", "type": "equal"},
    {"id": "equal-5", "name": "Equal 5x5", "n_agents": 5, "model": "sonnet-4", "type": "equal"},
    {"id": "equal-7", "name": "Equal 7x7", "n_agents": 7, "model": "sonnet-4", "type": "equal"},
    {"id": "equal-9", "name": "Equal 9x9", "n_agents": 9, "model": "sonnet-4", "type": "equal"},
    {"id": "supervised-2", "name": "Supervised 1+1", "n_agents": 2, "model": "opus-4+sonnet-4", "type": "supervised"},
    {"id": "supervised-3", "name": "Supervised 1+2", "n_agents": 3, "model": "opus-4+sonnet-4", "type": "supervised"},
    {"id": "supervised-5", "name": "Supervised 1+4", "n_agents": 5, "model": "opus-4+sonnet-4", "type": "supervised"},
    {"id": "supervised-7", "name": "Supervised 1+6", "n_agents": 7, "model": "opus-4+sonnet-4", "type": "supervised"},
    {"id": "pipeline-3", "name": "Pipeline 3-stage", "n_agents": 3, "model": "sonnet-4", "type": "pipeline"},
    {"id": "pipeline-5", "name": "Pipeline 5-stage", "n_agents": 5, "model": "sonnet-4", "type": "pipeline"},
]


def build_experiment_plan(task_set: dict, architectures: list) -> list:
    """
    构建完整实验计划：5 任务 × 12 架构 × 3 重复 = 180 次
    """
    plan = []
    for task in task_set["tasks"]:
        for arch in architectures:
            for rep in range(1, 4):  # 3 repetitions
                plan.append({
                    "experiment_id": f"E{task['id'][-1]}_{arch['id']}_r{rep}",
                    "task_id": task["id"],
                    "task_name": task["name"],
                    "task_query": task["query"],
                    "arch_id": arch["id"],
                    "arch_name": arch["name"],
                    "n_agents": arch["n_agents"],
                    "model": arch["model"],
                    "arch_type": arch["type"],
                    "repetition": rep,
                    "scheduled_at": None,  # 实际启动时填
                })
    return plan


def save_plan(plan: list, output_path: Path):
    """保存实验计划到 JSON"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({
            "generated_at": cst_now_str(),
            "total_runs": len(plan),
            "tasks": 5,
            "architectures": len(ARCHITECTURES),
            "repetitions": 3,
            "expected_total_tokens": "5.5M",
            "plan": plan,
        }, f, ensure_ascii=False, indent=2)
    print(f"[PLAN] {len(plan)} runs saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="033 Phase 2 实验启动器")
    parser.add_argument("--task", help="指定任务 ID (T1-T5)")
    parser.add_argument("--architecture", help="指定架构 ID (single/equal-3/supervised-5/...)")
    parser.add_argument("--all", action="store_true", help="全量跑 180 次")
    parser.add_argument("--dry-run", action="store_true", help="只生成实验计划，不实际执行")
    parser.add_argument("--repetition", type=int, default=3, help="重复次数（默认 3）")
    args = parser.parse_args()

    task_set = load_task_set()
    plan = build_experiment_plan(task_set, ARCHITECTURES)

    print(f"[{cst_now_str()}] 033 Phase 2 实验启动器 v0.1")
    print(f"  任务: {len(task_set['tasks'])} 个")
    print(f"  架构: {len(ARCHITECTURES)} 种")
    print(f"  重复: 3 次")
    print(f"  合计: {len(plan)} 次实验")
    print(f"  预计 Token: ~5.5M")
    print()

    # 过滤
    if args.task and args.architecture:
        plan = [p for p in plan
                if p["task_id"] == args.task and p["arch_id"] == args.architecture]
        print(f"[FILTER] task={args.task} arch={args.architecture} → {len(plan)} runs")
    elif args.task:
        plan = [p for p in plan if p["task_id"] == args.task]
        print(f"[FILTER] task={args.task} → {len(plan)} runs")
    elif args.architecture:
        plan = [p for p in plan if p["arch_id"] == args.architecture]
        print(f"[FILTER] arch={args.architecture} → {len(plan)} runs")

    # 保存计划
    plan_path = RESULTS_DIR / f"experiment_plan_{datetime.now().strftime('%Y%m%d')}.json"
    save_plan(plan, plan_path)

    if args.dry_run:
        print("\n[DRY-RUN] 详细计划（前 5 条）：")
        for p in plan[:5]:
            print(f"  {p['experiment_id']}: {p['task_name'][:30]} | {p['arch_name']} | rep={p['repetition']}")
        print(f"  ... ({len(plan) - 5} more)")
        return 0

    # 实际执行（v0.1 阶段还是 stub，W27 启动实验时实装）
    print("\n[STUB] v0.1 启动器骨架，W27 启动实验时实装以下模块：")
    print("  - OpenClaw 多 agent 调度（subagent spawn）")
    print("  - OWL 框架加载（scripts/owl/）")
    print("  - LLM-as-judge 评估（Opus 4）")
    print("  - 结果收集器（results/）")
    print("  - 异常处理 + 重试机制（3 次）")
    print()
    print(f"📋 实验计划已保存: {plan_path}")
    print(f"🚀 W27 启动后用 --all 或 --task/--architecture 参数执行")
    return 0


if __name__ == "__main__":
    sys.exit(main())
