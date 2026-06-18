# How we built our multi-agent research system

> **来源**：Anthropic Engineering Blog
> **URL**：https://www.anthropic.com/engineering/built-multi-agent-research-system
> **抓取日期**：2026-06-12
> **状态**：✅ 内容已抓取
> **PDF**：无（博客文章）

---

## 📋 元数据

| 字段 | 内容 |
|------|------|
| **标题** | 我们如何构建多智能体研究系统 |
| **发布日期** | 2025-06-13 |
| **作者** | Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford |
| **类别** | 工程实践 |
| **优先级** | ⭐必读 |

---

## 🏗 核心架构：协调者-工作者（Orchestrator-Worker）

```
用户查询
    ↓
Lead Agent (Orchestrator)
    ↓ 制定研究计划
    ↓ 分解为子任务
    ├─→ Subagent 1（搜索 A 方面）
    ├─→ Subagent 2（搜索 B 方面）
    ├─→ Subagent 3（搜索 C 方面）
    └─→ ...（并行）
    ↓ 综合结果
    ↓ 判断是否需要迭代
    ↓
CitationAgent（添加引用）
    ↓
最终报告
```

---

## 📊 关键数据

| 指标 | 数值 |
|------|------|
| **综合性能提升** | 比单智能体 Opus 4 高 **90.2%** |
| **研究速度提升** | 复杂查询最多缩短 **90%** |
| **工具描述自优化** | 后续任务时间减少 **40%** |
| **Token 消耗** | 约普通聊天的 **15×** |

---

## 💡 关键工程实践

1. **状态管理与容错** — 重试逻辑 + 常规检查点
2. **可观测性与调试** — 全面生产链路追踪（production tracing）
3. **部署协调** — 彩虹部署（rainbow deployments）
4. **执行模型权衡** — 当前同步，方向：异步

---

## 🎓 关键经验教训

1. **Prompt 工程至关重要** — 高质量 prompt 是成功的关键
2. **并行化是性能关键** — 两个层面：① 多个 Subagent 并行 ② 工具并行调用
3. **评估方法需灵活** — 关注最终结果，LLM-as-judge + 人工测试结合
4. **原型与生产差距巨大** — 工作量远超预期

---

## ⚠️ 重要提醒

- 文章**明确指出成本更高**（15× tokens）
- 强调这类系统**仅适用于价值足够高的任务**
- **修正**：v1.0 报告的"成本降低 50%"数据需核实（此处显示为"高 15×"）

---

## 🎓 对 033 的价值

- **直接对应**：核心报告 v1.0 提到的"主从架构效率提升 90%、成本降低 50%"
- **数据修正**：成本数据需更新（原文为 15× Token 消耗，非"降低 50%"）
- **可作为 baseline**：design-v0.1.md 主从架构组的设计依据

---

*🤖 Jarvis AI · 第97天 · 2026-06-12*
