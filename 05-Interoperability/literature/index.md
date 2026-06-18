# 智能体互联互通专题文献索引

> 路径：`05-Interoperability/literature/index.md`
> 创建：2026-06-18 · Jarvis AI · 第103天
> 范围：业务层 / 协议层 / 网络层

---

## 📚 业务层（Business Layer）

| # | 名称 | 主体 | 关键内容 | 链接 |
|---|------|------|---------|------|
| 1 | **Agent Commerce Protocol (ACP)** | IBM Research + Linux Foundation | 开放、厂商中立的智能体间商务交易（定价、报价、支付、协商）| [heidloff.net](https://heidloff.net/article/mcp-acp-a2a-agent-protocols/) |
| 2 | **Universal Commerce Protocol (UCP)** | Google | 嵌入 Google Shopping 的智能体商务协议 | [digitalapplied.com](https://www.digitalapplied.com/blog/ai-agent-protocol-ecosystem-map-2026-mcp-a2a-acp-ucp) |
| 3 | **Project NANDA Index + AgentFacts** | MIT (Raskar et al., arXiv:2507.14263) | 跨平台智能体发现 + 已验证的智能体事实 | [arXiv:2507.14263](https://arxiv.org/abs/2507.14263) |

---

## 📡 协议层（Protocol Layer）

| # | 名称 | 主体 | 关键内容 | 链接 |
|---|------|------|---------|------|
| 1 | **Model Context Protocol (MCP)** | Anthropic（开源）| 智能体↔工具/数据 标准接口（JSON-RPC）| [digitalapplied.com](https://www.digitalapplied.com/blog/ai-agent-protocol-ecosystem-map-2026-mcp-a2a-acp-ucp) |
| 2 | **Agent2Agent (A2A)** | Google + Linux Foundation | 跨厂商智能体发现 + 任务委派（Agent Card）| [github.com/a2aproject/A2A](https://github.com/a2aproject/A2A) |
| 3 | **A2A v1 (2026)** | Linux Foundation | 已被 150+ 组织采用，落地 3 大云 | [linuxfoundation.org](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year) |
| 4 | **Agentic Intent Network (AIN)** | IETF NMRG (Feng et al.) | 智能体间路由架构（类比 BGP/IP）| [draft-feng-nmrg-ain-architecture](https://datatracker.ietf.org/doc/draft-feng-nmrg-ain-architecture/) |

---

## 🌐 网络层（Network Layer）

| # | 名称 | 主体 | 关键内容 | 链接 |
|---|------|------|---------|------|
| 1 | **Agent Name Service (ANS)** | OWASP GenAI + Verisign | 智能体命名 + 身份 + 验证（基于 DNS）| [genai.owasp.org](https://genai.owasp.org/resource/agent-name-service-ans-for-secure-al-agent-discovery-v1-0/) |
| 2 | **DNS-AID** | IETF (Mozley et al., 2026) | DNS for AI Discovery（DNSSEC + SVCB + DANE）| [draft-mozleywilliams-dnsop-dnsaid-01](https://datatracker.ietf.org/doc/draft-mozleywilliams-dnsop-dnsaid/) |
| 3 | **.Agent Headless Domains** | Headless Domains | 智能体专用顶级域（.agent）| [headlessdomains.com/agent](https://headlessdomains.com/agent) |
| 4 | **AgentDNS** | Cui et al. (arXiv:2505.22368) | 根域命名系统 for LLM Agents | [arXiv:2505.22368](https://arxiv.org/abs/2505.22368) |
| 5 | **AGNTCY Agent Directory** | Cisco + Linux Foundation (arXiv:2509.18787) | 中心化智能体目录服务 | [arXiv:2509.18787](https://arxiv.org/abs/2509.18787) |
| 6 | **DNSid** | IETF (Ihsanullah, 2026) | DNS 锚定的持久智能体身份 | [draft-ihsanullah-dnsid-00](https://datatracker.ietf.org/doc/draft-ihsanullah-dnsid/00/) |
| 7 | **Discovering Agents for Discovery** | Verisign (Seethiraju et al., arXiv:2606.02314) | 用 DNS 评估智能体发现：3 维框架 | [arXiv:2606.02314](https://arxiv.org/html/2606.02314v1) |

---

## 🔍 关键洞察（来自 119,757 真实端点测量）

Verisign 2026-06 实证研究：
- **可导航性**（navigational completeness）= 元数据大小可塞进单条 DNS UDP 消息
- **查找复杂度** = 多次 lookup（SVCB + DANE + ANS registry）vs 单次
- **事务性能** = UDP 毫秒级 vs TCP/HTTPS 多 RTT

**结论**：P90 智能体元数据 **940 字节**，单次 UDP 响应可达 1232 字节，**理论无碎片化**。
DNSSEC（ECDSA P-256）增加 104 字节，RSA-2048 增加 296 字节——**已为商业部署就绪**。

---

## 🧠 政策与监管来源

| # | 文件 | 关键点 | 时间 |
|---|------|--------|------|
| 1 | **EU AI Act 全面实施** | 2026-08-02 全面适用（含 Article 53-55 高风险 AI 治理）| 2026 |
| 2 | **EU AI Act Article 57** | 各成员国 2026-08-02 前建 AI 监管沙盒 | 2026 |
| 3 | **The 2026 EU AI Act and AI-Generated Code** | 8 月 2 日激活高风险 AI 合规框架（Articles 8-15）| 2026-04 |

---

## 🔗 三层关系图

```
┌─────────────────────────────────────────────────────┐
│  业务层 (Business Layer)                             │
│  ACP (IBM/Linux) · UCP (Google) · NANDA Index       │
│  → 智能体间交易 / 商业 / 法律契约                     │
├─────────────────────────────────────────────────────┤
│  协议层 (Protocol Layer)                            │
│  MCP (Anthropic) · A2A (Google) · AIN (IETF)         │
│  → 智能体↔工具 / 智能体↔智能体 / 智能体↔路由         │
├─────────────────────────────────────────────────────┤
│  网络层 (Network Layer)                             │
│  ANS · DNS-AID · .Agent · AgentDNS · AGNTCY        │
│  → 智能体身份 / 命名 / 发现 / 验证                  │
└─────────────────────────────────────────────────────┘
   ↓ 都建立在现有互联网基础设施之上 (TCP/IP, DNS, BGP, TLS)
```

---

*🤖 Jarvis AI · 第103天 · 2026-06-18 · 智能体互联互通文献索引 v0.1*
