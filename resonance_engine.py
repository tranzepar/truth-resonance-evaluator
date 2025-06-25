
import re

def evaluate_claim(claim):
    claim = claim.strip()
    tokens = claim.split()
    word_count = len(tokens)

    # Example coherence check: basic punctuation and clarity
    coherence_score = 0.9 if re.search(r'[.?!]$', claim) and word_count > 3 else 0.5

    # Example scalability check: generality, not overly specific or personal
    lower_claim = claim.lower()
    if any(word in lower_claim for word in ["always", "everyone", "all", "universal", "truth", "love", "freedom"]):
        scalability_score = 0.9
    elif any(word in lower_claim for word in ["I", "me", "my", "mine", "today", "this"]):
        scalability_score = 0.4
    else:
        scalability_score = 0.7

    # Value Dignity Index (VDI): does it uphold human flourishing language?
    if any(word in lower_claim for word in ["love", "peace", "dignity", "justice", "kindness"]):
        vdi_score = 0.9
    elif any(word in lower_claim for word in ["hate", "kill", "worthless", "evil"]):
        vdi_score = 0.3
    else:
        vdi_score = 0.6

    # Truth Resonance Estimate (TRE): composite based on weights
    composite_score = round((coherence_score * 0.3 + scalability_score * 0.4 + vdi_score * 0.3), 2)

    explanation = (
        f"Coherence: {coherence_score:.2f} — based on structure and clarity.\n"
        f"Scalability: {scalability_score:.2f} — based on general vs. personal applicability.\n"
        f"VDI: {vdi_score:.2f} — based on language promoting dignity or harm.\n"
        f"Composite TRE: {composite_score:.2f} — weighted sum of the above metrics."
    )

    return {
        "coherence": round(coherence_score, 2),
        "scalability": round(scalability_score, 2),
        "vdi": round(vdi_score, 2),
        "tre": composite_score,
        "explanation": explanation
    }
