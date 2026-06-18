#!/usr/bin/env python3
"""
033 Phase 2 · LLM-as-Judge 评估器 v0.1

功能：
- 对 5 个 T1-T5 任务的输出进行 4 维评分
- 评分维度：fact_accuracy / structure_completeness / readability / insight_depth
- 使用 Opus 4 作为 judge（最强推理）
- 输出评分 JSON + Markdown 评估报告

用法：
  python3 llm_judge.py --input results/run_E1_single_r1.json
  python3 llm_judge.py --batch results/*.json  # 批量评估
  python3 llm_judge.py --dry-run --input ...   # 只看 prompt 不调用

依赖：
- results/<run_id>.json 必须包含 task_id, task_query, output, duration_ms, tokens_used
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


# ========== 评估 Prompt 模板 ==========

JUDGE_SYSTEM_PROMPT = """你是 033 课题的 LLM-as-Judge 评估员。任务：对一个多智能体系统的输出做 4 维评分。

【评分原则】
1. 客观中立 - 不受输出长度、格式偏好影响
2. 严格对照评分标准（下方提供）
3. 每维度给 0-10 分，最后给加权综合分
4. 给出 1-2 句具体改进建议

【权重】
- fact_accuracy: 40%
- structure_completeness: 20%
- readability: 20%
- insight_depth: 20%
"""

JUDGE_USER_PROMPT_TEMPLATE = """【任务定义】
任务 ID: {task_id}
任务名称: {task_name}
难度: {difficulty}

【任务原始 Query】
{query}

【待评估输出】
{output}

【关键事实 Checklist】（必须覆盖）
{checklist}

【4 维评分标准】
1. fact_accuracy (0-10) - 关键事实覆盖度 + 数据准确性
2. structure_completeness (0-10) - 章节完整度 + 图表/列表/数据呈现
3. readability (0-10) - 语言流畅 + 学术规范性
4. insight_depth (0-10) - "个人判断"质量 + 论证深度

【输出格式】（必须是合法 JSON）
{{
  "fact_accuracy": <0-10>,
  "fact_accuracy_reasoning": "...",
  "structure_completeness": <0-10>,
  "structure_completeness_reasoning": "...",
  "readability": <0-10>,
  "readability_reasoning": "...",
  "insight_depth": <0-10>,
  "insight_depth_reasoning": "...",
  "composite_score": <加权后 0-10>,
  "checklist_coverage": {{"checklist_id_1": "covered/missing/partial", ...}},
  "improvement_suggestions": ["建议 1", "建议 2"]
}}
"""


def load_task_set() -> dict:
    with open(TASK_SET, "r", encoding="utf-8") as f:
        return json.load(f)


def get_task_by_id(task_set: dict, task_id: str) -> dict:
    for t in task_set["tasks"]:
        if t["id"] == task_id:
            return t
    raise ValueError(f"Task {task_id} not found")


def build_judge_prompt(task: dict, output_text: str) -> str:
    """构建 LLM-as-judge 的 user prompt"""
    checklist_str = "\n".join(
        f"  - [{i+1}] {fact}"
        for i, fact in enumerate(task["key_facts_checklist"])
    )

    return JUDGE_USER_PROMPT_TEMPLATE.format(
        task_id=task["id"],
        task_name=task["name"],
        difficulty="⭐" * int(task.get("difficulty", "⭐⭐").count("⭐")),
        query=task["query"],
        output=output_text[:8000],  # 截断到 8K，避免超长
        checklist=checklist_str,
    )


def call_llm_judge(prompt: str, model: str = "opus-4") -> dict:
    """
    调用 LLM-as-judge 评估。
    v0.1 阶段：mock 实现（返回预置分数）
    W27 实际运行时：接入真实 LLM API
    """
    # 实际接入时替换为：
    # response = openai_client.chat.completions.create(
    #     model=model,
    #     messages=[
    #         {"role": "system", "content": JUDGE_SYSTEM_PROMPT},
    #         {"role": "user", "content": prompt},
    #     ],
    #     response_format={"type": "json_object"},
    # )
    # return json.loads(response.choices[0].message.content)

    # v0.1 mock：返回合理占位分数
    return {
        "fact_accuracy": 7.5,
        "fact_accuracy_reasoning": "[MOCK] 待接入真实 LLM",
        "structure_completeness": 7.0,
        "structure_completeness_reasoning": "[MOCK]",
        "readability": 8.0,
        "readability_reasoning": "[MOCK]",
        "insight_depth": 6.5,
        "insight_depth_reasoning": "[MOCK]",
        "composite_score": 7.3,
        "checklist_coverage": {
            f"checklist_{i+1}": "covered"
            for i in range(len(get_task_by_id(load_task_set(), "T1")["key_facts_checklist"]))
        },
        "improvement_suggestions": ["[MOCK] 待接入真实 LLM"]
    }


def evaluate_single(input_path: Path, task_set: dict, dry_run: bool = False) -> dict:
    """
    评估单个 run 结果。
    """
    with open(input_path, "r", encoding="utf-8") as f:
        run = json.load(f)

    task = get_task_by_id(task_set, run["task_id"])
    output_text = run.get("output", "")

    if not output_text:
        print(f"[WARN] {input_path.name}: output 为空，跳过评估")
        return None

    # 构建 prompt
    prompt = build_judge_prompt(task, output_text)

    if dry_run:
        print(f"[DRY-RUN] {input_path.name}")
        print(f"  Task: {task['id']} - {task['name']}")
        print(f"  Output length: {len(output_text)} 字符")
        print(f"  Prompt preview (前 500 字符):")
        print(f"  {prompt[:500]}...")
        return None

    # 调用 LLM judge
    print(f"[EVAL] {input_path.name} ({task['id']} - {task['name']})")
    scores = call_llm_judge(prompt)

    # 合并结果
    result = {
        "run_id": run.get("experiment_id", input_path.stem),
        "task_id": run["task_id"],
        "task_name": task["name"],
        "arch_id": run.get("arch_id"),
        "arch_name": run.get("arch_name"),
        "n_agents": run.get("n_agents"),
        "repetition": run.get("repetition"),
        "duration_ms": run.get("duration_ms"),
        "tokens_used": run.get("tokens_used"),
        "scores": scores,
        "evaluated_at": cst_now_str(),
        "judge_model": "opus-4 (MOCK)",
    }
    return result


def save_evaluation(result: dict, output_path: Path):
    """保存评估结果"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"  → {output_path}")


def render_markdown_report(evaluations: list, output_path: Path):
    """生成 Markdown 评估汇总报告"""
    lines = [
        "# 033 Phase 2 · LLM-as-Judge 评估报告 v0.1",
        "",
        f"**生成时间**: {cst_now_str()}",
        f"**评估样本数**: {len(evaluations)}",
        f"**Judge 模型**: opus-4 (MOCK v0.1)",
        "",
        "---",
        "",
        "## 📊 评估结果汇总",
        "",
        "| Run ID | Task | 架构 | Agent 数 | Fact | Struct | Read | Insight | 综合 |",
        "|--------|------|------|---------|------|--------|------|---------|------|",
    ]
    for e in evaluations:
        s = e["scores"]
        lines.append(
            f"| {e['run_id']} | {e['task_id']} | {e['arch_id']} | {e['n_agents']} | "
            f"{s['fact_accuracy']:.1f} | {s['structure_completeness']:.1f} | "
            f"{s['readability']:.1f} | {s['insight_depth']:.1f} | "
            f"**{s['composite_score']:.2f}** |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 🏆 排名（按综合分）",
        "",
    ])
    sorted_evals = sorted(evaluations, key=lambda e: e["scores"]["composite_score"], reverse=True)
    for i, e in enumerate(sorted_evals[:10], 1):
        s = e["scores"]
        lines.append(
            f"{i}. **{e['run_id']}** ({e['task_id']} · {e['arch_name']}) — "
            f"综合 {s['composite_score']:.2f} | Fact {s['fact_accuracy']:.1f}"
        )

    lines.extend([
        "",
        "---",
        "",
        "*🤖 Jarvis AI · 评估器 v0.1 · 等待 W27 接入真实 LLM*",
    ])

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n[REPORT] {output_path}")


def main():
    parser = argparse.ArgumentParser(description="033 LLM-as-Judge 评估器")
    parser.add_argument("--input", help="单个 run JSON 文件")
    parser.add_argument("--batch", nargs="+", help="批量 run JSON 文件")
    parser.add_argument("--dry-run", action="store_true", help="只看 prompt 不评估")
    parser.add_argument("--report", action="store_true", help="生成 Markdown 汇总报告")
    args = parser.parse_args()

    task_set = load_task_set()

    if args.input:
        input_paths = [Path(args.input)]
    elif args.batch:
        input_paths = [Path(p) for p in args.batch]
    else:
        # 默认评估 results/ 下所有 JSON
        input_paths = sorted(RESULTS_DIR.glob("run_*.json"))
        if not input_paths:
            print("[INFO] results/ 下没有 run_*.json，跳过")
            return 0

    print(f"[{cst_now_str()}] LLM-as-Judge 评估器 v0.1")
    print(f"  待评估文件数: {len(input_paths)}")
    print(f"  Judge 模型: opus-4 (MOCK)")
    print()

    evaluations = []
    for ip in input_paths:
        if not ip.exists():
            print(f"[WARN] {ip} 不存在")
            continue
        result = evaluate_single(ip, task_set, dry_run=args.dry_run)
        if result:
            evaluations.append(result)
            # 保存单条评估
            eval_path = RESULTS_DIR / f"eval_{ip.stem}.json"
            save_evaluation(result, eval_path)

    if args.report and evaluations:
        report_path = RESULTS_DIR / f"judge_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        render_markdown_report(evaluations, report_path)

    print(f"\n[DONE] 评估完成：{len(evaluations)} 条")
    return 0


if __name__ == "__main__":
    sys.exit(main())
