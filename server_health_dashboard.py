#!/usr/bin/env python3
"""
=============================================================
  Linux Server Health Dashboard
  Author : Devendra Singh | github.com/Dsingh1988
  Repo   : github.com/Dsingh1988/sysadmin-toolkit
  License: MIT
  Version: 1.0.0
=============================================================
  Instant server health snapshot — CPU, Memory, Disk, Network,
  Top Processes, Failed Services, Load Average & more.
  Works on: RHEL / Rocky / CentOS / Ubuntu / Debian
=============================================================
"""

import os
import sys
import platform
import subprocess
import shutil
import datetime

# ── ANSI Colours ────────────────────────────────────────────
R  = "\033[91m"   # Red
Y  = "\033[93m"   # Yellow
G  = "\033[92m"   # Green
B  = "\033[94m"   # Blue
C  = "\033[96m"   # Cyan
W  = "\033[97m"   # White
DIM= "\033[2m"
BOLD="\033[1m"
RST= "\033[0m"

def color_pct(val, warn=70, crit=90):
    if val >= crit: return f"{R}{val:.1f}%{RST}"
    if val >= warn: return f"{Y}{val:.1f}%{RST}"
    return f"{G}{val:.1f}%{RST}"

def bar(pct, width=30):
    filled = int(width * pct / 100)
    empty  = width - filled
    if   pct >= 90: col = R
    elif pct >= 70: col = Y
    else:           col = G
    return f"{col}{'█' * filled}{DIM}{'░' * empty}{RST}"

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return ""

def section(title):
    print(f"\n{BOLD}{C}{'─'*60}{RST}")
    print(f"{BOLD}{W}  {title}{RST}")
    print(f"{BOLD}{C}{'─'*60}{RST}")

# ── Header ───────────────────────────────────────────────────
def print_header():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hostname = platform.node()
    kernel   = platform.release()
    distro   = run("cat /etc/os-release | grep PRETTY_NAME | cut -d= -f2 | tr -d '\"'") or platform.system()
    uptime   = run("uptime -p")
    print(f"""
{BOLD}{B}╔══════════════════════════════════════════════════════════╗
║        Linux Server Health Dashboard  v1.0.0             ║
║        github.com/Dsingh1988/sysadmin-toolkit            ║
╚══════════════════════════════════════════════════════════╝{RST}
  {DIM}Host   :{RST} {W}{hostname}{RST}
  {DIM}OS     :{RST} {W}{distro}{RST}
  {DIM}Kernel :{RST} {W}{kernel}{RST}
  {DIM}Uptime :{RST} {W}{uptime}{RST}
  {DIM}Report :{RST} {W}{now}{RST}
""")

# ── CPU ──────────────────────────────────────────────────────
def cpu_info():
    section("CPU")
    try:
        import psutil
        pct     = psutil.cpu_percent(interval=1)
        count   = psutil.cpu_count(logical=True)
        freq    = psutil.cpu_freq()
        load    = os.getloadavg()
        print(f"  Logical CPUs : {W}{count}{RST}")
        if freq:
            print(f"  Frequency    : {W}{freq.current:.0f} MHz{RST}")
        print(f"  Load Avg     : {W}{load[0]:.2f} / {load[1]:.2f} / {load[2]:.2f}{RST}  (1m / 5m / 15m)")
        print(f"  Usage        : {bar(pct)}  {color_pct(pct)}")
    except ImportError:
        # Fallback without psutil
        load = run("cat /proc/loadavg").split()[:3]
        cores = run("nproc")
        print(f"  Logical CPUs : {W}{cores}{RST}")
        print(f"  Load Avg     : {W}{' / '.join(load)}{RST}  (1m / 5m / 15m)")
        print(f"  {Y}Install psutil for richer CPU metrics: pip3 install psutil{RST}")

# ── Memory ───────────────────────────────────────────────────
def memory_info():
    section("Memory & Swap")
    try:
        import psutil
        mem  = psutil.virtual_memory()
        swap = psutil.swap_memory()
        def fmt(b): return f"{b/1024**3:.2f} GB"
        ram_pct = mem.percent
        print(f"  RAM Total    : {W}{fmt(mem.total)}{RST}")
        print(f"  RAM Used     : {color_pct(ram_pct)}  ({fmt(mem.used)} / {fmt(mem.total)})")
        print(f"  RAM          : {bar(ram_pct)}")
        print(f"  Swap Used    : {color_pct(swap.percent)}  ({fmt(swap.used)} / {fmt(swap.total)})")
        print(f"  Swap         : {bar(swap.percent)}")
    except ImportError:
        lines = run("free -h").splitlines()
        for l in lines:
            print(f"  {l}")

# ── Disk ─────────────────────────────────────────────────────
def disk_info():
    section("Disk Usage")
    try:
        import psutil
        for part in psutil.disk_partitions():
            if 'loop' in part.device or part.fstype in ('tmpfs','devtmpfs','squashfs'):
                continue
            try:
                usage = psutil.disk_usage(part.mountpoint)
                pct   = usage.percent
                total = f"{usage.total/1024**3:.1f}G"
                used  = f"{usage.used/1024**3:.1f}G"
                free  = f"{usage.free/1024**3:.1f}G"
                print(f"  {W}{part.mountpoint:<20}{RST} {bar(pct,width=20)}  {color_pct(pct)}  {used}/{total}  free:{free}")
            except PermissionError:
                pass
    except ImportError:
        lines = run("df -hT | grep -vE 'tmpfs|loop|udev'").splitlines()
        for l in lines:
            print(f"  {l}")

# ── Network ──────────────────────────────────────────────────
def network_info():
    section("Network Interfaces")
    try:
        import psutil
        stats = psutil.net_io_counters(pernic=True)
        addrs = psutil.net_if_addrs()
        for iface, s in stats.items():
            if iface == 'lo': continue
            ip = "N/A"
            if iface in addrs:
                for a in addrs[iface]:
                    if a.family.name == 'AF_INET':
                        ip = a.address
            rx = f"{s.bytes_recv/1024**2:.1f} MB"
            tx = f"{s.bytes_sent/1024**2:.1f} MB"
            print(f"  {W}{iface:<12}{RST}  IP: {C}{ip:<18}{RST}  RX: {G}{rx:<12}{RST}  TX: {Y}{tx}{RST}")
    except ImportError:
        out = run("ip -br addr")
        for l in out.splitlines():
            print(f"  {l}")

# ── Top Processes ────────────────────────────────────────────
def top_processes():
    section("Top 5 Processes by CPU & Memory")
    try:
        import psutil
        procs = []
        for p in psutil.process_iter(['pid','name','cpu_percent','memory_percent','status']):
            try:
                procs.append(p.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        # Top by CPU
        top_cpu = sorted(procs, key=lambda x: x['cpu_percent'] or 0, reverse=True)[:5]
        print(f"\n  {BOLD}By CPU:{RST}")
        print(f"  {'PID':<8} {'Name':<22} {'CPU%':<8} {'MEM%'}")
        print(f"  {'─'*50}")
        for p in top_cpu:
            print(f"  {p['pid']:<8} {p['name'][:22]:<22} {color_pct(p['cpu_percent'] or 0):<20} {color_pct(p['memory_percent'] or 0)}")
        # Top by MEM
        top_mem = sorted(procs, key=lambda x: x['memory_percent'] or 0, reverse=True)[:5]
        print(f"\n  {BOLD}By Memory:{RST}")
        print(f"  {'PID':<8} {'Name':<22} {'CPU%':<8} {'MEM%'}")
        print(f"  {'─'*50}")
        for p in top_mem:
            print(f"  {p['pid']:<8} {p['name'][:22]:<22} {color_pct(p['cpu_percent'] or 0):<20} {color_pct(p['memory_percent'] or 0)}")
    except ImportError:
        out = run("ps aux --sort=-%cpu | head -6")
        for l in out.splitlines():
            print(f"  {l}")

# ── Failed Services ──────────────────────────────────────────
def failed_services():
    section("Failed Systemd Services")
    out = run("systemctl list-units --state=failed --no-legend 2>/dev/null | head -20")
    if out:
        for l in out.splitlines():
            print(f"  {R}✖{RST}  {l}")
    else:
        print(f"  {G}✔  No failed services{RST}")

# ── Last Logins ───────────────────────────────────────────────
def last_logins():
    section("Last 5 Logins")
    out = run("last -n 5 --time-format iso 2>/dev/null || last -n 5")
    if out:
        for l in out.splitlines():
            print(f"  {DIM}{l}{RST}")
    else:
        print(f"  {Y}Could not retrieve login history{RST}")

# ── Alerts Summary ───────────────────────────────────────────
def alerts_summary():
    section("Health Alerts")
    alerts = []
    try:
        import psutil
        # CPU
        cpu = psutil.cpu_percent(interval=0.5)
        if cpu >= 90:  alerts.append((R, f"CRITICAL: CPU usage at {cpu:.1f}%"))
        elif cpu >= 70: alerts.append((Y, f"WARNING : CPU usage at {cpu:.1f}%"))
        # Memory
        mem = psutil.virtual_memory()
        if mem.percent >= 90:  alerts.append((R, f"CRITICAL: Memory usage at {mem.percent:.1f}%"))
        elif mem.percent >= 75: alerts.append((Y, f"WARNING : Memory usage at {mem.percent:.1f}%"))
        # Disks
        for part in psutil.disk_partitions():
            if 'loop' in part.device: continue
            try:
                usage = psutil.disk_usage(part.mountpoint)
                if usage.percent >= 90:  alerts.append((R, f"CRITICAL: Disk {part.mountpoint} at {usage.percent:.1f}%"))
                elif usage.percent >= 80: alerts.append((Y, f"WARNING : Disk {part.mountpoint} at {usage.percent:.1f}%"))
            except: pass
    except ImportError:
        alerts.append((Y, "Install psutil for automated alerts: pip3 install psutil"))

    if alerts:
        for col, msg in alerts:
            print(f"  {col}⚠  {msg}{RST}")
    else:
        print(f"  {G}✔  All systems nominal{RST}")

# ── Footer ───────────────────────────────────────────────────
def print_footer():
    print(f"\n{BOLD}{C}{'─'*60}{RST}")
    print(f"  {DIM}Tool by Devendra Singh  |  github.com/Dsingh1988{RST}")
    print(f"  {DIM}Part of: sysadmin-toolkit  |  MIT License{RST}")
    print(f"{BOLD}{C}{'─'*60}{RST}\n")

# ── Main ─────────────────────────────────────────────────────
if __name__ == "__main__":
    print_header()
    cpu_info()
    memory_info()
    disk_info()
    network_info()
    top_processes()
    failed_services()
    last_logins()
    alerts_summary()
    print_footer()
