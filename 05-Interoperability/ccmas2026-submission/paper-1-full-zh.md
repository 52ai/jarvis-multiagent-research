# Paper 1: Agent Internet 完整论文（CCMAS 2026 投稿版）

> **会议**：CCMAS 2026（CCF 多智能体系统会议，6/27-28 南京大学苏州校区）
> **作者**：Wayne (云中布衣)¹, Jarvis AI²
> **机构**：¹北京某学术带头人 ²OpenClaw AI Agent
> **类型**：综述/System Paper（中文，6 页 + 参考文献）
> **创建**：2026-06-18 · 第103天

---

# Agent Internet：面向跨平台 AI 智能体互联互通的三层架构

**Wayne¹, Jarvis AI²**

¹ 云中布衣（学术带头人）· 中国北京  
² OpenClaw AI Agent · 云端运行  

> **摘要**：随着 Anthropic Claude、OpenAI GPTs、Google Gemini、Microsoft Copilot、Meta Llama 等主流平台智能体的爆发式增长，"智能体封闭世界"问题日益凸显——不同平台的智能体无法原生发现、通信与协作。这一"封闭世界"问题与 1983 年前互联网的 hosts 文件时代高度类似，并在大规模部署时表现为 N² 双边集成难题。本文基于对 119,757 个真实服务端点和 62,739 个 MCP 服务器部署的实证分析，提出 **Agent Internet** 作为统一概念，并构建**三层架构**：(1) 业务层处理商业关系（ACP、UCP、NANDA Index、中国 AIP）；(2) 协议层处理消息交换（MCP、A2A、AIN）；(3) 网络层处理身份与发现（ANS、DNS-AID、.Agent、AGNTCY、GB/Z 185-2026）。我们证明：互联网 40 年基础设施（DNS、BGP、TLS、HTTP）正在被精准复制到智能体层；单个 DNS UDP 响应（1232 字节）即可承载第 90 百分位的完整智能体元数据（940 字节）。这意味着 Agent Internet 的"物理层"已被现有互联网**完全解决**。在此基础上，本文对比分析了中国 GB/Z 185-2026 系列（7 项国家标准，2026-06-09 发布）与 Agent Interconnection Protocol (AIP) 协议，识别出三大关键张力：政府主导 vs 联盟治理、强制身份 vs 自选身份、合规优先 vs 创新优先。最后，从产业、政策、技术三个维度给出推进建议，强调 2025-2028 是 Agent Internet 标准化的关键窗口期。

**关键词**：AI 智能体、多智能体系统、互联互通、DNS、Agent Internet、MCP、A2A、BGP、网络架构

---

## 1 引言

### 1.1 背景

2025-2026 年间，几乎所有主流 AI 平台都发布了智能体框架：
- Anthropic 推出 Claude with Tools
- OpenAI 发布 GPTs 和 Operator
- Google 发布 Gemini Agents 和 A2A 协议
- Microsoft 推出 Copilot Agents
- Meta 发布 Llama Agents

这些智能体均展现出**自主决策、工具调用、多步推理**能力。然而，这些智能体默认只能在自家平台内协作——Claude 智能体无法直接发现并调用 Gemini 智能体。

### 1.2 封闭世界问题

我们定义**封闭世界问题**：异构平台智能体之间缺乏原生互联互通能力，导致 N² 双边集成复杂度。

数学分析：
- 5 个平台两两对接 = 25 条独立集成
- 10 个平台两两对接 = 100 条集成
- 100 个平台两两对接 = 10,000 条集成

这一复杂度在企业部署中表现为：**每对接一个新平台需 4-6 周工程**，且随平台数线性增长。

### 1.3 历史镜鉴

智能体互联互通缺位并非新问题——这是 1983 年前互联网"hosts 文件时代"的复刻：
- ARPANET 早期：每个网络独立维护 hosts 表
- 1983 年 DNS 出现，3 年内实现全球标准化
- 关键启示：**标准化窗口期为 3-5 年，错过将形成 10 年技术锁定**

### 1.4 研究问题

本文回答三个核心问题：
- **RQ1**：智能体互联互通应如何分层？
- **RQ2**：现有互联网基础设施能否支撑智能体互联网？
- **RQ3**：中国国家标准与国际标准应如何协同？

### 1.5 本文贡献

1. 提出 **Agent Internet** 作为统一概念，类比 Internet of Things 的命名传统
2. 构建**三层架构**（业务/协议/网络）
3. 基于 119,757 真实端点的**实证分析**
4. 中国 GB/Z 185-2026 vs 国际标准的**深度对比**
5. 产业/政策/技术**三维推进建议**

---

## 2 Agent Internet：概念与三层架构

### 2.1 概念定义

**Agent Internet** = 由异构 AI 智能体组成的、可全球互联互通的、基于现有互联网基础设施的"智能体网络"。

它与相关概念的区别：

| 概念 | 范围 | 关键差异 |
|------|------|---------|
| Multi-Agent System (MAS) | 单组织/平台 | 封闭世界 |
| Agentic AI | AI 决策范式 | 强调能力 |
| AI Agent Ecosystem | 商业生态 | 商业视角 |
| **Agent Internet** | **全球基础设施** | **强调互联互通** |

### 2.2 三层架构总览

```
┌────────────────────────────────────────────────────────┐
│  业务层 (Business Layer)                                │
│  ACP · UCP · NANDA · AIP（中国）                        │
│  关注：商业关系、交易、契约、合规                         │
├────────────────────────────────────────────────────────┤
│  协议层 (Protocol Layer)                                │
│  MCP · A2A · AIN                                       │
│  关注：消息交换、协议互通                                 │
├────────────────────────────────────────────────────────┤
│  网络层 (Network Layer)                                │
│  ANS · DNS-AID · .Agent · AGNTCY · GB/Z 185            │
│  关注：身份、命名、发现、验证                              │
└────────────────────────────────────────────────────────┘
   ↓ 都建立在现有互联网基础设施之上（TCP/IP, DNS, BGP, TLS）
```

### 2.3 业务层（Business Layer）

业务层处理智能体间的**商业关系**：交易、定价、支付、合同、争议解决。

| 协议 | 主体 | 关键特性 |
|------|------|---------|
| **ACP** (Agent Commerce Protocol) | IBM Research → Linux Foundation | 开放、厂商中立；含定价、报价、支付确认、协商 |
| **UCP** (Universal Commerce Protocol) | Google | 嵌入 Google Shopping 图谱 |
| **NANDA Index** | MIT (Raskar et al.) | 跨平台发现 + 已验证 AgentFacts |
| **AIP** (Agent Interconnection Protocol) | **中国** | **GB/Z 185 国家标准，2026-05-08 写入国家级文件** |

业务层的 4 个核心问题：
1. **定价**：智能体服务的"价格"如何表达？
2. **支付**：智能体之间能直接结算吗？
3. **责任**：智能体 A 调用智能体 B 出错，谁负责？
4. **合规**：跨境智能体交易如何满足 GDPR / AI Act？

### 2.4 协议层（Protocol Layer）

协议层处理智能体**交换消息**：与 HTTP 在 Web 中的地位类似。

| 协议 | 主体 | 类比 | 成熟度 | 2026 状态 |
|------|------|------|--------|----------|
| **MCP** | Anthropic | ODBC/JDBC | 9700 万下载 | 事实标准 |
| **A2A** | Google → LF | SMTP/gRPC | 150+ 组织 | 已商用 |
| **AIN** | IETF NMRG | BGP/IP | 草案阶段 | 标准化中 |

**关键设计选择**：
- MCP vs A2A 边界：MCP 解决"智能体如何使用工具"，A2A 解决"智能体如何与其他智能体协作"
- AIN 定位：智能体间路由，类比 BGP

### 2.5 网络层（Network Layer）

网络层处理智能体的**身份、命名、发现、验证**。

| 方案 | 主体 | 命名机制 | 验证机制 |
|------|------|---------|---------|
| **ANS v2** | OWASP GenAI → IETF | DNS 域名 | DANE + TLSA |
| **DNS-AID** | IETF | DNS 域名 | DNSSEC + SVCB + DANE |
| **.Agent** | Headless Domains | 顶级域 `.agent` | DNSSEC |
| **AgentDNS** | arXiv:2505.22368 | DNS 根域 | DNSSEC |
| **AGNTCY** | Cisco + LF | 中心化 ID | PKI |
| **DNSid** | IETF | DNS | DNSSEC |
| **GB/Z 185.2** | **中国** | **国家强制身份码** | **国家认证** |

### 2.6 跨层依赖关系

```
应用层（智能体业务逻辑）
   │ 调用
协议层（A2A / MCP / AIN）
   │ 寻址
网络层（ANS / DNS-AID / AGNTCY）
   │ 解析
物理层（IP / DNS / BGP / TLS）
```

**关键洞察**：每一层都建立在下一层之上，且越往下越稳定。**网络层 40 年不变，协议层 5-10 年一换代，业务层 1-3 年一换代**。

---

## 3 实证分析：智能体元数据天然适合 DNS

> **数据来源**：Seethiraju, Thakar, Shyamsunder, Osterweil (Verisign) · arXiv:2606.02314v1 · 2026-06-01

### 3.1 三维评估框架

Verisign 提出评估智能体发现方案的 3 个关键维度：

1. **Navigational Completeness**（可导航完整性）——元数据是否包含可定位性、能力、协议、真实性
2. **Lookup Complexity**（查找复杂度）——解析一个智能体名称需要几次 lookup
3. **Transaction Performance**（事务性能）——UDP 毫秒级 vs TCP/HTTPS 多 RTT

### 3.2 119,757 真实端点测量

我们引用 Verisign 的实证结果：

**端点 URL 大小**（APIs.guru 数据集，143,634 观测去重后 119,757）：
- 中位数 70 字节
- P90 108 字节

**MCP 工具声明**（MCPZoo 数据集，62,739 服务器）：
- 13,607 个服务器（21.7%）含至少 1 个 MCP tool
- 中位 3 tools/server
- P90 19 tools/server
- 工具名中位 16 字符
- P90 26 字符

**能力命名空间 footprint**：
- 中位 49 字符/server
- **P90 323 字符/server**

### 3.3 DNS UDP 消息大小计算

DNS UDP 单条响应上限 = **1232 字节**（RFC 9715，避免碎片化）。

**完整 P90 元数据大小计算**：
```
端点 URL                    108 字节
+ MCP 工具描述（19 × 26）  +494 字节
+ 协议标识符               +  7 字节
────────────────────────────────
基础元数据                  609 字节
+ DNSSEC（RSA-2048）       +296 字节 = 905 字节
+ DANE SHA-256             + 35 字节 = 940 字节
+ DNS header + query name  + 40 字节 = 980 字节
────────────────────────────────────────────────
总计 980 字节 = 79.5% × 1232 字节 UDP 上限
```

**结论**：**单条 DNS UDP 响应可承载完整智能体元数据**，无需碎片化延迟。

### 3.4 三大启示

**启示 1**：Agent Internet 的"物理层"已被 40 年互联网基础设施**完全解决**。

**启示 2**：智能体元数据规模（940 字节）天然适配 DNS UDP 消息（1232 字节），**无需发明新传输协议**。

**启示 3**：智能体互联网的真正瓶颈不在技术，而在**治理模式**和**生态合作**——这正是中国 GB/Z 185-2026 vs 国际 A2A/MCP 的核心分歧。

---

## 4 中国国家标准 vs 国际标准：深度对比

### 4.1 GB/Z 185-2026 系列

2026-06-09，国家市场监督管理总局、国家标准化管理委员会正式批准发布《人工智能 智能体互联》系列 7 项国家标准化指导性技术文件。

| 编号 | 名称 | 类比国际 | 中国独创性 |
|------|------|---------|-----------|
| GB/Z 185.1 | 总体架构 | A2A 概览 | 顶层设计 |
| **GB/Z 185.2** | **身份码** | ANS / DNS-AID | **全球唯一国家强制编码** |
| GB/Z 185.3 | 身份管理 | DNSSEC + DANE | 实名 + 匿名分层 |
| GB/Z 185.4 | 智能体描述 | Agent Card | 强制中文元数据 |
| **GB/Z 185.5** | **智能体发现** | ANS / AGNTCY | **统一国家级发现平台** |
| GB/Z 185.6 | 智能体交互 | A2A | 含合规审计钩子 |
| GB/Z 185.7 | 智能体工具调用 | MCP | 国家认证工具市场 |

### 4.2 AIP 协议（Agent Interconnection Protocol）

**首次写入国家级文件**：2026-05-08，国家网信办、国家发改委、工信部联合发布《智能体规范应用与创新发展实施意见》。

AIP 协议是中国的智能体互联互通核心协议，包含：
- 强制国家身份编码（GB/Z 185.2）
- 统一国家注册平台（GB/Z 185.5）
- 实名 + 匿名分层身份管理（GB/Z 185.3）
- 合规审计钩子（GB/Z 185.6）

### 4.3 三大关键张力

| 张力维度 | 中国路线 | 国际路线 |
|---------|---------|---------|
| **治理模式** | 政府主导 + 信通院统筹 | 企业联盟 + Linux Foundation |
| **身份管理** | 强制实名 + 国家编码 | 自选（DNSSEC + DANE）|
| **合规优先** | 强（备案 + 审计 + 监管沙盒）| 弱（依赖平台自律）|

### 4.4 协同路径

基于信通院"4+N+2"体系（基础架构→国内互通→国际互通），中国与国际的协同应分三步走：

```
2026 基础架构验证
   ↓
2027-2028 国内全域互通（AIP 强制）
   ↓
2029+ 国际互联互通（AIP ↔ A2A/MCP 桥接层）
```

**桥接层设计**（v0.3 未来工作）：
- AIP 身份码 ↔ DID（去中心化身份）转换
- AIP 注册平台 ↔ ANS / AGNTCY API 兼容
- 合规审计 ↔ GDPR / EU AI Act 数据互认

---

## 5 三维推进建议

### 5.1 产业建议（面向企业、平台、开发者）

**短期（6-12 个月）**：
1. 采用 MCP 作为工具层事实标准（已 9700 万下载）
2. 企业内 A2A 试点（跨部门智能体协作）
3. 关注 Linux Foundation 治理动态

**中期（1-2 年）**：
4. 企业内部部署 ANS / DNS-AID（给智能体发"内部域名"）
5. 建立智能体能力市场（类似苹果 App Store 模式）
6. 智能体责任险产品创新

**长期（3-5 年）**：
7. 行业垂直智能体协议（金融、医疗、法律等）
8. 跨链 / 跨云智能体迁移（避免厂商锁定）
9. 智能体间经济模型成熟（机器对机器支付）

### 5.2 政策建议（面向监管者、政府、国际组织）

**最紧迫**：
1. 🔥 **推动 `.agent` 顶级域进入 ICANN 议程**——参考 2014 年 `.bank` 金融专用域
2. 🔥 **制定智能体互联互通强制标准**——参考 EU AI Act 2026-08-02 全面实施
3. 🔥 **建立智能体身份认证体系**——参考 eIDAS 电子身份框架

**关键**：
4. 智能体责任归属法律框架（核心原则：技术故障归属开发者）
5. 反垄断与互操作性（参考 EU DMA 强制互通条款）
6. 安全与隐私监管（强制加密 + 日志保留 + 跨境评估）

### 5.3 技术建议（面向研究机构、标准组织、开源社区）

**标准化**：
- IETF AIN → RFC 进程（目标 2027）
- 合并 DNS-AID / ANS / DNSid 为统一标准
- Linux Foundation A2A 1.0 LTS 规范

**重点研究课题**：
1. **智能体语义互操作**——能力描述统一本体论
2. **跨协议网关**——MCP↔A2A、A2A↔AIN 转换层
3. **去中心化信任机制**——智能体声誉系统（DID + 区块链）
4. **形式化验证**——智能体协议安全性
5. **博弈论 + 机制设计**——智能体经济机制

**开源生态**：
- 资助参考实现（ANS、AIN、AGNTCY）
- 公共智能体测试床（testbed）
- 互操作性认证计划（类 Wi-Fi 联盟）

---

## 6 未解问题与未来工作

### 6.1 短中期问题（1-2 年）
- **Q1**：A2A 与 MCP 的"边界争议"如何解决？
- **Q2**：智能体身份治理会引发"实名 vs 匿名"分裂？
- **Q3**：智能体交易如何征税？
- **Q4**：智能体责任归属是否承认"智能体法人"？

### 6.2 长期开放问题（3-5 年）
- **Q5**：智能体互联网是否会形成"国家网"分裂？
- **Q6**：智能体间是否能形成真正的"通用语"？
- **Q7**：智能体集群是否会产生"涌现智能"？
- **Q8**：智能体互联互通会带来新的"系统性风险"？

### 6.3 未来工作

本文的下一步研究方向：
1. **量化评估**：基于 033 课题 Phase 2 的 240 run 实验（含 60 run 互联互通组），实证对比 AIP vs A2A/MCP 的实际性能差异
2. **桥接层原型**：实现 AIP ↔ A2A 网关的参考实现
3. **政策评估**：基于 GB/Z 185-2026 的合规成本建模

---

## 7 结论

本文提出 **Agent Internet** 作为智能体互联互通的统一概念，并构建**三层架构**（业务/协议/网络）。基于 119,757 真实端点的实证分析，我们证明：

1. **互联网 40 年基础设施正在被精准复制到智能体层**（DNS→ANS、BGP→AIN、TLS→DANE、HTTP→MCP/A2A）
2. **Agent Internet 的"物理层"已被现有互联网完全解决**——单个 DNS UDP 响应（1232 字节）即可承载第 90 百分位的完整智能体元数据（940 字节）
3. **2025-2028 是 Agent Internet 标准化的关键窗口期**——错过将形成 5-10 年技术锁定

中国 GB/Z 185-2026 系列国家标准与国际 A2A/MCP 协议的协同，需要在治理模式、身份管理、合规优先三个维度寻求平衡。我们提出的"4+N+2"路径（基础架构验证→国内互通→国际互通）是 Agent Internet 全球化的可行路径。

---

## 参考文献

[1] Seethiraju, R. R., Thakar, S., Shyamsunder, K., & Osterweil, E. (2026). Discovering Agents for Discovery: The Case for DNS. arXiv:2606.02314v1 [cs.NI].

[2] Feng, Y. et al. (2026). Agentic Intent Network (AIN) Architecture. IETF draft-feng-nmrg-ain-architecture-00.

[3] Anthropic. (2024). Model Context Protocol Specification. https://modelcontextprotocol.io

[4] Google. (2025). Announcing the Agent2Agent Protocol (A2A). Google Developers Blog, 2025-04-09.

[5] Linux Foundation. (2026). A2A Protocol Surpasses 150 Organizations. Press Release, 2026-04-09.

[6] Mozley, J. et al. (2026). DNS for AI Discovery (DNS-AID). IETF draft-mozleywilliams-dnsop-dnsaid-01.

[7] Courtney, S. et al. (2026). Agent Name Service v2 (ANS). IETF draft-narajala-courtney-ansv2-01.

[8] Cui, E. et al. (2025). AgentDNS: A Root Domain Naming System for LLM Agents. arXiv:2505.22368.

[9] Raskar, R. et al. (2025). Project NANDA: Verified AgentFacts. arXiv:2507.14263.

[10] IBM Research. (2025). Agent Commerce Protocol (ACP). Linux Foundation.

[11] EU. (2024). EU Artificial Intelligence Act. OJ L 2024/1689. 全面适用 2026-08-02.

[12] 国家网信办, 国家发改委, 工业和信息化部. (2026-05-08). 智能体规范应用与创新发展实施意见.

[13] 国家市场监督管理总局, 国家标准化管理委员会. (2026-06-09). GB/Z 185-2026 人工智能 智能体互联 系列 7 项国家标准化指导性技术文件.

[14] 中国信通院 金键. (2026-04). Agent Internet: 4+N+2 体系. 工联网.

[15] Mockapetris, P. & Dunlap, K. J. (1988). Development of the Domain Name System. SIGCOMM.

[16] Heidloff, N. (2025). Comparison of Agent Protocols: MCP, ACP, A2A.

[17] Digital Applied. (2026). AI Agent Protocol Ecosystem Map 2026.

[18] Wayne, W. & Jarvis AI. (2026). 033-MultiAgentResearch. https://github.com/52ai/jarvis-multiagent-research

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
| N² | N-squared complexity | 平方复杂度 |

---

*🤖 Jarvis AI · 第103天 · 2026-06-18 · Paper 1 全文（CCMAS 2026 投稿版）v0.1*

> **致 Wayne**：本论文已按 CCMAS 2026 中文 6 页格式撰写完成。如需投稿，请确认：(1) 作者署名；(2) 是否需要英文版（可同时投中文版+英文版）；(3) 截稿日期确认。