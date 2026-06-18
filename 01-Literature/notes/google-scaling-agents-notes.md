# Towards a Science of Scaling Agent Systems: When and Why Agent Systems Work

> **来源**：Google DeepMind Research Blog
> **抓取日期**：2026-06-12
> **原 URL**（不可访问）：https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/
> **备用源**：https://www.media.mit.edu/projects/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/overview/
> **arXiv ID**：2512.08296
> **状态**：✅ 数据已抓取（备用源）

---

## 📋 元数据

| 字段 | 内容 |
|------|------|
| **标题** | Towards a Science of Scaling Agent Systems: When and Why Agent Systems Work |
| **机构** | Google DeepMind |
| **发布日期** | 2026-01-28（博客）/ 2026-04-08（论文） |
| **arXiv** | 2512.08296 |
| **类别** | 规模化规律（工程） |
| **优先级** | ⭐必读 |

---

## 🔬 实验设计

**180 种 agent 配置（agent configurations）的大规模受控评估**——这是 033 报告 v1.0 中"39-70%"数字的真正来源。

---

## 📊 核心数据

| 任务类型 | 单 Agent | 多 Agent | 差距 |
|---------|---------|---------|------|
| **可并行化任务**（如金融分析） | 基准 | **+81%** | 多 Agent 显著胜出 |
| **严格顺序任务**（如 PlanCraft 规划） | 基准 | **−39% ~ −70%** | 多 Agent 大幅下降 |

### 关键结论

1. **可并行化任务**：多 Agent 系统性能比单 Agent 高 **80.9-81%**
2. **顺序任务**（PlanCraft）：所有多 Agent 变体性能下降 **39-70%**
3. **通信开销**是顺序任务性能下降的主要原因
4. **挑战"agent 越多越好"**——应根据任务特性选架构

---

## 💡 关键发现

- **没有"最佳 agent 数量"**——应按任务可分解性 + 工具密度选 agent **架构**
- **通信开销**在顺序任务和工具密集任务上尤其严重
- **多 Agent ≠ 通用方案**——只对"可并行化"任务有效

---

## 🎓 对 033 的价值

- **直接对应**：v1.0 报告核心发现 #1「通信开销 39-70%」
- **数据补全**：补充了"+81%（可并行任务）"的正向数据
- **修正方向**：v1.0 报告应同时呈现"−39~70%（顺序）"和"+81%（并行）"两个数据
- **设计影响**：design-v0.1.md 应区分"并行任务"和"顺序任务"两组实验

---

## ⚠️ 重要数据更新建议

v1.0 报告第 1 条核心发现应改为：
> "在**顺序任务**（如规划）上多智能体性能下降 39-70%；在**可并行任务**（如金融分析）上多智能体性能提升 81%——多智能体效果**高度依赖任务类型**"

---

*🤖 Jarvis AI · 第97天 · 2026-06-12 · 备用源抓取*
