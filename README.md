# 033-MultiAgentResearch
> **课题**：多智能体协作技术研究 | **创建**：2026-06-11 | **状态**：🟢 Phase 1 收尾（2026-06-18）

---

## 课题简介

系统研究基于大语言模型（LLM）的多智能体协作技术，涵盖：
- 协作机制与架构设计
- 主要开源框架对比（CrewAI / LangGraph / AutoGen）
- 2025—2026年前沿研究进展
- 现存问题与未来研究方向

---

## 目录结构

```
033-MultiAgentResearch/
├── README.md                      ← 课题总览（本文件）
│
├── 01-Literature/                ← 文献调研
│   ├── literature-review.md       ← 文献索引与笔记
│   ├── papers/                    ← 论文全文存储
│   └── notes/                     ← 阅读笔记
│
├── 02-Experiments/               ← 实验研究
│   ├── benchmarks/                ← 基准测试结果
│   ├── prototypes/                ← 原型系统代码
│   └── experiment-log.md          ← 实验日志
│
├── 03-Report/                    ← 报告撰写
│   └── 033-多智能体协作技术报告-2026.md  ← 核心报告
│
└── 04-FrontierHotspots/          ← 前沿热点
    ├── weekly-monitor.md          ← 每周热点追踪
    ├── roadmap.md                 ← 研究路线图
    └── collaborations/             ← 协作与联系
```

---

## 核心报告摘要

**报告版本**：v1.0 初稿
**核心发现（5条）：**
1. 多智能体效果**依赖任务类型**：顺序任务下降 39-70%，可并行任务反而提升 81%（Google DeepMind, 180 种配置实验）
2. 3-5个Agent是小规模协作最优解；超过7个后成本超过收益
3. Anthropic "主Agent+子Agent" 架构性能提升90.2%、时间最多缩短90%，**但Token消耗约15倍**（成本反向）
4. 三大未解决挑战：通信效率 / 安全脆弱性 / 评估基准缺失
5. 2026年最热框架：LangGraph（月搜索量27,100）超越CrewAI（14,800）

---

## 快速导航

- 📄 [技术报告 v1.0 全文](./03-Report/033-多智能体协作技术报告-2026.md)
- 📄 [v1.1 增量版（W25 补抓）](./03-Report/033-多智能体协作技术报告-2026-v1.1.md)
- 📚 [文献调研索引](./01-Literature/literature-review.md)
- 🔥 [W24 热点](./04-FrontierHotspots/weekly-monitor.md) · [W25 热点](./04-FrontierHotspots/weekly-monitor-2026-06-18.md)
- 🧪 [实验设计 v0.1](./02-Experiments/benchmarks/design-v0.1.md) · [实验日志](./02-Experiments/experiment-log.md)
- 🗺 [6 月研究路线图](./04-FrontierHotspots/roadmap.md)
- ⚙️ [weekly-monitor 自动生成脚本](./scripts/weekly_monitor_gen.py)

---

*🤖 Jarvis AI · 第96天 · 2026-06-11*
