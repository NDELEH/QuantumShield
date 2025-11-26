"""
QuantumShield - Quantum Vulnerability Scanner
Author: Ndeleh
"""

import os
import subprocess
from typing import List, Dict
from rich import print


def _run_cmd(cmd: list) -> str:
    """Helper to safely run shell commands and return output as string."""
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        return out.decode(errors="ignore")
    except Exception:
        return ""


def scan_ssh_host_keys() -> List[Dict]:
    """
    Scan common SSH host keys for RSA/ECDSA usage.
    """
    ssh_dir = "/etc/ssh"
    findings = []

    if not os.path.isdir(ssh_dir):
        return findings

    for fname in os.listdir(ssh_dir):
        if fname.startswith("ssh_host_") and fname.endswith(".pub"):
            path = os.path.join(ssh_dir, fname)
            out = _run_cmd(["ssh-keygen", "-lf", path])
            algo = "UNKNOWN"

            if "rsa" in out.lower():
                algo = "RSA"
            elif "ecdsa" in out.lower():
                algo = "ECDSA"
            elif "ed25519" in out.lower():
                algo = "ED25519"

            findings.append({
                "component": "SSH Host Key",
                "file": path,
                "algorithm": algo,
                "raw": out.strip()
            })

    return findings


def scan_ssh_config_files() -> List[Dict]:
    """
    Look for RSA/ECDSA references in SSH config files.
    """
    configs = [
        "/etc/ssh/sshd_config",
        "/etc/ssh/ssh_config",
    ]

    findings = []
    for cfg in configs:
        if not os.path.isfile(cfg):
            continue
        try:
            with open(cfg, "r", errors="ignore") as f:
                text = f.read()
        except Exception:
            continue

        lower = text.lower()
        if "rsa" in lower or "ecdsa" in lower:
            findings.append({
                "component": "SSH Config",
                "file": cfg,
                "contains_rsa": "rsa" in lower,
                "contains_ecdsa": "ecdsa" in lower
            })

    return findings


def scan_cert_files(cert_paths: List[str]) -> List[Dict]:
    """
    Use openssl to inspect certificate algorithms in given paths.
    """
    findings = []

    for path in cert_paths:
        if not os.path.isfile(path):
            continue

        out = _run_cmd(["openssl", "x509", "-in", path, "-text", "-noout"])
        if not out:
            continue

        algo = "UNKNOWN"
        sig_algo = "UNKNOWN"

        for line in out.splitlines():
            line = line.strip()
            if line.startswith("Public Key Algorithm:"):
                algo = line.split(":", 1)[1].strip()
            if "Signature Algorithm:" in line:
                sig_algo = line.split(":", 1)[1].strip()

        findings.append({
            "component": "X.509 Certificate",
            "file": path,
            "public_key_algorithm": algo,
            "signature_algorithm": sig_algo
        })

    return findings


def scan_generic_config_files(root="/etc") -> List[Dict]:
    """
    Grep through /etc for RSA/ECDSA mentions as a rough heuristic.
    """
    findings = []

    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            fpath = os.path.join(dirpath, fname)

            # skip binary-ish files by extension
            if any(fpath.endswith(ext) for ext in [".so", ".gz", ".png", ".jpg", ".jpeg"]):
                continue

            try:
                with open(fpath, "r", errors="ignore") as f:
                    text = f.read()
            except Exception:
                continue

            lower = text.lower()
            if "rsa" in lower or "ecdsa" in lower:
                findings.append({
                    "component": "Config File",
                    "file": fpath,
                    "contains_rsa": "rsa" in lower,
                    "contains_ecdsa": "ecdsa" in lower
                })

    return findings


def run_all_scans() -> List[Dict]:
    """
    Run all scanner modules and merge results into a single list.
    """
    print("[bold cyan]Running QuantumShield scans...[/bold cyan]")
    findings = []

    findings.extend(scan_ssh_host_keys())
    findings.extend(scan_ssh_config_files())

    # you can add specific cert locations here if you have them
    cert_candidates = [
        "/etc/ssl/certs/ssl-cert-snakeoil.pem",  # common Debian test cert
    ]
    findings.extend(scan_cert_files(cert_candidates))

    findings.extend(scan_generic_config_files("/etc"))

    print(f"[green]Scan complete. {len(findings)} potential crypto items found.[/green]")
    return findings
