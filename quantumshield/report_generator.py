"""
QuantumShield - Report Generator
Author: Ndeleh
"""

from datetime import datetime
from typing import List, Dict


def generate_markdown_report(analyzed_findings: List[Dict]) -> str:
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    report = []
    report.append("# QuantumShield Security Report")
    report.append("")
    report.append(f"**Generated:** {now}")
    report.append("")
    report.append("Author: **Ndeleh**")
    report.append("")
    report.append("## Overview")
    report.append("")
    report.append(
        "This report summarizes cryptographic assets discovered on the system "
        "and evaluates their risk in the context of future quantum computers."
    )
    report.append("")

    # summary stats
    total = len(analyzed_findings)
    high = sum(1 for f in analyzed_findings if f.get("combined_risk") == "High")
    medium = sum(1 for f in analyzed_findings if f.get("combined_risk") == "Medium")
    low = sum(1 for f in analyzed_findings if f.get("combined_risk") == "Low")

    report.append("## Summary of Findings")
    report.append("")
    report.append(f"- Total cryptographic items found: **{total}**")
    report.append(f"- High quantum risk: **{high}**")
    report.append(f"- Medium quantum risk: **{medium}**")
    report.append(f"- Low quantum risk: **{low}**")
    report.append("")

    # detailed section
    report.append("## Detailed Findings")
    report.append("")

    if not analyzed_findings:
        report.append("_No cryptographic items were detected._")
        return "\n".join(report)

    for idx, f in enumerate(analyzed_findings, start=1):
        report.append(f"### Finding {idx}")
        report.append("")
        report.append(f"- **Component:** {f.get('component')}")
        report.append(f"- **File:** `{f.get('file', 'N/A')}`")
        algo = (
            f.get("algorithm")
            or f.get("public_key_algorithm")
            or "Unknown"
        )
        report.append(f"- **Algorithm:** {algo}")
        report.append(f"- **Combined Quantum Risk:** **{f.get('combined_risk')}**")
        report.append("")
        report.append(f"**Explanation:** {f.get('explanation')}")
        report.append("")
        report.append("---")
        report.append("")

    report.append("## Recommended Next Steps")
    report.append("")
    report.append("- Prioritize migration away from RSA and ECC towards post-quantum algorithms.")
    report.append("- Inventory all externally-facing services using vulnerable algorithms.")
    report.append("- Follow NIST post-quantum cryptography guidance when selecting replacements.")
    report.append("")

    return "\n".join(report)
