# 033 课题脚本索引

> **路径**：`scripts/README.md`
> **创建**：2026-06-18 · Jarvis AI · 第103天
> **作用**：033 仓库内所有脚本的入口导航

---

## 📁 目录结构

```
033-MultiAgentResearch/
├── scripts/                              ← 本目录
│   ├── README.md                          ← 本文件（索引）
│   ├── weekly_monitor_gen.py              ← 每周热点追踪（cron 化）
│   ├── github_sync_phase1.sh              ← Phase 1 GitHub 推送
│   └── owl/                               ← OWL 框架参考（arXiv:2505.23885）
│
└── 02-Experiments/scripts/                ← 实验相关
    ├── run_baseline_v0.1.py               ← 180 次实验启动器
    └── llm_judge.py                       ← LLM-as-Judge 评估器
```

---

## 🎯 各脚本用途

### 1. `weekly_monitor_gen.py`（033 仓库根）
**功能**：每周生成多智能体领域热点追踪报告  
**输入**：6 个预设关键词 + 可选 `--keywords-file`  
**输出**：`04-FrontierHotspots/weekly-monitor-YYYY-MM-DD.md`  
**Cron**：每周三 10:00 CST 自动运行（job `68d3efb4-bd8b-4077-9656-b330dba1e770`）

**用法**：
```bash
# 默认（手动 + CST 今天）
python3 weekly_monitor_gen.py

# 指定日期
python3 weekly_monitor_gen.py --date 2026-06-25

# 自定义关键词
python3 weekly_monitor_gen.py --keywords-file my_keywords.txt

# 只看输出不写文件
python3 weekly_monitor_gen.py --dry-run
```

---

### 2. `github_sync_phase1.sh`（033 仓库根）
**功能**：把 033 仓库变更推送到 GitHub  
**Token 优先级**：环境变量 `$GITHUB_TOKEN_033` > `/workspace/.env`  
**注意**：不硬编码任何密钥（GitHub push protection 要求）

**用法**：
```bash
export GITHUB_TOKEN_033=<your_token>
bash github_sync_phase1.sh "feat: add new analysis"
```

---

### 3. `02-Experiments/scripts/run_baseline_v0.1.py`
**功能**：构建 5 任务 × 12 架构 × 3 重复 = 180 次实验计划  
**状态**：v0.1 是 stub（计划生成 OK，实际调度 W27 启动时实装）  
**输出**：`02-Experiments/results/experiment_plan_YYYYMMDD.json`

**用法**：
```bash
# 全量 dry-run
python3 run_baseline_v0.1.py --dry-run

# 单个任务
python3 run_baseline_v0.1.py --task T1 --dry-run

# 单个架构
python3 run_baseline_v0.1.py --architecture supervised-5 --dry-run
```

---

### 4. `02-Experiments/scripts/llm_judge.py`
**功能**：4 维 LLM-as-judge 评估（fact/struct/read/insight）  
**Judge 模型**：默认 opus-4（MOCK），`--real` 接 OpenAI/Anthropic  
**输出**：
- 单条：`results/eval_<run_id>.json`
- 汇总：`results/judge_report_YYYYMMDD_HHMMSS.md`

**用法**：
```bash
# 批量评估 + 报告
python3 llm_judge.py --batch results/run_*.json --report

# 真实 LLM（需 OPENAI_API_KEY 或 ANTHROPIC_API_KEY）
python3 llm_judge.py --batch results/run_*.json --real --report

# dry-run 看 prompt
python3 llm_judge.py --input results/run_E1_single_r1.json --dry-run
```

---

### 5. `scripts/owl/`（OWL 框架）
**来源**：[github.com/camel-ai/owl](https://github.com/camel-ai/owl)（arXiv:2505.23885）  
**作用**：Phase 2 多 agent 调度的参考实现  
**未上传 GitHub**（.git 排除，避免 gitlink 问题）

---

## 🔗 调用链

```
[weekly-monitor cron]
        │
        ▼
weekly_monitor_gen.py  ──→ 04-FrontierHotspots/weekly-monitor-YYYY-MM-DD.md
        │
        ▼
[用户审阅后] cron_governor.py 收尾

[实验阶段 W27]
        │
        ▼
run_baseline_v0.1.py  ──→ results/run_<id>.json (180 个)
        │
        ▼
llm_judge.py  ──→ results/eval_<id>.json + judge_report_*.md
        │
        ▼
[报告撰写] v1.5 / v3.0
```

---

## 🛠 维护规范

- 任何 Python 脚本必须 `chmod +x` + shebang `#!/usr/bin/env python3`
- 任何 shell 脚本必须 `set -e` + token 从环境变量读
- commit message 用 `feat/fix/chore/docs/refactor` 前缀
- 提交前确保本地有 `PYTHONPATH=/workspace/.python-packages` 路径

---

*🤖 Jarvis AI · 第103天 · 2026-06-18 · 033 脚本索引 v0.1*
