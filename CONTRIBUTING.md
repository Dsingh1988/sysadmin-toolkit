# 🤝 Contributing to Linux SysAdmin Automation Toolkit

Thank you for your interest in contributing! This project is built by sysadmins, for sysadmins — every improvement matters.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Script Standards](#script-standards)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)

---

## 📜 Code of Conduct

Be respectful, constructive, and collaborative. This is a professional community.

---

## 🚀 How to Contribute

### Types of contributions welcome:
- 🐛 **Bug fixes** — script errors, edge cases, OS compatibility issues
- ✨ **New scripts** — automation for common sysadmin tasks
- 📖 **Documentation** — README improvements, usage examples, inline comments
- 🧪 **Tests** — shell test cases, API test coverage
- 🌐 **OS support** — extending scripts to Ubuntu, Debian, SUSE

---

## 🛠️ Development Setup

```bash
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/sysadmin-toolkit.git
cd sysadmin-toolkit

# 2. Create a feature branch
git checkout -b feature/my-new-script

# 3. Make your changes

# 4. Lint your bash scripts
shellcheck scripts/your_module/your_script.sh

# 5. Test on a Linux system (RHEL/Rocky/Ubuntu preferred)
sudo bash scripts/your_module/your_script.sh --help

# 6. Push and open a PR
git push origin feature/my-new-script
```

---

## 📝 Script Standards

All bash scripts must follow these standards:

### Header Block (required)
```bash
#!/usr/bin/env bash
# =============================================================================
# script_name.sh — Short Description
# =============================================================================
# Author  : Your Name <your@email.com>
# License : MIT
# Version : 1.0.0
#
# Description:
#   What this script does.
#
# Usage:
#   sudo ./script_name.sh [OPTIONS]
# =============================================================================
```

### Coding Standards
- Use `set -euo pipefail` at the top
- All variables quoted: `"$var"` not `$var`
- Functions for all logic (no bare code except `main()`)
- Support `--help` flag
- Use exit codes: `0` = OK, `1` = warning, `2` = critical
- Log to `/var/log/` where appropriate
- No hardcoded paths — use variables

### Compatibility
- Test on RHEL/Rocky Linux 8+ **and** Ubuntu 20.04+
- Note OS-specific differences with `if [[ -f /etc/redhat-release ]]`
- Use `command -v tool` before calling any external tool

---

## 🔁 Pull Request Process

1. **One feature per PR** — keep PRs focused
2. **Update README** if adding a new script or feature
3. **Pass ShellCheck** — `shellcheck --severity=warning your_script.sh`
4. **Test on real Linux** — not just dry-run
5. **PR title format**: `feat: add dns_zone_transfer_check.sh` or `fix: disk_health lvm detection on Ubuntu`

### PR Template
Your PR will be auto-filled with our template. Required fields:
- What does this PR do?
- Which OS/distro was it tested on?
- Any breaking changes?

---

## 🐛 Issue Reporting

Use GitHub Issues with the appropriate template:
- **Bug Report** — script fails, wrong output, OS incompatibility
- **Feature Request** — new script idea, new module

Please include:
- OS and version (`cat /etc/os-release`)
- Script version
- Full error output
- Steps to reproduce

---

## 🏷️ Versioning

This project uses [Semantic Versioning](https://semver.org/):
- `MAJOR.MINOR.PATCH` — e.g. `1.2.0`
- Bump `PATCH` for bug fixes
- Bump `MINOR` for new scripts/features
- Bump `MAJOR` for breaking changes

---

*Built with ❤️ by [Devendra Singh Chouhan](https://github.com/Dsingh1988)*
