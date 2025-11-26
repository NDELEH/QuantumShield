"""
QuantumShield - Utility Functions
Author: Ndeleh
"""

from pathlib import Path


def save_report(content: str, output_path: str = "quantumshield_report.md") -> str:
    """
    Save markdown report to given path, return path.
    """
    p = Path(output_path)
    p.write_text(content, encoding="utf-8")
    return str(p)
