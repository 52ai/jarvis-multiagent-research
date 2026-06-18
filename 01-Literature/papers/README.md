# 必读论文 · papers/

> **路径**：`01-Literature/papers/`
> **目标**：抓取 5 篇⭐必读论文全文，沉淀研读素材
> **启动日期**：2026-06-12

---

## 📥 抓取状态

| 序号 | 论文 | 来源 | 状态 | 本地文件 |
|------|------|------|------|----------|
| 1 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | arXiv:2501.06322 | ⏳ 待抓 | - |
| 2 | How we built our multi-agent research system | Anthropic Blog | ⏳ 待抓 | - |
| 3 | Towards a Science of Scaling Agent Systems | Google Research | ⏳ 待抓 | - |
| 4 | A Communication-Centric Survey of LLM-Based MAS | arXiv:2502.14321 | ⏳ 待抓 | - |
| 5 | Emergent Coordination in Multi-Agent Language Models | OpenReview | ⏳ 待抓 | - |

---

## 📝 抓取方法

**首选渠道**（按优先级）：
1. arXiv 官方 PDF（`https://arxiv.org/pdf/{id}.pdf`）
2. Semantic Scholar API（`https://api.semanticscholar.org/graph/v1/paper/{id}`）
3. OpenReview / 会议官网
4. 论文作者主页

**存储约定**：
- PDF 文件命名：`{arxiv-id}.pdf` 或 `{venue-year-slug}.pdf`
- 元数据：`papers/index.json`
- 笔记：`../notes/{arxiv-id}-notes.md`

---

## 🎯 抓取脚本（W26 待实现）

```python
# 计划路径：/workspace/033-MultiAgentResearch/01-Literature/scripts/fetch_papers.py
# 功能：批量下载 → 自动命名 → 生成 index.json
# 工具：requests + arxiv API
```

---

## ⚠️ 注意事项

- **版权**：仅供个人研究使用，不外部分发
- **Token**：抓取 PDF 本身不消耗 LLM Token，OCR/LLM 解析时才消耗
- **失败重试**：3 次重试 + 备用源降级
- **大小限制**：单 PDF 控制在 10MB 以内（兼容性）

---

*🤖 Jarvis AI · 第97天 · 2026-06-12 · papers/ 目录初始化*
