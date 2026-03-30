# 🛠️ Linux SysAdmin Automation Toolkit

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Shell](https://img.shields.io/badge/Shell-Bash-4EAA25?logo=gnubash&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-2.14+-EE0000?logo=ansible&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-RHEL%20%7C%20Rocky%20%7C%20AlmaLinux%20%7C%20Ubuntu-red)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
![Stars](https://img.shields.io/github/stars/Dsingh1988/sysadmin-toolkit?style=social)

**A production-grade collection of automation scripts, Ansible playbooks, and a FastAPI REST interface for Linux enterprise infrastructure management.**

*Built by a 15+ year enterprise infrastructure veteran. Battle-tested on 50+ physical servers and 150+ VMs.*

[📖 Documentation](#documentation) • [🚀 Quick Start](#quick-start) • [🤝 Contributing](CONTRIBUTING.md) • [🐛 Report a Bug](https://github.com/Dsingh1988/sysadmin-toolkit/issues)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Module Documentation](#module-documentation)
- [REST API](#rest-api)
- [Ansible Playbooks](#ansible-playbooks)
- [Docker Deployment](#docker-deployment)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

The **Linux SysAdmin Automation Toolkit** is an open-source project designed to automate repetitive and complex Linux system administration tasks across enterprise environments. It targets:

- **Disk & Storage** — health checks, LVM management, NAS mounts, capacity alerts
- **Network** — interface diagnostics, firewall audits, latency monitoring, DNS validation
- **Security** — SSH hardening, user audits, failed login reports, CVE patch checks
- **Services** — systemd status sweeps, HA cluster health (Pacemaker/DRBD), auto-restart
- **User Management** — bulk user provisioning, sudo audits, LDAP sync checks

All scripts are designed for **RHEL 8/9, Rocky Linux 8/9, AlmaLinux 8/9**, and **Ubuntu 20.04/22.04/24.04**.

---

## ✨ Features

| Module | Capability |
|--------|-----------|
| 🖴 **Disk** | SMART health, LVM thin-pool alerts, ZFS/XFS integrity checks |
| 🌐 **Network** | MTU discovery, BGP neighbor status, NIC bonding validation |
| 🔐 **Security** | CIS benchmark audit, SSH hardening, failed auth report |
| ⚙️ **Services** | Systemd sweep, Pacemaker cluster status, auto-remediation |
| 👤 **Users** | Bulk LDAP provisioning, stale account detection, sudo audit |
| 📡 **API** | FastAPI REST interface for remote script execution |
| 📦 **Ansible** | Idempotent playbooks for fleet-wide configuration |
| 🐳 **Docker** | Containerized API deployment with Compose |

---

## 📁 Project Structure

```
sysadmin-toolkit/
├── scripts/
│   ├── disk/
│   │   ├── disk_health_check.sh       # SMART + LVM + filesystem checks
│   │   ├── lvm_thin_pool_monitor.sh   # Thin-pool usage alerts
│   │   └── nas_mount_verify.sh        # NetApp/Synology NFS mount validation
│   ├── network/
│   │   ├── network_audit.sh           # Full NIC/bond/VLAN diagnostics
│   │   ├── dns_bulk_check.sh          # BIND/DNS zone health checker
│   │   └── firewall_audit.sh          # firewalld/iptables rule reporter
│   ├── security/
│   │   ├── ssh_hardening.sh           # CIS-compliant SSH config enforcer
│   │   ├── failed_login_report.sh     # Auth log parser + email report
│   │   └── cis_benchmark_audit.sh     # Lightweight CIS Level 1 audit
│   ├── services/
│   │   ├── service_health_sweep.sh    # Systemd service status checker
│   │   ├── pacemaker_status.sh        # Pacemaker/DRBD HA cluster health
│   │   └── auto_restart_service.sh    # Intelligent service auto-restarter
│   └── users/
│       ├── bulk_user_provision.sh     # CSV-driven user provisioning
│       ├── stale_account_audit.sh     # Detect inactive/expired accounts
│       └── sudo_audit.sh             # Sudoers privilege report
├── ansible/
│   ├── inventory/
│   │   └── hosts.example.yml
│   ├── playbooks/
│   │   ├── site.yml
│   │   ├── security_hardening.yml
│   │   ├── service_deploy.yml
│   │   └── user_management.yml
│   └── roles/
│       ├── common/
│       ├── ssh_hardening/
│       └── monitoring_agent/
├── api/
│   ├── main.py                        # FastAPI entry point
│   ├── routes/
│   │   ├── disk.py
│   │   ├── network.py
│   │   ├── security.py
│   │   └── services.py
│   ├── models/
│   │   └── schemas.py
│   └── requirements.txt
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── .github/
│   ├── workflows/
│   │   └── ci.yml
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── feature_request.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- Linux: RHEL/Rocky/AlmaLinux 8+ or Ubuntu 20.04+
- Bash 4.x+
- Python 3.10+ (for API)
- Ansible 2.14+ (for playbooks)
- Docker & Docker Compose (optional, for API container)

### Clone the Repository

```bash
git clone https://github.com/Dsingh1988/sysadmin-toolkit.git
cd sysadmin-toolkit
chmod +x scripts/**/*.sh
```

### Run a Script Directly

```bash
# Check disk health across all mounted volumes
sudo ./scripts/disk/disk_health_check.sh

# Audit SSH configuration against CIS benchmarks
sudo ./scripts/security/ssh_hardening.sh --audit-only

# Generate a failed login report (last 7 days)
sudo ./scripts/security/failed_login_report.sh --days 7 --email admin@yourdomain.com

# Check all systemd services
./scripts/services/service_health_sweep.sh --critical-only
```

### Start the REST API

```bash
cd api
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

API docs available at: `http://localhost:8000/docs`

### Docker Deployment

```bash
cd docker
docker-compose up -d
```

---

## 📖 Module Documentation

### 🖴 Disk Module

#### `disk_health_check.sh`
Checks SMART status for all physical drives, LVM volume group usage, and XFS/ext4 filesystem integrity.

```bash
sudo ./scripts/disk/disk_health_check.sh [OPTIONS]

Options:
  --threshold <N>    Alert if disk usage > N% (default: 85)
  --email <addr>     Send report to email address
  --json             Output in JSON format
  --quiet            Only print warnings/errors
```

#### `lvm_thin_pool_monitor.sh`
Monitors LVM thin-pool data and metadata usage. Sends alerts before pools fill up (a common cause of VM crashes).

```bash
sudo ./scripts/disk/lvm_thin_pool_monitor.sh --threshold 80
```

#### `nas_mount_verify.sh`
Validates NFS/CIFS mounts (NetApp, Synology, HP NAS). Checks mount status, read/write access, and latency.

```bash
sudo ./scripts/disk/nas_mount_verify.sh --config /etc/nas_mounts.conf
```

---

### 🌐 Network Module

#### `network_audit.sh`
Full network interface diagnostic: NIC status, bonding/teaming, VLAN tagging, MTU, and routing table validation.

```bash
./scripts/network/network_audit.sh --verbose
```

#### `dns_bulk_check.sh`
Validates DNS zone resolution for a list of domains against BIND or external resolvers. Ideal for environments managing 40K+ domains.

```bash
./scripts/network/dns_bulk_check.sh --domains /path/to/domains.txt --resolver 8.8.8.8
```

---

### 🔐 Security Module

#### `ssh_hardening.sh`
Enforces CIS Benchmark Level 1 SSH settings: disables root login, enforces key-based auth, sets ciphers/MACs, configures idle timeout.

```bash
sudo ./scripts/security/ssh_hardening.sh          # Apply hardening
sudo ./scripts/security/ssh_hardening.sh --audit  # Audit only, no changes
sudo ./scripts/security/ssh_hardening.sh --dry-run # Preview changes
```

#### `failed_login_report.sh`
Parses `/var/log/secure` and `/var/log/auth.log`, aggregates failed SSH/sudo attempts, identifies top attacker IPs, and optionally emails the report.

```bash
sudo ./scripts/security/failed_login_report.sh --days 7
```

---

### ⚙️ Services Module

#### `service_health_sweep.sh`
Sweeps all systemd units, identifies failed/degraded services, optionally attempts auto-restart, and produces a status report.

```bash
./scripts/services/service_health_sweep.sh
./scripts/services/service_health_sweep.sh --auto-restart --critical-only
```

#### `pacemaker_status.sh`
Checks Pacemaker/DRBD cluster health: node quorum, resource status, split-brain detection, and DRBD replication lag.

```bash
sudo ./scripts/services/pacemaker_status.sh
```

---

### 👤 User Management Module

#### `bulk_user_provision.sh`
CSV-driven user creation with home directory, shell, group assignment, SSH key injection, and optional LDAP attribute setting.

```bash
# CSV format: username,fullname,group,shell,ssh_pubkey
sudo ./scripts/users/bulk_user_provision.sh --csv /path/to/users.csv
```

#### `sudo_audit.sh`
Produces a full report of sudoers privileges: direct entries, group memberships, and NOPASSWD flags.

```bash
sudo ./scripts/users/sudo_audit.sh --output /var/log/sudo_audit_$(date +%F).txt
```

---

## 🌐 REST API

The FastAPI interface lets you trigger scripts remotely via HTTP, making integration with monitoring tools (Grafana, Prometheus, Zabbix) easy.

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/disk/health` | Run disk health check |
| GET | `/api/v1/disk/lvm-pools` | LVM thin-pool status |
| GET | `/api/v1/network/audit` | Network interface audit |
| GET | `/api/v1/security/ssh-audit` | SSH config audit |
| POST | `/api/v1/security/ssh-harden` | Apply SSH hardening |
| GET | `/api/v1/services/sweep` | Service health sweep |
| GET | `/api/v1/users/sudo-audit` | Sudo privilege report |

### Example

```bash
curl http://localhost:8000/api/v1/disk/health
# Returns JSON with disk status for all volumes
```

Interactive Swagger docs: `http://localhost:8000/docs`

---

## 📦 Ansible Playbooks

### Run the full site playbook

```bash
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/site.yml
```

### Run security hardening only

```bash
ansible-playbook -i ansible/inventory/hosts.yml ansible/playbooks/security_hardening.yml --limit webservers
```

---

## 🐳 Docker Deployment

```yaml
# docker/docker-compose.yml
version: "3.9"
services:
  sysadmin-api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - /var/log:/var/log:ro
    restart: unless-stopped
```

```bash
docker-compose up -d
docker-compose logs -f
```

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Quick contribution steps:**
1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-script`
3. Write your script with inline documentation
4. Add a test or usage example
5. Submit a Pull Request

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Devendra Singh Chouhan**
- 🏢 Head of IT Infrastructure, Data Ingenious Global Ltd
- 🎓 M.Tech, BITS Pilani | RHCSA | AWS SysOps | GCP ACE | NVIDIA AI Infrastructure
- 💼 [LinkedIn](https://linkedin.com/in/devendra-singh-chouhan) | [GitHub](https://github.com/Dsingh1988)
- 📧 debuchouhan@gmail.com

> *"Automate what's repetitive. Document what matters. Share what you learn."*

---

<div align="center">
⭐ If this toolkit saves you time, please give it a star!
</div>
