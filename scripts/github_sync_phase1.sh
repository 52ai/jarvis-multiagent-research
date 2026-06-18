#!/bin/bash
# 033 课题 Phase 1 成果 GitHub 同步脚本
# 仓库: jarvis-multiagent-research
# 用法: bash /workspace/033-MultiAgentResearch/scripts/github_sync_phase1.sh [commit_message]

set -e

# Token 来源（优先环境变量，回退到 .env 文件）
# 注意：本脚本不硬编码任何密钥，避免 commit 触发 GitHub push protection
if [ -n "$GITHUB_TOKEN_033" ]; then
    TOKEN="$GITHUB_TOKEN_033"
elif [ -f "/workspace/.env" ]; then
    TOKEN=$(grep -E "^GITHUB_TOKEN_033=" /workspace/.env | cut -d= -f2)
else
    echo "❌ 找不到 GitHub token"
    echo "请选择以下任一方式："
    echo "  1) export GITHUB_TOKEN_033=<你的 GitHub PAT>"
    echo "  2) 在 /workspace/.env 添加: GITHUB_TOKEN_033=<你的 GitHub PAT>"
    echo ""
    echo "Wayne 当前 TOOLS.md 中公开的 token 也可通过环境变量传入："
    echo "  export GITHUB_TOKEN_033=\$(grep GITHUB_TOKEN /workspace/TOOLS.md | head -1 | awk -F'[ \"]+' '{print \$3}')"
    exit 1
fi

REPO_NAME="jarvis-multiagent-research"
LOCAL_DIR="/workspace/033-MultiAgentResearch"
REMOTE_URL="https://${TOKEN}@github.com/52ai/${REPO_NAME}.git"
COMMIT_MSG="${1:-chore(033): Phase 1 收尾 - 5篇论文+v1.1报告+monitor cron}"

cd "$LOCAL_DIR"

# 1. 初始化 git 仓库（首次）
if [ ! -d ".git" ]; then
    echo "📦 初始化 git 仓库..."
    git init
    git config user.name "Wayne Yu"
    git config user.email "wayne@example.com"
    git branch -M main
    git remote add origin "$REMOTE_URL"
else
    git remote set-url origin "$REMOTE_URL"
fi

# 2. .gitignore 排除临时文件
if [ ! -f ".gitignore" ]; then
    cat > .gitignore <<'EOF'
__pycache__/
*.pyc
.DS_Store
*.tmp
.venv/
EOF
fi

# 3. 添加所有变更
echo "📝 添加文件..."
git add -A

# 4. 统计本次 commit 内容
FILE_COUNT=$(git diff --cached --name-only | wc -l)
echo "📊 待提交文件数: $FILE_COUNT"
git diff --cached --stat

# 5. 提交
echo "💾 提交: $COMMIT_MSG"
git commit -m "$COMMIT_MSG" || {
    echo "⚠️ 没有需要提交的变更"
    exit 0
}

# 6. 推送到 main 分支
echo "🚀 推送到 GitHub..."
git push -u origin main 2>&1

echo ""
echo "✅ 同步完成"
echo "🔗 仓库: https://github.com/52ai/${REPO_NAME}"
