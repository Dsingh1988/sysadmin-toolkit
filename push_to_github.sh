#!/usr/bin/env bash
# =============================================================================
# push_to_github.sh — One-command setup and push to GitHub
# =============================================================================
# Run this script from the sysadmin-toolkit/ directory after extracting the zip.
# It will:
#   1. Initialize git
#   2. Create the repo on GitHub (via gh CLI if available)
#   3. Commit everything
#   4. Push to github.com/Dsingh1988/sysadmin-toolkit
#
# Usage:
#   chmod +x push_to_github.sh
#   ./push_to_github.sh
# =============================================================================

set -euo pipefail

GITHUB_USER="Dsingh1988"
REPO_NAME="sysadmin-toolkit"
REPO_DESC="Production-grade Linux SysAdmin automation scripts, Ansible playbooks, and FastAPI REST interface for enterprise infrastructure management."
REMOTE_URL="https://github.com/${GITHUB_USER}/${REPO_NAME}.git"

GREEN='\033[0;32m'; CYAN='\033[0;36m'; YELLOW='\033[1;33m'; BOLD='\033[1m'; RESET='\033[0m'

echo -e "${BOLD}${CYAN}======================================${RESET}"
echo -e "${BOLD}${CYAN}  SysAdmin Toolkit — GitHub Pusher   ${RESET}"
echo -e "${BOLD}${CYAN}======================================${RESET}\n"

# ─── Step 1: Git init ─────────────────────────────────────────────────────────
echo -e "${CYAN}[1/5]${RESET} Initializing git repository..."
git init
git branch -M main

# ─── Step 2: Create .gitignore ────────────────────────────────────────────────
echo -e "${CYAN}[2/5]${RESET} Creating .gitignore..."
cat > .gitignore <<'EOF'
# Python
__pycache__/
*.pyc
*.pyo
.venv/
venv/
.env

# Logs
*.log
/var/log/

# Ansible sensitive files
ansible/inventory/hosts.yml
ansible/vault_pass.txt
*.vault

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
EOF

# ─── Step 3: Stage everything ─────────────────────────────────────────────────
echo -e "${CYAN}[3/5]${RESET} Staging all files..."
git add .
git status --short

# ─── Step 4: Commit ───────────────────────────────────────────────────────────
echo -e "${CYAN}[4/5]${RESET} Creating initial commit..."
git commit -m "feat: initial release — Linux SysAdmin Automation Toolkit v1.0.0

- Bash scripts: disk health, SSH hardening, service sweep, user audit
- FastAPI REST interface for remote script execution
- Ansible playbooks: security hardening, fleet management
- Docker + docker-compose deployment
- GitHub Actions CI (ShellCheck, pytest, ansible-lint, docker build)
- Full documentation and contribution guidelines"

# ─── Step 5: Push ─────────────────────────────────────────────────────────────
echo -e "${CYAN}[5/5]${RESET} Pushing to GitHub..."

if command -v gh &>/dev/null; then
  echo -e "${YELLOW}GitHub CLI detected — creating repo automatically...${RESET}"
  gh repo create "${GITHUB_USER}/${REPO_NAME}" \
    --public \
    --description "$REPO_DESC" \
    --source=. \
    --remote=origin \
    --push
  echo -e "${GREEN}✅ Repo created and pushed via GitHub CLI!${RESET}"
else
  echo -e "${YELLOW}GitHub CLI not found. Adding remote and pushing...${RESET}"
  echo -e "${YELLOW}Make sure you have already created the repo at:${RESET}"
  echo -e "${YELLOW}  https://github.com/${GITHUB_USER}/${REPO_NAME}${RESET}\n"

  git remote add origin "$REMOTE_URL" 2>/dev/null || git remote set-url origin "$REMOTE_URL"
  git push -u origin main
  echo -e "${GREEN}✅ Pushed to GitHub!${RESET}"
fi

echo ""
echo -e "${BOLD}${GREEN}============================================${RESET}"
echo -e "${BOLD}${GREEN}  ALL DONE!${RESET}"
echo -e "${BOLD}${GREEN}============================================${RESET}"
echo -e "  Repo : https://github.com/${GITHUB_USER}/${REPO_NAME}"
echo -e "  Docs : https://github.com/${GITHUB_USER}/${REPO_NAME}#readme"
echo ""
echo -e "${BOLD}Next steps:${RESET}"
echo -e "  1. ${CYAN}Pin this repo${RESET} on your GitHub profile"
echo -e "  2. ${CYAN}Add topics/tags${RESET}: linux, sysadmin, ansible, bash, devops, automation, fastapi"
echo -e "  3. ${CYAN}Create your Profile README${RESET}: see GITHUB_PROFILE_README.md"
echo -e "     → Create repo: github.com/new → name it exactly '${GITHUB_USER}' → paste contents"
echo -e "  4. ${CYAN}Share on LinkedIn${RESET} with your post about the toolkit"
echo -e "${BOLD}${GREEN}============================================${RESET}"
