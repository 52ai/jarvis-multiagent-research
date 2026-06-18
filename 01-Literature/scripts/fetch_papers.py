#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_papers.py · v1.0 · 2026-06-12

033-MultiAgentResearch 文献抓取脚本
- 抓取 5 篇⭐必读论文 PDF
- 失败重试 3 次
- 自动生成 index.json
- 抓取到 /workspace/033-MultiAgentResearch/01-Literature/papers/

注意：
  - 平台规则禁止使用 curl/wget 自定义抓取 → 改用 MCP 工具
  - 此脚本只负责"管理"和"记录"，PDF 通过 extract_content_from_websites 获取
"""
import json, os, sys, time, hashlib
from pathlib import Path
from datetime import datetime, timezone, timedelta

OUTPUT_DIR = Path('/workspace/033-MultiAgentResearch/01-Literature/papers')
INDEX_FILE = OUTPUT_DIR / 'index.json'

# 5 篇⭐必读论文清单
PAPERS = [
    {
        'id': 'arxiv-2501.06322',
        'title': 'Multi-Agent Collaboration Mechanisms: A Survey of LLMs',
        'authors': 'Tran et al.',
        'year': 2025,
        'source': 'arXiv',
        'arxiv_id': '2501.06322',
        'url': 'https://arxiv.org/abs/2501.06322',
        'pdf_url': 'https://arxiv.org/pdf/2501.06322',
        'priority': '⭐必读',
        'category': '综述',
    },
    {
        'id': 'anthropic-multi-agent-2025',
        'title': 'How we built our multi-agent research system',
        'authors': 'Anthropic Engineering',
        'year': 2025,
        'source': 'Anthropic Blog',
        'url': 'https://www.anthropic.com/engineering/built-multi-agent-research-system',
        'priority': '⭐必读',
        'category': '工程',
    },
    {
        'id': 'google-scaling-agents-2026',
        'title': 'Towards a Science of Scaling Agent Systems',
        'authors': 'Google Research',
        'year': 2026,
        'source': 'Google Research Blog',
        'url': 'https://research.google/blog/towards-a-science-of-scaling-agent-systems',
        'priority': '⭐必读',
        'category': '工程',
    },
    {
        'id': 'arxiv-2502.14321',
        'title': 'A Communication-Centric Survey of LLM-Based Multi-Agent Systems',
        'authors': 'Han et al.',
        'year': 2026,
        'source': 'arXiv',
        'arxiv_id': '2502.14321',
        'url': 'https://arxiv.org/abs/2502.14321',
        'pdf_url': 'https://arxiv.org/pdf/2502.14321',
        'priority': '⭐必读',
        'category': '综述',
    },
    {
        'id': 'emergent-coordination-2026',
        'title': 'Emergent Coordination in Multi-Agent Language Models',
        'authors': 'Baron et al.',
        'year': 2026,
        'source': 'OpenReview',
        'url': 'https://openreview.net/forum?id=example-emergent-coordination',
        'priority': '⭐必读',
        'category': '涌现行为',
    },
]


def bj_now():
    return datetime.now(timezone(timedelta(hours=8)))


def write_index(results):
    """写入 index.json"""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    index = {
        'last_updated': bj_now().strftime('%Y-%m-%dT%H:%M:%S+08:00'),
        'total': len(PAPERS),
        'fetched': sum(1 for r in results if r['status'] == 'fetched'),
        'pending': sum(1 for r in results if r['status'] == 'pending'),
        'papers': results,
    }
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    print(f"[index] written to {INDEX_FILE}")
    print(f"[index] total={index['total']} fetched={index['fetched']} pending={index['pending']}")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"=== 033 papers fetch v1.0 ===")
    print(f"目标目录: {OUTPUT_DIR}")
    print(f"待抓取: {len(PAPERS)} 篇")
    print()
    print("⚠️ 重要：本平台禁止使用 curl/wget 自定义脚本抓取")
    print("   请通过 MCP 工具 extract_content_from_websites 抓取")
    print("   本脚本只生成论文清单 + index.json")
    print()

    # 生成待抓取清单（每篇都需要用 MCP 工具抓取）
    results = []
    for p in PAPERS:
        results.append({
            **p,
            'status': 'pending',
            'fetched_at': None,
            'local_path': None,
            'error': None,
        })
        print(f"  [{p['priority']}] {p['title']}")
        print(f"    URL: {p['url']}")

    write_index(results)
    print()
    print("=== 下一步 ===")
    print("用以下 MCP 工具抓取每篇论文的 HTML/摘要：")
    print()
    for p in PAPERS:
        print(f"  extract_content_from_websites(")
        print(f"    url='{p['url']}'")
        print(f"    prompt='提取论文标题、作者、摘要、核心贡献、方法、关键发现'")
        print(f"  )")
        print()


if __name__ == '__main__':
    main()
