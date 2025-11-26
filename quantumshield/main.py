"""
QuantumShield - Main Entry Point
Author: Ndeleh
"""

from rich import print
from .scanner import run_all_scans
from .analyzer import analyze_findings
from .report_generator import generate_markdown_report
from .utils import save_report


def main():
    print("[bold magenta]QuantumShield - Quantum Vulnerability Scanner[/bold magenta]")
    print("Author: [bold]Ndeleh[/bold]\n")

    # 1. Run scanner
    raw_findings = run_all_scans()

    # 2. Analyze risk
    analyzed = analyze_findings(raw_findings)

    # 3. Generate report text
    report_md = generate_markdown_report(analyzed)

    # 4. Save report
    out_path = save_report(report_md)
    print(f"\n[bold green]Report generated:[/bold green] {out_path}")


if __name__ == "__main__":
    main()
