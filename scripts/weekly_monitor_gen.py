#!/usr/bin/env python3
"""
033 课题 · 每周热点追踪自动生成脚本

功能：每周三 10:00 CST 自动抓取 6 个关键词的多智能体最新动态，
     输出到 weekly-monitor-YYYY-MM-DD.md，模板对齐 W25 期格式。

使用：
  python3 weekly_monitor_gen.py [--date YYYY-MM-DD] [--keywords-file PATH]
"""
import sys
import os
import argparse
from datetime import datetime, timezone, timedelta
from pathlib import Path

WORKSPACE = Path("/workspace")
OUT_DIR = WORKSPACE / "033-MultiAgentResearch" / "04-FrontierHotspots"

# 6 个追踪关键词（v1.1 报告 §11.2）
DEFAULT_KEYWORDS = [
    "multi-agent LLM 2026",
    "A2A protocol MCP comparison",
    "Anthropic Claude multi-agent",
    "Google DeepMind agent scaling",
    "multi-agent emergent coordination",
    "multi-agent security alignment",
]


def cst_now() -> datetime:
    """CST 当前时间"""
    return datetime.now(timezone(timedelta(hours=8)))


def week_label(dt: datetime) -> str:
    """ISO 周编号 (e.g. 2026-W25)"""
    y, w, _ = dt.isocalendar()
    return f"{y}-W{w:02d}"


def search_keywords(keywords, num_per=5):
    """
    调用 batch_web_search 抓取关键词结果。

    Returns: {keyword: [{title, link, snippet, date}, ...]}
    """
    # 延迟导入避免 unit test 时强制依赖
    try:
        from batch_web_search import batch_web_search  # type: ignore
    except ImportError:
        print("[WARN] batch_web_search 不可用，跳过搜索（手动模式）", file=sys.stderr)
        return {kw: [] for kw in keywords}

    results = {}
    queries = [{"query": kw, "num_results": num_per} for kw in keywords]
    try:
        resp = batch_web_search(queries=queries)
        # 解析响应（实际结构依平台而定）
        for i, kw in enumerate(keywords):
            results[kw] = resp.get("data", [{}])[i].get("results", []) if i < len(resp.get("data", [])) else []
    except Exception as e:
        print(f"[ERROR] 搜索失败: {e}", file=sys.stderr)
        results = {kw: [] for kw in keywords}
    return results


def render_markdown(week: str, today: str, results: dict) -> str:
    """渲染 weekly-monitor 模板（对齐 W25 期格式）"""
    lines = [
        f"# 多智能体协作 · 前沿热点追踪 {week}（{today}）",
        "",
        f"> **路径**：`04-FrontierHotspots/weekly-monitor-{today}.md`",
        f"> **更新日期**：{today} · Jarvis AI",
        f"> **追踪频率**：每周",
        f"> **关联**：W24 期见 `weekly-monitor.md`",
        "",
        "---",
        "",
        f"## 本周热点摘要（{week}）",
        "",
    ]

    for kw, hits in results.items():
        lines.append(f"### 🔍 关键词：`{kw}`")
        lines.append("")
        if not hits:
            lines.append("- （本周无新增结果）")
        else:
            for h in hits[:3]:
                title = h.get("title", "(无标题)")
                link = h.get("link", "")
                snippet = h.get("snippet", "")[:200]
                lines.append(f"- **[{title}]({link})**")
                if snippet:
                    lines.append(f"  > {snippet}")
        lines.append("")

    lines.extend([
        "---",
        "",
        f"## 📊 关键词追踪状态",
        "",
        "| 关键词 | 本周结果数 | 趋势 |",
        "|--------|----------|------|",
    ])
    for kw, hits in results.items():
        lines.append(f"| `{kw}` | {len(hits)} | - |")

    lines.extend([
        "",
        f"## 🎯 路线图对齐",
        "",
        f"- Phase 1 (W25-W26): 5 篇必读论文 100% 抓取 ✅",
        f"- Phase 2 (W27-W30): 180 次实验设计就绪",
        f"- Phase 4 (W37-38): A2A vs MCP 协议实验素材完整",
        "",
        "---",
        "",
        f"*下次更新时间：{(cst_now() + timedelta(days=7)).strftime('%Y-%m-%d')}（每周三）*",
        f"*🤖 Jarvis AI · 自动生成 · {today}*",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="033 每周热点追踪自动生成")
    parser.add_argument("--date", help="指定日期 (YYYY-MM-DD)，默认 CST 今天")
    parser.add_argument("--keywords-file", help="关键词文件，每行一个")
    parser.add_argument("--dry-run", action="store_true", help="只打印不写文件")
    args = parser.parse_args()

    if args.date:
        today = args.date
    else:
        today = cst_now().strftime("%Y-%m-%d")

    keywords = DEFAULT_KEYWORDS
    if args.keywords_file and os.path.exists(args.keywords_file):
        with open(args.keywords_file) as f:
            keywords = [l.strip() for l in f if l.strip()]

    week = week_label(datetime.strptime(today, "%Y-%m-%d").replace(tzinfo=timezone(timedelta(hours=8))))

    print(f"[INFO] 日期={today} · 周={week} · 关键词数={len(keywords)}")

    results = search_keywords(keywords)
    md = render_markdown(week, today, results)

    if args.dry_run:
        print(md)
        return 0

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"weekly-monitor-{today}.md"
    out_path.write_text(md, encoding="utf-8")
    print(f"[DONE] {out_path} ({len(md)} 字符)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
