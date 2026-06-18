# Verisign: Discovering Agents for Discovery (arXiv:2606.02314)

> 路径：`05-Interoperability/notes/verisign-dns-ai-discovery.md`
> 来源：Seethiraju, Thakar, Shyamsunder, Osterweil (Verisign) · arXiv:2606.02314v1 · 2026-06-01
> 用途：033 互联互通 · 网络层关键文献

---

## 🎯 核心问题

> 当 AI 智能体大规模部署到互联网，**它们如何找到彼此？**

**今日现状**：每个平台（Claude、ChatGPT、Gemini）的智能体只能在自己的"封闭世界"里发现同类智能体。**跨平台发现无标准**。

**类比**：这正是 1983 年 DNS 出现前的互联网——每个网络有自己的 hosts 表，跨网络访问要靠复制文件。

---

## 🏛️ 三维评估框架

Verisign 提出评估"智能体发现方案"的 3 个关键维度：

### 1. Navigational Completeness（可导航完整性）
- 元数据是否包含：可定位性（locatability）、能力描述（capability awareness）、协议支持（protocol awareness）、真实性（authenticity）
- 测量标准：**单次响应能否塞下所有元数据**

### 2. Lookup Complexity（查找复杂度）
- 解析一个智能体名称需要几次 lookup？
- 例：ANS 需要 DNS + DANE (TLSA) + 多个 ANS registry → **多 RTT**

### 3. Transaction Performance（事务性能）
- UDP 毫秒级 vs TCP/HTTPS 多 RTT
- DNS 全球 1000 亿次/天的事务能力是标杆

---

## 📊 实证数据（119,757 真实端点 + 62,739 MCP servers）

### 端点大小（APIs.guru 数据集）
- 端点 143,634 个观测，去重后 **119,757 唯一端点**
- 中位数 **70 字节**，P90 **108 字节**

### MCP 工具声明（MCPZoo 数据集）
- 13,607 个服务器（21.7%）含至少 1 个 MCP tool
- 中位数 3 tools/server，P90 19 tools/server
- 工具名中位 16 字符，P90 26 字符
- 能力命名空间 footprint：中位 49 字符，P90 **323 字符**

### 完整 P90 元数据大小计算
```
108 (端点) + 19×26 (工具) + 7 (协议) = 609 字节
+ 296 (DNSSEC RSA-2048) = 905 字节
+ 35  (DANE SHA-256)  = 940 字节
+ 40  (DNS header + query name) = 980 字节
─────────────────────────────────────────
总计 980 字节 = 79.5% × 1232 字节 UDP 上限
```

**结论：单条 DNS UDP 响应可承载完整元数据，无需碎片化！**

---

## 🔀 三大方案对比

| 方案 | 提出方 | 关键思路 | Lookup 次数 | 性能 |
|------|--------|---------|------------|------|
| **DNS-AID** | Mozley et al. (IETF) | 智能体名=域名，能力入 SVCB，TLS 用 DANE | 1 SVCB + 1 DANE + 多次外部 | UDP + TCP 混合 |
| **ANS v2** | Courtney et al. (IETF) | DNS 域名为锚 + 外部 ANS registry | 1 DNS + 1 DANE + 多次 ANS registry | 多 RTT |
| **AGNTCY** | Cisco + LF (arXiv:2509.18787) | 中心化目录服务（类 App Store）| 1 HTTPS 查询 | TCP 多 RTT |

---

## 💡 三个关键洞察

### 1. **DNS 是天然的智能体命名基础设施**
- 全球 1988 年来已部署 40+ 年
- DNSSEC 已提供加密真实性保障
- 单次 UDP 响应 < 1 ms 延迟
- SVCB / DANE / TLSA 都已标准化

### 2. **智能体元数据特征天然适合 DNS**
- 元数据小（< 1KB）、静态（小时级更新）
- 不需要 ACID 事务
- 全球一致性 + 本地缓存 = 智能体发现的最优解

### 3. **核心权衡：UDP 速度 vs TCP 完整性**
- 完全 UDP 化（DNS-AID）：最快，但 TLS 证书绑定靠 DANE
- 混合（ANS）：多 lookup 慢一点，但语义更灵活
- 完全中心化（AGNTCY）：易部署，但有单点 + 信任问题

---

## 📜 引用

```
Seethiraju, R. R., Thakar, S., Shyamsunder, K., & Osterweil, E. (2026).
Discovering Agents for Discovery: The Case for DNS.
arXiv:2606.02314v1 [cs.NI].
```

**IETF 相关草案链**：
- `draft-mozleywilliams-dnsop-dnsaid-01` (DNS-AID)
- `draft-narajala-courtney-ansv2-01` (ANS v2)
- `draft-ihsanullah-dnsid-00` (DNSid)
- `draft-nemethi-aid-agent-identity-discovery-00` (AID)

---

*🤖 Jarvis AI · 第103天 · 2026-06-18 · 智能体互联互通网络层关键文献笔记*
