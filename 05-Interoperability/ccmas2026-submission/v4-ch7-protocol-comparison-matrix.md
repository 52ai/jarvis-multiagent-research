# 第 2 件：4 协议主对比矩阵（v4.0 §7 内容）

> **路径**：`05-Interoperability/ccmas2026-submission/v4-ch7-protocol-comparison-matrix.md`
> **日期**：2026-06-18 20:21
> **对应 v4.0 章节**：§7 协议对比矩阵
> **核心**：Table 7 - 借鉴 arXiv:2505.02279 主对比表范式

---

# 主流发现协议主对比矩阵

> 4 大协议 × 8 维度严格对比
> 借鉴 Yang et al. 2025 (arXiv:2505.02279) Table 7 范式

---

## 1 Table 7: 主对比矩阵（核心表）

> 维度：架构、发现机制、身份认证、消息格式、目标范围、优势、限制、典型场景

| 维度 | **DNS-AID** | **ANS-v2** | **AGNTCY** | **AIN** |
|------|------------|-----------|-----------|---------|
| **架构** | DNS + SVCB | DNS + Registry | 中心化目录 | 多跳路由 |
| **发现机制** | SVCB + DANE 查询 | ANS API 调用 | 中心目录查询 | 路由洪泛 |
| **身份认证** | DNSSEC | TLSA | JWT | 链上签名 |
| **消息格式** | DNS TXT/SVCB | JSON+TLS | JSON+TLS | 路由协议 |
| **目标范围** | 全球 | 域内 | 平台 | 跨域 |
| **优势** | 极快、零信任、可扩展 | 灵活、丰富元数据 | 易部署、低门槛 | 跨域、动态 |
| **限制** | 静态元数据 | 需注册 | 单点故障 | 复杂度高、延迟高 |
| **典型场景** | 高频发现 | 中频发现 | 平台内 | 跨域协作 |
| **P50 延迟** | 3ms | 117ms | 78ms | 245ms |
| **标准化** | IETF 草案 | IETF 草案 | LF | IETF 草案 |
| **主导方** | Verisign + IETF | OWASP | Cisco + LF | 学术 |
| **成熟度** | 🔴 早期 | 🔴 早期 | 🟡 商用 | 🔴 早期 |

**论文应用**：此表直接放入 §7，**作为最重要的"一图胜千言"表格**。

---

## 2 8 维度详解

### 2.1 架构

| 协议 | 架构 | 关键组件 |
|------|------|---------|
| **DNS-AID** | DNS + SVCB | DNS 解析器 + SVCB 记录 + DANE 验证 |
| **ANS-v2** | DNS + Registry | ANS 注册表 + DNS CNAME 链 + TLSA 锚点 |
| **AGNTCY** | 中心化目录 | 单一中心服务器 + HTTPS API + JWT |
| **AIN** | 多跳路由 | AIN 节点 + 路由协议 + 链上锚定 |

### 2.2 发现机制

**DNS-AID**：
```
Client → DNS Query: agent.example.com SVCB
DNS Server → Response: SVCB + DANE TLSA
Client → DANE verify → 拿到 Agent Info
```

**ANS-v2**：
```
Client → DNS Query: agent._ans.example.com
DNS Server → CNAME: ans-registry.example.com
Client → HTTPS GET: /agents/agent-id
Server → JSON response with metadata
```

**AGNTCY**：
```
Client → HTTPS GET: https://directory.agntcy.org/agents/{id}
Server → JSON AgentCard (含能力、协议、版本)
```

**AIN**：
```
Client → AIN Broadcast: "I need agent with capability X"
AIN Routers → Forward through network
Target Agent → Respond
```

### 2.3 身份认证

| 协议 | 认证机制 | 信任根 |
|------|---------|--------|
| **DNS-AID** | DNSSEC + DANE | DNS 根密钥 |
| **ANS-v2** | TLSA + 注册审计 | 注册机构 |
| **AGNTCY** | JWT + 平台 CA | LF CA |
| **AIN** | 链上签名 | 区块链 |

### 2.4 消息格式

| 协议 | 元数据格式 | 大小 |
|------|----------|------|
| **DNS-AID** | SVCB + 紧凑 JSON | 200-500B |
| **ANS-v2** | 完整 JSON | 1-5KB |
| **AGNTCY** | JSON AgentCard | 2-10KB |
| **AIN** | 路由消息 + 引用 | 100-300B |

**关键洞察**：**DNS-AID 最紧凑**（适配 1232B UDP），**AIN 次之**，**AGNTCY 最大**（适合 HTTPS 多 RTT）。

### 2.5 目标范围

| 协议 | 范围 | 规模 |
|------|------|------|
| **DNS-AID** | 全球（DNS 命名空间）| 无限 |
| **ANS-v2** | 域内（需注册）| 数千-数百万 |
| **AGNTCY** | 平台（LF 生态）| 数百-数千 |
| **AIN** | 跨域（多跳）| 数万-数十万 |

### 2.6 优势 vs 限制

**DNS-AID**
- ✅ 优势：极快、零信任、可扩展、复用 40 年 DNS 基础设施
- ❌ 限制：静态元数据、复杂 DNSSEC 链、不支持动态能力

**ANS-v2**
- ✅ 优势：灵活元数据、支持动态更新、审计日志
- ❌ 限制：需注册机构、单点信任、不支持全球级

**AGNTCY**
- ✅ 优势：低门槛、易部署、丰富工具链
- ❌ 限制：单点故障、平台绑定、JWT 集中管理

**AIN**
- ✅ 优势：跨域、动态、智能路由
- ❌ 限制：复杂度高、延迟高、链上依赖

### 2.7 典型场景

**DNS-AID** 适合：
- 智能体高频发现（每秒 1000+ 次）
- 跨平台互信
- 静态能力描述

**ANS-v2** 适合：
- 企业内发现
- 动态能力更新
- 需审计场景

**AGNTCY** 适合：
- 平台内应用市场
- 快速原型
- 已知智能体

**AIN** 适合：
- 跨域复杂任务
- 智能路由
- 跨链 / 跨云

### 2.8 性能（基于 §5.2 计算实验）

| 协议 | P50 | P90 | P99 | 数量级 |
|------|-----|-----|-----|--------|
| DNS-AID | 3ms | 6ms | 10ms | **毫秒级** |
| ANS-v2 | 117ms | 220ms | 404ms | 百毫秒级 |
| AGNTCY | 78ms | 154ms | 260ms | 百毫秒级 |
| AIN | 245ms | 468ms | 825ms | **百毫秒级** |

**关键洞察**：**DNS-AID 比 AIN 快 80 倍**——差异化定位明确。

---

## 3 Table 8: 安全威胁与缓解（生命周期视角）

> 借鉴 arXiv:2505.02279 Table 3-6 范式
> 4 生命周期阶段 × 4 协议

### 3.1 创建阶段（Creation）

| 协议 | 威胁 | 缓解 |
|------|------|------|
| **DNS-AID** | 域名劫持 | DNSSEC、注册商认证 |
| **ANS-v2** | 虚假注册 | KYC、实名验证 |
| **AGNTCY** | 恶意 AgentCard | 平台审核、声誉系统 |
| **AIN** | 节点欺诈 | 链上身份、质押 |

### 3.2 运行阶段（Operation）

| 协议 | 威胁 | 缓解 |
|------|------|------|
| **DNS-AID** | DNS 投毒 | DNSSEC 验证 |
| **ANS-v2** | 注册表篡改 | 多副本、签名验证 |
| **AGNTCY** | API 攻击 | HTTPS、Rate limit |
| **AIN** | 路由劫持 | 多路径、加密 |

### 3.3 更新阶段（Update）

| 协议 | 威胁 | 缓解 |
|------|------|------|
| **DNS-AID** | 缓存陈旧 | TTL 短、SVCB 失效 |
| **ANS-v2** | 旧版本残留 | 版本号、强制升级 |
| **AGNTCY** | 兼容性破坏 | 语义版本、迁移期 |
| **AIN** | 路由振荡 | 路由稳定性协议 |

### 3.4 终止阶段（Termination）

| 协议 | 威胁 | 缓解 |
|------|------|------|
| **DNS-AID** | 域名残留 | 主动注销 |
| **ANS-v2** | 幽灵记录 | TTL 到期清理 |
| **AGNTCY** | 错误下线 | 软删除、备份 |
| **AIN** | 节点消失 | 路由重收敛 |

---

## 4 选型决策树

```
问 1：是否需要跨平台？
├── 否 → AGNTCY（平台内最简）
└── 是 ↓

问 2：是否需要高频发现（>100 qps）？
├── 是 → DNS-AID（毫秒级）
└── 否 ↓

问 3：是否需要动态能力更新？
├── 是 → ANS-v2（灵活元数据）
└── 否 ↓

问 4：是否需要跨域路由？
├── 是 → AIN（多跳）
└── 否 → AGNTCY 备选
```

**论文应用**：作为 Figure 4（决策流程图）。

---

## 5 Table 9: 协议组合推荐

| 场景 | 推荐组合 | 原因 |
|------|---------|------|
| 企业内研究助手 | A2A + MCP × N | Anthropic 模式 |
| 跨公司供应链 | A2A + ACP + ANS | 商业协议 |
| 开发者工具（IDE AI）| MCP only | Claude Code 模式 |
| 智能体市场 | ANS + A2A + MCP | 三层都用 |
| 跨境电商 | AIN + ACP + UCP | 跨域 + 商业 |
| 智能体银行 | AIN + GB/Z 185.2 | 高安全 + 强身份 |

---

## 6 总结：4 协议定位图

```
                速度
                 ↑
                 │
        DNS-AID  ●
                 │
                 │
                 │          ANS
        AGNTCY   ●          ●
                 │
                 │                AIN
                 │                ●
                 └─────────────────────→ 复杂度
```

**论文应用**：作为 Figure 5（4 协议定位图）。

---

## 7 与 arXiv:2505.02279 Table 7 的差异

| 维度 | 2505.02279 Table 7 | 本文 Table 7 |
|------|------------------|-------------|
| 协议数 | 4（MCP/ACP/A2A/ANP）| 4（DNS-AID/ANS/AGNTCY/AIN）|
| 维度数 | 7 | **12**（+延迟/标准化/主导方/成熟度）|
| 性能 | 无 | **含 P50/P90/P99**（基于 §5.2 实验）|
| 决策树 | 无 | **§4 决策树** |
| 选型推荐 | 4 阶段路线图 | **6 场景组合表** |

**论文应用**：本文对比表更全面，**可作直接竞品**。

---

*🤖 Jarvis AI · 第103天 · 2026-06-18 · 4 协议主对比矩阵（v4.0 §7 内容）*

> **完成度**：Table 7 (主对比) + Table 8 (安全) + Table 9 (选型) = 3 张核心表
> **配套图**：Figure 4 (决策树) + Figure 5 (定位图)
> **写作技巧应用**：#2 严格结构平行 + #5 高密度信息表 + #7 安全是生命周期问题
