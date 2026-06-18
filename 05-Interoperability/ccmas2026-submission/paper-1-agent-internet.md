# Paper 1 完整摘要 + 大纲

> **标题**：Agent Internet: A Three-Layer Architecture for Cross-Platform AI Agent Interoperability
> **类型**：System/Position Paper (6 pages + references)
> **作者**：Wayne (云中布衣), Jarvis AI*
> **目标会议**：CCMAS 2026 (CCF)

---

## 摘要 (Abstract — 300 words)

The rapid proliferation of AI agents across major platforms—Anthropic Claude, OpenAI GPTs, Google Gemini, Microsoft Copilot, Meta Llama—has created a critical challenge: agents from different platforms cannot natively discover, communicate, or collaborate. This "closed world" problem mirrors the early Internet's hosts-file era (pre-1983) and manifests as an N² bilateral integration problem at scale.

Drawing on empirical analysis of 119,757 real-world service endpoints and 62,739 MCP server deployments (Verisign 2026), this paper proposes **Agent Internet** as a unifying concept and presents a **three-layer architecture**:

1. **Business Layer** — Commercial relationships (ACP, UCP, NANDA Index, China AIP)
2. **Protocol Layer** — Message exchange (MCP, A2A, AIN)
3. **Network Layer** — Identity and discovery (ANS, DNS-AID, .Agent, AGNTCY, GB/Z 185-2026)

We show that the Internet's 40-year infrastructure (DNS, BGP, TLS, HTTP) is being precisely replicated in the agent layer, and that a single DNS UDP response (1232 bytes) can carry the full 90th-percentile agent metadata (940 bytes). This implies that the "physical layer" of agent interoperability is **already solved** by the existing Internet.

We then provide a comparative analysis of China's GB/Z 185-2026 series (7 national standards released on 2026-06-09) and the Agent Interconnection Protocol (AIP), contrasting them with international standards. We identify three key tensions: (1) government-led vs. consortium-led governance, (2) mandatory identity vs. self-sovereign identity, and (3) compliance-first vs. innovation-first.

We conclude with three-dimensional recommendations for industry, policy, and technology stakeholders, emphasizing that 2025-2028 represents a critical standardization window for the Agent Internet.

**Keywords**: AI agents, multi-agent systems, interoperability, DNS, Agent Internet, MCP, A2A, BGP, network architecture

---

## 1. Introduction

### 1.1 Background
- AI 智能体 2025-2026 爆发增长
- 主要平台：Anthropic、OpenAI、Google、Microsoft、Meta
- 智能体 = 自主决策 + 工具调用 + 多步推理

### 1.2 The Closed World Problem
- 5 平台 × N 智能体 = 跨平台无法直接协作
- 真实案例：Anthropic 内部 Claude 智能体与 Google Gemini 智能体不互通
- 类比早期互联网"hosts 文件时代"

### 1.3 Research Questions
- RQ1: 智能体互联互通应如何分层？
- RQ2: 现有互联网基础设施能否支撑智能体互联网？
- RQ3: 中国国家标准与国际标准应如何协同？

### 1.4 Contributions
1. 提出 "Agent Internet" 概念
2. 三层架构（业务/协议/网络）
3. 基于 119,757 端点的实证分析
4. 中国 vs 国际标准对比
5. 政策建议

---

## 2. The Closed World Problem: A Network Perspective

### 2.1 N² Bilateral Integration Problem
- 数学分析：5 平台 = 25 对接，100 平台 = 10,000 对接
- 真实成本：4-6 周/对接工程

### 2.2 Historical Parallel: Pre-1983 Internet
- ARPANET：每个网络独立维护 hosts 表
- 1983 年 DNS 出现，3 年内标准化
- 类比：智能体互联网正处于"hosts 时代"

### 2.3 Three Hidden Costs
- 创新速度（封闭生态壁垒）
- 跨组织协作（中心化撮合）
- 监管可见性（黑盒化）

---

## 3. The Agent Internet: A Three-Layer Architecture

### 3.1 Concept Definition
Agent Internet = 由异构 AI 智能体组成的、可全球互联互通的、基于现有互联网基础设施的"智能体网络"。

### 3.2 Layer 1: Business Layer
| 协议 | 主体 | 关键特性 |
|------|------|---------|
| ACP | IBM + LF | 商务交易（定价/支付/协商）|
| UCP | Google | Google Shopping 集成 |
| NANDA | MIT | AgentFacts 验证 |
| **AIP** | **中国** | **国家协议（GB/Z 185）** |

### 3.3 Layer 2: Protocol Layer
| 协议 | 类比 | 成熟度 |
|------|------|--------|
| MCP | ODBC | 9700 万下载 |
| A2A | SMTP | 150+ 组织 |
| AIN | BGP/IP | 草案阶段 |

### 3.4 Layer 3: Network Layer
| 方案 | 关键创新 |
|------|---------|
| ANS | DNS + DANE |
| DNS-AID | SVCB + DANE（纯 DNS）|
| .Agent | 顶级域 |
| AGNTCY | 中心化目录 |
| **GB/Z 185.2** | **中国国家身份码** |

### 3.5 Cross-Layer Dependencies
（图表：栈式依赖图）

---

## 4. Empirical Analysis: Agent Metadata Fits in DNS

### 4.1 Verisign 2026 Data
- 119,757 unique API endpoints
- 62,739 MCP servers, 13,607 with tool declarations

### 4.2 Metadata Size Distribution
- 端点 URL：median 70B, P90 108B
- MCP 工具：median 3/server, P90 19/server
- 能力命名空间：median 49 chars, P90 323 chars
- **完整 P90 元数据：940 字节**

### 4.3 DNS UDP 1232-byte Budget
```
940 字节 + DNS header (20) + query name (20) = 980 字节
980 / 1232 = 79.5% 利用率 ✅
```

### 4.4 Three Insights
1. 物理层已被互联网解决
2. 元数据规模天然适配 DNS
3. 不应发明新协议，应复用 40 年基础设施

---

## 5. China vs International Standards: A Comparative Analysis

### 5.1 GB/Z 185-2026 (7 Standards)
（表格：7 项标准详细对比）

### 5.2 AIP Protocol
- 2026-05-08 首次写入国家级文件
- 强制身份编码 + 国家注册平台
- 实名 + 合规审计

### 5.3 Three Key Tensions
1. **治理模式**：政府 vs 基金会
2. **身份管理**：强制 vs 自选
3. **创新速度**：集中 vs 多元

### 5.4 Synergy Path
- 2026-2028 双轨发展
- 2029+ 国际互联互通
- AIP + A2A/MCP 桥接层

---

## 6. Three-Dimensional Recommendations

### 6.1 Industry
（短期/中期/长期）

### 6.2 Policy
（最紧迫：.agent 顶级域 / 强制标准 / 身份认证）

### 6.3 Technology
（IETF AIN 标准化 / 开源参考实现 / 互操作认证）

---

## 7. Conclusion

- Agent Internet 是 40 年互联网基础设施的"插入层"
- 2025-2028 标准化窗口
- 监管 + 学术 + 产业协同
- 中国 vs 国际的协同进化

---

## 附录 A：术语表

| 术语 | 全称 | 中文 |
|------|------|------|
| MCP | Model Context Protocol | 模型上下文协议 |
| A2A | Agent2Agent | 智能体间协议 |
| AIN | Agentic Intent Network | 智能体意图网络 |
| ANS | Agent Name Service | 智能体命名服务 |
| DNS-AID | DNS for AI Discovery | 智能体发现 DNS |
| ACP | Agent Commerce Protocol | 智能体商务协议 |
| UCP | Universal Commerce Protocol | 通用商务协议 |
| AIP | Agent Interconnection Protocol | 智能体互联协议（中国）|
| GB/Z | 标准化指导性技术文件 | 国标指导性技术文件 |
| IETF | Internet Engineering Task Force | 互联网工程任务组 |
| NANDA | Networked Agents and Decentralized AI | 网络化智能体与去中心化 AI |

---

*🤖 Jarvis AI · 第103天 · 2026-06-18 · Paper 1 v0.1*
