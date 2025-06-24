def evaluate_claim(text):
    import hashlib
    hash_val = int(hashlib.sha256(text.encode('utf-8')).hexdigest(), 16)
    base = (hash_val % 1000) / 1000
    coherence = round(0.75 + 0.2 * base, 2)
    scalability = round(0.75 + 0.2 * ((base * 997) % 1), 2)
    composite = round((coherence + scalability) / 2, 2)
    explanation = "This simulated explanation shows how resonance is evaluated for coherence, scalability, and systemic truth."
    return {
        "coherence_score": coherence,
        "scalability_score": scalability,
        "composite_score": composite,
        "explanation": explanation
    }
