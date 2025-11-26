"""
QuantumShield - Quantum Risk Analyzer
Author: Ndeleh
"""

from typing import List, Dict


def _risk_from_algorithm(algo: str) -> str:
    """
    Simple rule-based risk logic based on algorithm type.
    """
    if not algo:
        return "Unknown"

    a = algo.lower()

    # PQC is what we want eventually
    if "dilithium" in a or "falcon" in a or "kyber" in a:
        return "Low"

    # ED25519 is not broken by quantum the way RSA/ECC are, but future risk exists
    if "ed25519" in a:
        return "Medium"

    # RSA and ECC are the main quantum targets
    if "rsa" in a or "ecdsa" in a or "ecc" in a:
        return "High"

    return "Medium"


def _risk_from_component(component: str) -> str:
    if "Certificate" in component:
        return "High"
    if "SSH Host Key" in component:
        return "High"
    if "Config File" in component:
        return "Medium"
    return "Medium"


def analyze_findings(findings: List[Dict]) -> List[Dict]:
    """
    Input: scanner findings
    Output: extended findings with risk_score & explanation
    """
    analyzed = []

    for f in findings:
        algo = f.get("algorithm") or f.get("public_key_algorithm") or ""
        component = f.get("component", "Unknown")

        algo_risk = _risk_from_algorithm(algo)
        comp_risk = _risk_from_component(component)

        # combine risk (simple rule: worst wins)
        combined_risk = "Medium"
        if "High" in (algo_risk, comp_risk):
            combined_risk = "High"
        elif "Unknown" in (algo_risk, comp_risk):
            combined_risk = "Unknown"
        else:
            combined_risk = "Medium"

        explanation = []

        if "rsa" in algo.lower():
            explanation.append("Uses RSA, which is vulnerable to Shor's quantum algorithm.")
        if "ecdsa" in algo.lower() or "ecc" in algo.lower():
            explanation.append("Uses ECC, which is also vulnerable to Shor's quantum algorithm.")
        if "ed25519" in algo.lower():
            explanation.append("Uses Ed25519; not directly broken by current quantum attacks but long-term risk remains.")
        if not explanation:
            explanation.append("Potential cryptographic material found; evaluate for quantum safety.")

        new_item = {
            **f,
            "algo_risk": algo_risk,
            "component_risk": comp_risk,
            "combined_risk": combined_risk,
            "explanation": " ".join(explanation)
        }

        analyzed.append(new_item)

    return analyzed
