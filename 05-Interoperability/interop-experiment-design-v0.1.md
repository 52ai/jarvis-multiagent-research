# 033 Phase 2 · 互联互通组实验设计 v0.1

> **路径**：`05-Interoperability/interop-experiment-design-v0.1.md`
> **创建**：2026-06-18 · Jarvis AI · 第103天
> **目标**：把"互联互通"作为第 13 个实验架构组，实装进 033 Phase 2

---

## 🎯 实验目标

**核心问题**：在 033 现有 5 任务（T1-T5）上，**不同互联互通架构的性能差异**？

**假设（基于已有文献）**：
- **H1**：MCP 工具密集型任务（T1/T2）上表现最好
- **H2**：A2A 协作密集型任务（T4/T5）上表现最好
- **H3**：AIP（国产标准）在跨境场景中比国际协议更稳定
- **H4**：混合（MCP+A2A）在复杂任务（T3）上最优

---

## 🏛️ 4 互联互通架构

| ID | 架构名 | 组成 | 适用任务 | 实现成本 |
|----|--------|------|---------|---------|
| **E13-A** | `single-mcp` | 1 Lead + N MCP tools | T1/T2 工具密集 | 低 |
| **E13-B** | `single-a2a` | 1 Lead + 3 Sub-agents via A2A | T4/T5 协作密集 | 中 |
| **E13-C** | `hybrid-mcp-a2a` | Lead + Sub + MCP tools | T3 混合任务 | 高 |
| **E13-D** | `ain-routed` | AIN-like intent router + 多 domain | T5 涌现 | 极高 |

### 详细架构图

```
[E13-A] single-mcp
─────────────────
[Opus 4 Lead]
    ├── MCP → 搜索工具
    ├── MCP → 数据库
    └── MCP → Python 解释器


[E13-B] single-a2a
─────────────────
[Opus 4 Lead]  ◀──A2A──▶  [Sonnet 4 Researcher]
    │                          │
    │                          ├── MCP → 工具
    ▼                          ▼
[Sonnet 4 Writer]  ◀──A2A──▶  [Sonnet 4 Reviewer]


[E13-C] hybrid-mcp-a2a
──────────────────────
[Opus 4 Lead]
    │
    ├── A2A → Researcher
    │            └── MCP → 搜索/文献
    │
    ├── A2A → Writer
    │            └── MCP → 文档工具
    │
    └── A2A → Reviewer
                 └── MCP → 审核规则


[E13-D] ain-routed
──────────────────
[Intent Router (Opus 4)]
    │
    ├── [Domain: 研究]  → Researcher agent
    │                     └── MCP
    │
    ├── [Domain: 写作]  → Writer agent
    │                     └── MCP
    │
    └── [Domain: 审核]  → Reviewer agent
                          └── MCP
[Capability Routing Table]  ← 能力注册中心
```

---

## 📋 实验矩阵

### 任务 × 架构 × 重复

| 任务 | E13-A single-mcp | E13-B single-a2a | E13-C hybrid | E13-D ain-routed |
|------|------------------|------------------|--------------|-------------------|
| T1 综述 | ✅ ×3 | ✅ ×3 | ✅ ×3 | ✅ ×3 |
| T2 推理优化 | ✅ ×3 | ✅ ×3 | ✅ ×3 | ✅ ×3 |
| T3 A2A vs MCP | ✅ ×3 | ✅ ×3 | ✅ ×3 | ✅ ×3 |
| T4 Agent 安全 | ✅ ×3 | ✅ ×3 | ✅ ×3 | ✅ ×3 |
| T5 涌现行为 | ✅ ×3 | ✅ ×3 | ✅ ×3 | ✅ ×3 |

**总实验数**：4 架构 × 5 任务 × 3 重复 = **60 run**

### 与已有 180 run 合并

| 类别 | Run 数 | 占比 |
|------|--------|------|
| 原有 12 架构 (Phase 2) | 180 | 75% |
| **新增 4 互联互通架构** | **60** | **25%** |
| **Phase 2 总数** | **240** | **100%** |

---

## 🔬 度量维度（超越已有 4 维）

### 复用：4 维 LLM-as-judge
- fact_accuracy / structure_completeness / readability / insight_depth

### 新增：3 维互联互通专项
| 维度 | 含义 | 度量方法 |
|------|------|---------|
| **interop_score** | 互联互通完整度 | 输出是否调用了 2+ 智能体/工具（Y/N）|
| **latency_overhead** | 协议开销 | 单次 A2A 委派 vs 单次 MCP 调用的延迟差 |
| **token_efficiency** | 协议层 token 效率 | 完成相同任务，互联互通组 vs single agent 的 token 比 |

### 总计：7 维评分

| # | 维度 | 权重 | 已有/新增 |
|---|------|------|----------|
| 1 | fact_accuracy | 30% | 已有 |
| 2 | structure_completeness | 15% | 已有 |
| 3 | readability | 15% | 已有 |
| 4 | insight_depth | 20% | 已有 |
| 5 | **interop_score** | 10% | **新增** |
| 6 | **latency_overhead** | 5% | **新增** |
| 7 | **token_efficiency** | 5% | **新增** |

---

## 📅 实验时间表

| 阶段 | 时间 | 工作 |
|------|------|------|
| **W26 (本周)** | 6/22-6/28 | 实验设计 v0.1 (本文件) + 评估器升级 |
| **W27 (下周)** | 6/29-7/5 | 接入 LLM API + 实装 4 架构 stub |
| **W28** | 7/6-7/12 | 跑 60 run + 数据收集 |
| **W29** | 7/13-7/19 | 评估 + 聚合 + v0.5 报告 |
| **W30** | 7/20-7/26 | 撰写 v0.2 互联互通专题报告（含实验结论）|

---

## 🛠️ 实装计划

### W27 必做

1. **升级 run_baseline_v0.1.py** → 接受 `--architecture` 参数扩展
2. **新增 4 架构配置文件** `02-Experiments/benchmarks/architectures/interop_*.json`
3. **实现 stub 调度器** `02-Experiments/scripts/interop_runner.py`
   - 输入：task_id + architecture_id
   - 输出：run_<id>.json
4. **升级 llm_judge.py** → 支持 7 维评分
5. **升级 result_aggregator.py** → 按"原有 12 架构 vs 互联互通 4 架构"分组

### W28 必做
6. 跑 60 run（可并发 = ~6-12 小时）
7. 收集 token / latency / 互操作证据
8. 生成 cross-architecture 对比表

---

## 📊 预期产出

### 文档
- `02-Experiments/results/interop_60runs_<date>.json` — 60 run 原始数据
- `02-Experiments/results/interop_aggregate_report_<date>.md` — 跨架构对比
- `02-Experiments/results/interop_visualization_<date>.png` — 性能雷达图

### 报告增量
- `05-Interoperability/智能体互联互通专题报告-v0.2.md`
  - 新增 §12 实验设计（本文档）
  - 新增 §13 实验结果（4 架构对比）
  - 新增 §14 中国 AIP 标准 vs 国际协议

---

## 🧪 H1-H4 假设验证计划

| 假设 | 验证方法 | 通过条件 |
|------|---------|---------|
| **H1** MCP 工具密集型优 | E13-A vs single 在 T1/T2 的 fact_accuracy 对比 | E13-A 显著高于 single (p<0.05) |
| **H2** A2A 协作密集型优 | E13-B vs single 在 T4/T5 的 insight_depth 对比 | E13-B 显著高于 single |
| **H3** AIP 跨境场景稳定 | T5（含跨境数据）综合分对比 | E13-D 在跨境子集上稳定性高 |
| **H4** 混合在 T3 最优 | E13-C vs 其他 3 架构在 T3 的综合分 | E13-C 最高 |

**统计方法**：t 检验 + ANOVA + 效应量（Cohen's d）

---

## 📦 文件清单（本次新增）

```
05-Interoperability/
└── interop-experiment-design-v0.1.md      ← 本文件

02-Experiments/
├── benchmarks/
│   └── architectures/                      ← W27 新建
│       ├── interop_single_mcp.json
│       ├── interop_single_a2a.json
│       ├── interop_hybrid.json
│       └── interop_ain_routed.json
├── scripts/
│   └── interop_runner.py                   ← W27 新建
└── results/                                ← W28 填充
    ├── run_E13A_*.json × 15
    ├── run_E13B_*.json × 15
    ├── run_E13C_*.json × 15
    └── run_E13D_*.json × 15
```

---

*🤖 Jarvis AI · 第103天 · 2026-06-18 · 033 互联互通组实验设计 v0.1*
