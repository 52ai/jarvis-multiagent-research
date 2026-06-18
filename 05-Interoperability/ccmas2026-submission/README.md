# CCMAS 2026 投稿材料

> **会议**：第四届 CCF 多智能体系统会议（CCMAS 2026）
> **地点**：南京大学苏州校区
> **日期**：2026-06-27 至 06-28（6-26 报到）
> **距离 deadline**：~9 天
> **创建**：2026-06-18 · Jarvis AI · 第103天

---

## 📌 路径

```
05-Interoperability/ccmas2026-submission/
├── README.md           ← 本文件（投稿指南）
├── paper-1-agent-internet.md
├── paper-2-aip-vs-a2a.md
└── paper-3-empirical-multiagent.md
```

---

## 🎯 033 课题组投稿策略

### 论文 1：综述论文（推荐主投）

**标题**：Agent Internet: A Three-Layer Architecture for Cross-Platform AI Agent Interoperability

**摘要要点**：
- 提出 "Agent Internet" 概念（类比 Internet of Things 命名传统）
- 三层架构：业务层 / 协议层 / 网络层
- 系统梳理 2025-2026 年主流方案
- 中国 GB/Z 185-2026 国家标准与国际标准对比
- 10+ 篇核心文献 + 119,757 端点实证（Verisign 2026-06）

**篇幅**：6 页 + 1 页参考文献
**类型**：System/Position Paper

---

### 论文 2：对比研究（候选）

**标题**：National vs Open Standards: A Comparative Study of China's AIP and International A2A/MCP Protocols

**摘要要点**：
- 对比中国 AIP（GB/Z 185-2026）与国际 A2A/MCP
- 7 维分析：治理 / 身份 / 发现 / 兼容性 / 合规 / 跨境 / 演进
- 提出"协议地理学"（Protocol Geography）概念
- 政策建议

**篇幅**：6 页
**类型**：Comparative Study

---

### 论文 3：实验论文（需 W27 数据）

**标题**：Empirical Study of Multi-Agent System Performance under Different Communication Protocols

**摘要要点**：
- 实验设计：4 互联互通架构 × 5 任务 × 3 重复 = 60 run
- 7 维评分（4 维原有 + 3 维新增）
- H1-H4 假设验证
- MCP/A2A/AIN 性能对比

**状态**：⏸️ 等 W27 真实数据
**风险**：如实验未跑通，可改投 demo 论文

---

## 📅 时间表

| 日期 | 行动 |
|------|------|
| 6/18（今天）| 完成 3 篇摘要草稿 |
| 6/19-20 | 写论文 1 全文（综述）|
| 6/21 | 内审 + 格式调整 |
| 6/22-23 | 提交到 EasyChair |
| 6/24-25 | 备用时间（修回） |
| 6/26 | 大会报到 |
| **6/27-28** | **会议** |

---

## ⚠️ 决策点（等 Wayne 决定）

1. **投稿哪一篇**？
   - 主推论文 1（综述，9 天可完成）
   - 或论文 2（对比，9 天可完成）
2. **是否同时投 2 篇**？
3. **是否要 W27 实验数据**？
4. **作者列表**：Wayne + Jarvis AI（共著）？

---

## 🔗 相关材料

### 033 仓库已有
- `05-Interoperability/智能体互联互通专题报告-v0.2.md`（11K · 主投材料）
- `05-Interoperability/decision-tree-mcp-vs-a2a.md`（6.9K）
- `05-Interoperability/china-perspective.md`（6.5K）
- `05-Interoperability/notes/verisign-dns-ai-discovery-notes.md`（2.7K）
- `05-Interoperability/notes/ain-architecture-notes.md`（2.5K）
- `05-Interoperability/literature/index.md`（4.4K · 16 篇文献）

### CCF 会议信息
- **会议官网**：https://ccf.org.cn/ccmas2026
- **征稿主题**：多智能体系统、协同、决策、博弈、强化学习
- **截稿日期**：2026-06-23（推测）

---

## 📝 论文 1 详细摘要（草稿）

### 标题
**Agent Internet: A Three-Layer Architecture for Cross-Platform AI Agent Interoperability**

### 摘要（300 字）

The rapid proliferation of AI agents across major platforms—Anthropic Claude, OpenAI GPTs, Google Gemini, Microsoft Copilot—has created a critical challenge: agents from different platforms cannot natively discover, communicate, or collaborate. This "closed world" problem mirrors the early Internet's hosts-file era (pre-1983) and manifests as an N² bilateral integration problem at scale.

Drawing on empirical analysis of 119,757 real-world service endpoints and 62,739 MCP server deployments (Verisign 2026), this paper proposes **Agent Internet** as a unifying concept and presents a **three-layer architecture**:

1. **Business Layer** — Commercial relationships (ACP, UCP, NANDA Index, China AIP)
2. **Protocol Layer** — Message exchange (MCP, A2A, AIN)
3. **Network Layer** — Identity and discovery (ANS, DNS-AID, .Agent, AGNTCY, GB/Z 185-2026)

We show that the Internet's 40-year infrastructure (DNS, BGP, TLS, HTTP) is being precisely replicated in the agent layer, and that a single DNS UDP response (1232 bytes) can carry the full 90th-percentile agent metadata (940 bytes). This implies that the "physical layer" of agent interoperability is **already solved** by the existing Internet.

We then provide a comprehensive analysis of China's GB/Z 185-2026 series (7 national standards) and the Agent Interconnection Protocol (AIP), comparing them with international standards. We conclude with three-dimensional recommendations: industry, policy, and technology.

**Keywords**: AI agents, multi-agent systems, interoperability, DNS, Agent Internet, MCP, A2A

### 1. Introduction (草稿大纲)
- 背景：AI 智能体爆发增长 + 互联互通缺位
- 问题：N² 集成复杂度、跨平台协作壁垒
- 解决：本文提出 Agent Internet 概念
- 贡献：(1) 三层架构 (2) Verisign 实证分析 (3) 中国国标对比 (4) 政策建议

### 2. The Closed World Problem
- 5 大平台的智能体现状
- 真实成本分析
- 历史镜鉴：1983 年前互联网

### 3. Three-Layer Architecture
- 业务层（ACP/UCP/NANDA/AIP）
- 协议层（MCP/A2A/AIN）
- 网络层（ANS/DNS-AID/.Agent/AGNTCY/GB/Z 185）

### 4. Empirical Analysis: Agent Metadata Fits in DNS
- Verisign 119,757 端点数据
- 940 字节元数据 vs 1232 字节 DNS UDP
- 三大启示

### 5. Comparative Analysis: China vs International Standards
- GB/Z 185-2026 7 项标准
- AIP 协议
- 信通院 4+N+2 体系
- 治理模式对比

### 6. Three-Dimensional Recommendations
- 产业（短期/中期/长期）
- 政策（最紧迫/关键）
- 技术（标准/研究/开源）

### 7. Conclusion
- Agent Internet = 40 年互联网基础设施的"插入层"
- 2025-2028 窗口期
- 监管 + 学术 + 产业的协同

---

## 📚 论文 1 参考文献（精选 10+）

```
1. Seethiraju, R. R. et al. (2026). Discovering Agents for Discovery:
   The Case for DNS. arXiv:2606.02314v1.
2. Feng, Y. et al. (2026). Agentic Intent Network (AIN) Architecture.
   IETF draft-feng-nmrg-ain-architecture-00.
3. Google. (2025). Announcing the Agent2Agent Protocol (A2A).
   Google Developers Blog, 2025-04-09.
4. Anthropic. (2024). Model Context Protocol Specification.
5. Linux Foundation. (2026). A2A Protocol Surpasses 150 Organizations.
6. Mozley, J. et al. (2026). DNS for AI Discovery (DNS-AID).
   IETF draft-mozleywilliams-dnsop-dnsaid-01.
7. Courtney, S. et al. (2026). Agent Name Service v2 (ANS).
   IETF draft-narajala-courtney-ansv2-01.
8. 国家网信办等三部门. (2026). 智能体规范应用与创新发展实施意见.
9. 国家市场监管总局. (2026). GB/Z 185-2026 系列国家标准.
10. 中国信通院. (2026). 智能体互联网新型基础设施建设.
11. Raskar, R. et al. (2025). Project NANDA. arXiv:2507.14263.
12. Cui, E. et al. (2025). AgentDNS. arXiv:2505.22368.
13. EU. (2024). EU AI Act.
14. IBM Research. (2025). Agent Commerce Protocol (ACP).
15. CCF. (2026). CCMAS 2026 会议.
```

---

## ✅ Wayne 决策清单

- [ ] 投哪一篇（1/2/3）？
- [ ] 作者列表？
- [ ] 6/22 前确认投稿材料

---

*🤖 Jarvis AI · 第103天 · 2026-06-18 · CCMAS 2026 投稿材料 v0.1*
