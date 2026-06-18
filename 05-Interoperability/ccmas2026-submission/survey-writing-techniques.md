# 优秀综述论文写作技巧学习笔记

> **路径**：`05-Interoperability/ccmas2026-submission/survey-writing-techniques.md`
> **日期**：2026-06-18 20:06
> **目的**：学习 ACM/IEEE/NeurIPS 顶会综述的写作范式 → 提升 Paper 1 质量
> **标杆论文**：
> - **arXiv:2505.02279** "A Survey of Agent Interoperability Protocols"（直接竞品）
> - **arXiv:2501.06322** "Multi-Agent Collaboration Mechanisms"（602 引用）
> - **arXiv:2308.11432** "A Survey on LLM-based Autonomous Agents"（4000+ 引用）

---

## 🎓 论文 1：arXiv:2505.02279（直接竞品）

> Yang et al. "A Survey of Agent Interoperability Protocols: MCP, ACP, A2A, ANP"

### 10 章结构

```
1 Introduction
2 Challenges and Solutions in Agent Protocol Interoperability  ← ★ 问题-方案框架
3 Background and Related Work
  3.1 AI Agents: Definition and Scope
  3.2 Early Symbolic Agent Languages
  3.3 Service-Oriented Integrations and RAG
  3.4 LLM Agents and Function Calling
  3.5 Orchestration and Lightweight Agent Frameworks
  3.6 Protocol Evolution Timeline  ← ★ 演化时间线
4 MCP (Model Context Protocol)  ← 每个协议都按统一结构
  4.1 Client Application
  4.2 MCP Server
  4.3 Core Components
  4.4 MCP Server Core Capabilities
  4.5 MCP Connection Lifecycle
  4.6 Security Challenges and Mitigations  ← ★ 安全性独立成章
5 A2A Architecture
  ...
8 Comparison of Agent Protocols  ← ★ 对比表
9 Phased Adoption Roadmap  ← ★ 可执行路径
10 Conclusion
```

### 8 大写作技巧（金标准）

#### 1️⃣ Problem-Solution Framing（问题-方案框架）

**在介绍协议之前，先说为什么需要**。

第 2 章直接列出 4 个产业挑战 → 映射到 4 个协议：
- 工具调用问题 → MCP
- 多模态消息 → ACP
- 企业 P2P 编排 → A2A
- 去中心化开放网络 → ANP

**论文启示**：第 1 章写"封闭世界问题"后，应在第 2 章立刻给出"为什么需要 Agent Internet"。

#### 2️⃣ Strict Structural Parallelism（严格结构平行）

**每个协议按相同子结构介绍**：
- 概述 → 核心组件 → 生命周期 → 安全性

**论文启示**：介绍 MCP/A2A/AIN/ANS/DNS-AID 时**严格用相同子结构**。

#### 3️⃣ Lifecycle Normalization Lens（生命周期归一化）

**用统一框架（创建/运行/更新/终止）比较不同协议**。

**论文启示**：用 4 阶段生命周期（注册/发现/调用/退役）作为统一视角比较所有发现协议。

#### 4️⃣ Actionable Synthesis（可执行综合）

**第 9 章直接给"分阶段采纳路线图"**：
- Stage 1: MCP 用于工具调用
- Stage 2: ACP 用于富交互
- Stage 3: A2A 用于企业协作
- Stage 4: ANP 用于开放市场

**论文启示**：我们的"协议桥接 3 策略"应该升级为"分阶段采纳路线图（2026→2030）"。

#### 5️⃣ High Information Density via Tables（高密度信息表）

**冗长技术细节放表格，正文保持分析性**。

本文有 7 张表：
- Table 1: 轻量 LLM Agent 框架
- Table 2: 互操作里程碑时间线
- Table 3-6: 4 协议 × 4 阶段威胁/缓解
- **Table 7: 协议主对比矩阵**

**论文启示**：把"5 协议对比"做成单一对比矩阵表。

#### 6️⃣ Historical Evolution Timeline（历史演化时间线）

**Figure 2 + Table 2: 互操作演化时间线**：
- 1993-2006: 符号化 & SOA 基础
- 2020-2023: 检索 & 模型内动作
- 2024-2025: 协议导向互操作

**论文启示**：论文应有 1 张"互联互通演化时间线图"（从 hosts 文件 → DNS → MCP/A2A）。

#### 7️⃣ Security is a Lifecycle Problem（安全是生命周期问题）

**威胁不只发生在执行期，而是横跨创建/更新/终止期**。

**论文启示**：安全章节按生命周期组织，而不是按协议组织。

#### 8️⃣ Phased Adoption Roadmap（分阶段采纳路线图）

**不是"企业应该用什么协议"，而是"如何从阶段 1 走到阶段 4"**。

**论文启示**：第 8 章（建议）应升级为"4 阶段采纳路线图"：
- Stage 1: MCP（事实标准）
- Stage 2: A2A（企业内）
- Stage 3: ANS/DNS-AID（命名）
- Stage 4: AIN（跨域路由）

---

## 🎓 论文 2：arXiv:2501.06322（602 引用）

> Tran et al. "Multi-Agent Collaboration Mechanisms: A Survey of LLMs"

### 关键贡献

- **可扩展框架**指导未来研究
- 调查多领域应用（5G/6G、Industry 5.0、QA、社交）
- 识别开放挑战

### 6 大协作维度（taxonomy）

| 维度 | 含义 |
|------|------|
| **Actors** | 参与的智能体 |
| **Types** | 合作/竞争/竞合 |
| **Structures** | P2P/中心化/分布式 |
| **Strategies** | 角色型/模型型 |
| **Coordination Protocols** | 协调协议规则 |
| **Applications** | 应用领域分类 |

**论文启示**：我们的 4 维度（业务/协议/网络/评价）可以借鉴这个 6 维度扩展为 "Agent Internet 6 维度"。

---

## 🎓 论文 3：arXiv:2308.11432（4000+ 引用）

> Wang et al. "A Survey on LLM-based Autonomous Agents" - **HuggingFace 经典**

### 引用 4000+ 的原因

- **Holistic perspective**：从构造/应用/评估三角度
- **Comprehensive**：覆盖 100+ 论文
- **Systematic**：结构化对比表

**论文启示**：引用 4000+ 的关键是**全面性**（100+ 论文）和**系统性**（多角度结构）。

---

## 📊 三大综述论文范式对比

| 维度 | 2505.02279 | 2501.06322 | 2308.11432 |
|------|-----------|-----------|-----------|
| **页数** | ~20 | ~30 | ~50 |
| **引用数** | 较新 | 602 | 4000+ |
| **核心技巧** | Lifecycle + Roadmap | Taxonomy + Framework | Holistic |
| **最大价值** | 安全分析 + 采纳路线图 | 6 维度分类 | 全面性 |
| **对我们适用度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

---

## 🎯 Paper 1 v4.0 重设计（应用 8 大技巧）

### 新增章节

| 当前 | v4.0 新增 | 应用技巧 |
|------|----------|---------|
| §1 引言 | §1 引言（强化 Problem-Solution） | 技巧 1 |
| - | **§2 互联互通挑战与方案映射** | 技巧 1 |
| §2 相关工作 | §3 背景与演化时间线 | 技巧 6 |
| - | **§2.1 互联互通演化时间线图** | 技巧 6 |
| §3 形式化 | §4 形式化模型 | 保留 |
| §4 AITM | §5 AITM 拓扑 | 保留 |
| §5 实验 | §6 计算实验 | 保留 |
| §6 协议地理学 | §7 协议对比矩阵（Table） | 技巧 5 |
| - | **§8 安全分析（4 阶段）** | 技巧 7 |
| §7 Agent Rank | §9 Agent Rank | 保留 |
| §8 建议 | **§10 分阶段采纳路线图** | 技巧 4+8 |
| §9 结论 | §11 结论 | 保留 |

### 新增图表清单

1. **Figure 1**：Agent Internet 三层架构图（业务/协议/网络）
2. **Figure 2**：互联互通演化时间线（hosts 文件 → DNS → MCP/A2A）
3. **Figure 3**：4 协议生命周期流程图（统一结构）
4. **Figure 4**：协议地理学地图（中/美/欧三方）
5. **Figure 5**：BA 拓扑可视化（1000 节点 + Agent Rank 着色）
6. **Table 1**：4 协议主对比矩阵（架构/发现/认证/格式/范围/优势/限制）
7. **Table 2**：5 协议安全威胁与缓解（按生命周期）
8. **Table 3**：分阶段采纳路线图

### 写作风格调整

| 当前 | 改进 |
|------|------|
| 段落式描述 | 大量表格 + 简要分析 |
| "我们认为..." | "本文提出..."（更客观）|
| 引用论文罗列 | 按主题归类引用 |
| 缺乏可视化 | 5 图 + 8 表 |
| 缺少安全视角 | 加安全分析章节 |
| 缺少采纳路径 | 加 4 阶段路线图 |

### 引用量目标

- 当前：22 篇
- 目标：**50+ 篇**（提升 2.3x）
- 重点引用：arXiv:2505.02279（直接竞品，必须引用）

---

## 📝 立即可执行的 4 件事

按 Wayne "不着急，先完善论文"指示：

### 第 1 件：写"互联互通演化时间线"章节（30 分钟）

参考 2505.02279 风格：
```
1983-1998: ARPANET → DNS（hosts 文件时代结束）
1998-2010: SOA / Web Services（封闭系统）
2010-2020: REST / GraphQL（应用层 API）
2020-2023: LLM + RAG（基础智能体）
2024-2025: MCP（工具调用事实标准）
2025: A2A（智能体协作）
2026-2027: AIN / DNS-AID / ANS（标准化）
2027-2028: 区域互通
2029+: 智能体互联网
```

### 第 2 件：写 4 协议主对比矩阵表（30 分钟）

**7 维度 × 4 协议主对比**：

| 维度 | DNS-AID | ANS-v2 | AGNTCY | AIN |
|------|---------|--------|--------|-----|
| 架构 | DNS | DNS+Registry | HTTPS | 多跳 |
| 发现 | SVCB+DANE | ANS API | 中心目录 | 路由 |
| 认证 | DNSSEC | TLSA | JWT | 链上 |
| 格式 | SVCB | JSON+TLS | JSON+TLS | 路由协议 |
| 范围 | 全球 | 域内 | 平台 | 跨域 |
| 优势 | 速度快 | 灵活 | 易部署 | 跨域 |
| 限制 | 静态 | 需注册 | 单点 | 复杂 |

### 第 3 件：写 4 阶段采纳路线图（30 分钟）

**Stage 1: 工具层（2026）** —— MCP
**Stage 2: 协作层（2026-2027）** —— A2A
**Stage 3: 命名层（2027-2028）** —— ANS/DNS-AID
**Stage 4: 跨域层（2028-2030）** —— AIN

### 第 4 件：重写引言为 Problem-Solution 框架（30 分钟）

直接列 4 个产业痛点：
1. 智能体跨平台协作难
2. 智能体身份不可信
3. 智能体服务难定价
4. 智能体责任难归属

→ 映射到本文解决方案。

---

## ⏰ 时间表（按"不着急"指示拉长）

| 时间 | 任务 |
|------|------|
| 6/18 20:00-22:00 | 写演化时间线 + 采纳路线图 + 4 协议对比表 |
| 6/19 | 重写引言（Problem-Solution）+ 加安全分析章节 |
| 6/20 | 生成 5 张图（架构/时间线/拓扑/地理/流程）|
| 6/21 | 引用扩充到 50+ + 重新编号 |
| 6/22 | 全文精修 + LaTeX 格式（如需要）|
| 6/23 | v4.0 终版 + 提交 |
| 6/24-26 | 备用 + 答辩准备 |

---

## ❓ 待 Wayne 决策

1. **4 件事是否一起做**？（预计 2 小时）
2. **图表用什么工具生成**？（matplotlib / mermaid / Graphviz / draw.io）
3. **是否需要英文版同步写**？
4. **引用 50+ 是否需要**？（需要更多文献调研）

---

*🤖 Jarvis AI · 第103天 · 2026-06-18 · 综述写作技巧学习笔记*

> **核心收获**：3 篇标杆论文的 8 大写作技巧全部学完。论文从"内容堆砌"升级为"结构化综述"路径清晰。
> 关键技巧：
> 1. Problem-Solution 框架
> 2. 结构平行
> 3. 生命周期归一化
> 4. 可执行路线图
> 5. 高密度信息表
> 6. 历史时间线
> 7. 生命周期化安全
> 8. 分阶段采纳路线图
