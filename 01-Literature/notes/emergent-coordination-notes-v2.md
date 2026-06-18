# Emergent Coordination in Multi-Agent Language Models · 笔记（补抓版）

> **路径**：`01-Literature/notes/emergent-coordination-notes-v2.md`
> **补抓日期**：2026-06-18 · Jarvis AI · 第103天
> **来源**：[OpenReview SRn1MtMPRq](https://openreview.net/forum?id=SRn1MtMPRq)
> **作者**：Christoph Riedl
> **发布日期**：2026-01-26（ICLR 2026 Poster）

---

## 🎯 核心问题

**多智能体 LLM 系统到底是"一堆独立个体的集合"还是"有高层结构的整合集体"？**

---

## 🧠 核心方法

**信息论框架 + 时间延迟互信息分解（TDMI）**

| 元素 | 含义 |
|------|------|
| **TDMI** | Time-Delayed Mutual Information，量化跨 agent 时间耦合 |
| **信息分解** | Partial Information Decomposition，分离真协同 vs 虚假耦合 |
| **涌现判据** | 满足两个条件才算"涌现协同"：① 跨 agent 目标对齐 ② 互补贡献 |
| **实验载体** | 简单猜测游戏 + 三种随机干预（对照组 / 人设 / 心理理论提示） |

---

## 📊 三组实验结果

| 实验条件 | 涌现结构 | 关键观察 |
|---------|---------|---------|
| **Control**（无干预）| ❌ 弱协同 | 强时间协同，但**无跨 agent 对齐** |
| **+ Persona**（人设）| 🟡 中等 | 出现**身份差异化**（identity-linked differentiation） |
| **+ Persona + ToM**（心理理论提示"想想其他 agent 会做什么"）| ✅ **强涌现** | 同时具备**身份差异化** + **目标导向互补** |

> **金句**："Without attributing human-like cognition to the agents, the patterns ... mirror well-established principles of collective intelligence in human groups: **effective performance requires both alignment on shared objectives and complementary contributions across members**."

---

## 💡 对 033 课题的启示

1. **量化"涌现"成为可能** — TDMI 提供客观度量，告别"看现象说涌现"
2. **Prompt 设计是涌现的杠杆** — 单纯"加 agent"无效，需"persona + 心理理论提示"
3. **Phase 3 涌现专题章节** — 可直接复现本文的"猜测游戏 + 三组干预"实验
4. **联系 Wayne 研究** — 网络科学中"集体智能涌现"已有成熟框架（Bianconi 等），可借鉴

---

## 🔬 可复现实验（建议）

```
任务：3-Agent 中文短句补全
干预：
  G1: Control（无 prompt 引导）
  G2: + Persona（"你是一个经济学家/工程师/哲学家"）
  G3: + Persona + ToM（"考虑其他 agent 可能怎么回答"）
度量：TDMI（time-delayed mutual information）
输出：3 组互信息矩阵对比图
```

---

## 📚 与其他论文的关系

- 互补于 Google "Scaling Agent Systems"（架构视角）— 本文是**行为视角**
- 与 OWL（CAMEL-AI）的 WORKFORCE（架构视角）形成 三角验证
- **填补空白**：LLM 多智能体领域第一篇用**信息论度量涌现**的论文

---

## ⚠️ 补抓说明

- **首次抓取（6/12）失败原因**：OpenReview ID 用了占位符 `example-emergent-coordination`
- **二次抓取（6/18）成功**：通过 Google Scholar 搜到真实 ID `SRn1MtMPRq`
- **未来规避**：先 OpenReview Search 拿真实 ID，再用 fetch_papers.py

---

*🤖 Jarvis AI · 第103天 · 2026-06-18 · 补抓成功*
