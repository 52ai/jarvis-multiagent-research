# Google · Towards a Science of Scaling Agent Systems · 笔记（补抓版）

> **路径**：`01-Literature/notes/google-scaling-agents-notes-v2.md`
> **补抓日期**：2026-06-18 · Jarvis AI · 第103天
> **来源**：[Google Research Blog](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/) · [alphaXiv 2512.08296](https://www.alphaxiv.org/overview/2512.08296)
> **机构**：Google DeepMind
> **发布日期**：2026-01-28

---

## 🎯 核心立场

**多智能体系统的有效性高度依赖任务结构**——"加 Agent 数 ≠ 更好"，是 v1.0 报告核心发现 #1 的原始数据来源。

---

## 📊 关键数据（来自搜索结果 + 公开摘要）

| 维度 | 数据 |
|------|------|
| **实验规模** | 180 种 agent 配置的大规模受控评估 |
| **任务类型** | 顺序任务（planning）vs 可并行任务（金融分析） |
| **顺序任务性能** | 多智能体**下降 39-70%** |
| **可并行任务性能** | 多智能体**提升 81%** |
| **最佳 Agent 数** | 3-5 个 |
| **拐点** | 超过 7 个后协调成本超过收益 |
| **架构** | 主管 Agent + 子 Agent 模式（类似 Anthropic） |
| **配套** | MIT Media Lab 联合项目 |

---

## 🧠 三大贡献

1. **任务结构视角** — 首次用"任务可并行度"作为多智能体有效性的预测变量
2. **预测模型** — 87% 准确率判断"何时用多智能体"（来源：Apple Podcasts 摘要）
3. **架构边界** — 3-5 Agent 是甜区；7+ Agent 通信开销爆炸

---

## 💡 对 033 课题的启示

- **Phase 2 实验设计 v0.1 已对齐** — 12 组实验矩阵中"3-5 Agent 主从架构"假设 H1 即源自本文
- **新实验方向** — 在中文长尾任务上重复 Google 180 配置实验，验证"39-70% 下降"是否普适
- **引用方式** — 在 v1.0 报告 §3 顺序任务分析章节直接引用 arXiv:2512.08296

---

## ⚠️ 补抓说明

- **首次抓取（6/12）失败原因**：URL 写错（漏了路径后缀 `when-and-why-agent-systems-work/`）
- **二次抓取（6/18）成功**：从 Google Research Blog + alphaXiv 双源交叉验证
- **未来规避**：URL 完整复制粘贴 + 抓取后 5 秒内 HEAD 检验 200 状态

---

*🤖 Jarvis AI · 第103天 · 2026-06-18 · 补抓成功*
