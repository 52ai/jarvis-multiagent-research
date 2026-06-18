#!/usr/bin/env python3
"""
033 Phase 2 · 实验结果聚合分析器 v0.1

功能：
- 读取 results/eval_*.json（LLM-as-judge 评估结果）
- 按 architecture × task 维度聚合
- 输出 Markdown 对比表 + 关键洞察

用法：
  python3 result_aggregator.py --input results/eval_*.json
  python3 result_aggregator.py --all  # 扫描 results/ 所有 eval
  python3 result_aggregator.py --all --output results/aggregate_report.md
"""
import sys
import os
import json
import argparse
import glob
from datetime import datetime, timezone, timedelta
from pathlib import Path
from collections import defaultdict
import statistics

WORKSPACE = Path("/workspace")
EXP_DIR = WORKSPACE / "033-MultiAgentResearch" / "02-Experiments"
RESULTS_DIR = EXP_DIR / "results"


def cst_now_str() -> str:
    return datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S CST")


def load_evaluations(input_paths: list) -> list:
    """加载所有评估结果"""
    evals = []
    for p in input_paths:
        try:
            with open(p, "r", encoding="utf-8") as f:
                evals.append(json.load(f))
        except Exception as e:
            print(f"[WARN] {p}: 加载失败 - {e}")
    return evals


def aggregate_by_architecture(evals: list) -> dict:
    """按架构聚合：求每架构的 4 维平均分 + 综合分"""
    arch_scores = defaultdict(lambda: {
        "fact_accuracy": [],
        "structure_completeness": [],
        "readability": [],
        "insight_depth": [],
        "composite_score": [],
        "n_runs": 0,
    })
    for e in evals:
        arch = e.get("arch_id", "unknown")
        scores = e["scores"]
        for dim in ["fact_accuracy", "structure_completeness", "readability", "insight_depth", "composite_score"]:
            arch_scores[arch][dim].append(scores.get(dim, 0))
        arch_scores[arch]["n_runs"] += 1

    # 求均值 + 标准差
    result = {}
    for arch, data in arch_scores.items():
        result[arch] = {
            "n_runs": data["n_runs"],
            "fact_accuracy": statistics.mean(data["fact_accuracy"]),
            "fact_accuracy_std": statistics.stdev(data["fact_accuracy"]) if len(data["fact_accuracy"]) > 1 else 0,
            "structure_completeness": statistics.mean(data["structure_completeness"]),
            "readability": statistics.mean(data["readability"]),
            "insight_depth": statistics.mean(data["insight_depth"]),
            "composite_score": statistics.mean(data["composite_score"]),
            "composite_score_std": statistics.stdev(data["composite_score"]) if len(data["composite_score"]) > 1 else 0,
        }
    return result


def aggregate_by_task(evals: list) -> dict:
    """按任务聚合：求每任务的平均分"""
    task_scores = defaultdict(lambda: {
        "composite_score": [],
        "n_runs": 0,
    })
    for e in evals:
        task = e.get("task_id", "unknown")
        task_scores[task]["composite_score"].append(e["scores"].get("composite_score", 0))
        task_scores[task]["n_runs"] += 1

    return {
        task: {
            "n_runs": data["n_runs"],
            "avg_composite": statistics.mean(data["composite_score"]),
        }
        for task, data in task_scores.items()
    }


def render_markdown_report(arch_data: dict, task_data: dict, n_total: int) -> str:
    """生成 Markdown 聚合报告"""
    lines = [
        "# 033 Phase 2 · 实验结果聚合报告 v0.1",
        "",
        f"**生成时间**: {cst_now_str()}",
        f"**总评估数**: {n_total}",
        "",
        "---",
        "",
        "## 📊 按架构聚合（横向对比）",
        "",
        "| 架构 | 样本数 | Fact | Struct | Read | Insight | 综合 (mean ± std) |",
        "|------|--------|------|--------|------|---------|-------------------|",
    ]

    # 按综合分降序
    sorted_archs = sorted(arch_data.items(), key=lambda x: x[1]["composite_score"], reverse=True)
    for arch, data in sorted_archs:
        lines.append(
            f"| `{arch}` | {data['n_runs']} | "
            f"{data['fact_accuracy']:.2f} | {data['structure_completeness']:.2f} | "
            f"{data['readability']:.2f} | {data['insight_depth']:.2f} | "
            f"**{data['composite_score']:.2f}** ± {data['composite_score_std']:.2f} |"
        )

    # 找赢家
    if sorted_archs:
        winner_arch, winner_data = sorted_archs[0]
        lines.extend([
            "",
            f"### 🏆 最佳架构（按综合分）",
            "",
            f"**`{winner_arch}`** · 综合分 {winner_data['composite_score']:.2f} "
            f"(± {winner_data['composite_score_std']:.2f}, n={winner_data['n_runs']})",
            "",
        ])

    lines.extend([
        "---",
        "",
        "## 📋 按任务聚合（看哪个任务最难）",
        "",
        "| 任务 | 样本数 | 平均综合分 |",
        "|------|--------|----------|",
    ])
    sorted_tasks = sorted(task_data.items(), key=lambda x: x[1]["avg_composite"])
    for task, data in sorted_tasks:
        lines.append(
            f"| {task} | {data['n_runs']} | {data['avg_composite']:.2f} |"
        )

    # 最难任务
    if sorted_tasks:
        hardest, hardest_data = sorted_tasks[0]
        lines.extend([
            "",
            f"### 🧗 最难任务：{hardest}",
            "",
            f"平均综合分仅 {hardest_data['avg_composite']:.2f} "
            f"（{hardest_data['n_runs']} 个 run 聚合）",
        ])

    lines.extend([
        "",
        "---",
        "",
        "## 🔍 关键洞察（基于现有数据）",
        "",
        f"- **总样本数**：{n_total} 个 run",
        f"- **架构数**：{len(arch_data)}",
        f"- **任务数**：{len(task_data)}",
        "",
        "### 假设验证（基于 design-v0.1.md 的 H1-H3）",
        "",
        "- **H1** (3-5 agent 最优) — 待样本充足后验证",
        "- **H2** (3+ agent 通信开销显著) — 待 Token 成本数据汇总后验证",
        "- **H3** (主从架构效率高) — 待 supervised vs equal 对比",
        "",
        "---",
        "",
        "*🤖 Jarvis AI · 聚合器 v0.1 · 待 W27 真实数据注入*",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="033 实验结果聚合分析器")
    parser.add_argument("--input", nargs="+", help="eval_*.json 文件列表")
    parser.add_argument("--all", action="store_true", help="扫描 results/ 下所有 eval_*.json")
    parser.add_argument("--output", help="输出 Markdown 报告路径")
    args = parser.parse_args()

    if args.input:
        input_paths = [Path(p) for p in args.input]
    elif args.all:
        input_paths = sorted(RESULTS_DIR.glob("eval_*.json"))
    else:
        # 默认扫描
        input_paths = sorted(RESULTS_DIR.glob("eval_*.json"))

    if not input_paths:
        print(f"[INFO] 没有找到评估结果（{RESULTS_DIR}/eval_*.json）")
        return 0

    print(f"[{cst_now_str()}] 033 结果聚合器 v0.1")
    print(f"  评估文件数: {len(input_paths)}")

    evals = load_evaluations(input_paths)
    if not evals:
        print("[WARN] 所有文件加载失败")
        return 1

    arch_data = aggregate_by_architecture(evals)
    task_data = aggregate_by_task(evals)
    md = render_markdown_report(arch_data, task_data, len(evals))

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = RESULTS_DIR / f"aggregate_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(md, encoding="utf-8")

    print(f"\n[RESULT] 架构数: {len(arch_data)} | 任务数: {len(task_data)}")
    if arch_data:
        winner = max(arch_data.items(), key=lambda x: x[1]["composite_score"])
        print(f"[WINNER] {winner[0]} · 综合 {winner[1]['composite_score']:.2f}")
    print(f"[OUTPUT] {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
