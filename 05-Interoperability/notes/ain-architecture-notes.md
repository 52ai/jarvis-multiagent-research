# IETF: Agentic Intent Network (AIN) 架构笔记

> 路径：`05-Interoperability/notes/ain-architecture-notes.md`
> 来源：`draft-feng-nmrg-ain-architecture-00` · IETF NMRG · Feng et al. · 2026-04-16
> 用途：033 互联互通 · 协议层 + 网络层交叉文献

---

## 🎯 核心洞察

> **AIN = "智能体的 BGP/IP"**

BGP 解开了人类互联网的"N² 双边集成问题"。AIN 试图为智能体做同样的事：
**让任意智能体能动态发现并调用任意其他智能体的能力，跨异构框架和组织边界。**

---

## 🏛️ 三层架构

### 1. 应用实体层（Application Entities）
- **Originator**（发起者）— 发出 Intent
- **Dispatcher**（调度者）— 分解和协调复合任务
- **Handler**（执行者）— 执行原子 Intent

### 2. 网络子层（Networking Substrate）
- **Intent Routing Data Plane** — 无状态 hop-by-hop 转发 Intent 数据报
- **Intent Routing Control Plane** — 处理 CAP（能力广告），维护 CRT（能力路由表）
- **Semantic Substrate** — 提供 IC-OID 共享命名 + 能力匹配语义

### 3. 底层传输（Underlay / Transport Fabric）
- 架构上独立于 AIN
- 传统 IP 传输 + 服务网格
- 提供端到端可达性

---

## 🗺️ 与 BGP/IP 的精确映射

| AIN 概念 | 互联网类比 | 说明 |
|---------|----------|------|
| **Intent Datagram** | IP Datagram | 通用"窄腰"协议数据单元 |
| **Intent Router** | IP Router | 智能体网络的转发节点 |
| **Capability Routing Table (CRT)** | IP Forwarding Table | 能力 → 下一跳 |
| **Capability Advertisements (CAP)** | BGP Route Advertisements | 能力发布/传播 |
| **Agent Domain** | Autonomous System (AS) | 单个管理/策略边界下的实体集合 |
| **IC-OID** | IP address | 智能体能力的全局唯一标识符 |

**关键洞察**：AIN 不是要替换 IP，而是 **"智能体层的协议栈"**——和 TCP 在 IP 之上的关系一样。

---

## 🛡️ 四大治理挑战（论文 §5）

### 1. 命名空间治理
- IC-OID 根命名空间需全球统一治理
- 否则会出现"语义命名空间滥用"——恶意注册劫持合法请求的 capability class

### 2. 策略/机制分离
- 路由机制必须**通用且稳定**
- 策略和能力匹配语义应**分层在转发核心之上**
- 避免每个新业务需求都要改协议

### 3. 信任与安全策略
- "能力声明"必须可验证
- 防御：能力声明欺骗（capability-claim spoofing）
- 防御：路由状态投毒（routing-state poisoning）

### 4. 经济治理
- Phase 3 阶段需要跨域经济结算 + 激励对齐
- 不同 Agent Domain 之间的"通行费"如何定价？

---

## 💡 对 033 课题的启示

### 1. 互联网基础设施的"四十年模式"正在复制到智能体
- DNS（命名）→ ANS / DNS-AID / .Agent
- BGP（路由）→ AIN 的 CAP + CRT
- TLS（安全）→ DANE / 智能体身份认证
- HTTP（业务）→ MCP / A2A / ACP

### 2. 智能体"互联网"有 3 个独有的设计点
- **能力描述**（capability）比 IP 更复杂——不是数字地址，是语义标签
- **可信计算**（trusted execution）比纯网络传输更关键——智能体可能执行副作用操作
- **经济结算**（settlement）需要内嵌——智能体间是合作+交易混合

### 3. 互联网治理模式值得借鉴
- 1983 年 DNS 早期：根区文件由 IANA 一人管理 → 1998 年 ICANN 成立
- 2026 年智能体命名：可能要走类似的"开放标准化 → 中立基金会"路径

---

## 📜 引用

```
Feng, Y. et al. (2026). Agentic Intent Network (AIN) Architecture.
IETF Internet-Draft, draft-feng-nmrg-ain-architecture-00.
Work in Progress, expires 2026-10-19.
```

**关联草案**：
- `draft-mozleywilliams-dnsop-dnsaid-01` (网络层 DNS-AID)
- `draft-narajala-courtney-ansv2-01` (网络层 ANS v2)

---

*🤖 Jarvis AI · 第103天 · 2026-06-18 · 智能体互联互通协议层关键文献笔记*
