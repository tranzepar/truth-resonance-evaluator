
import random

def score_coherence(text):
    return round(0.6 + 0.4 * random.random(), 2)

def score_scalability(text):
    return round(0.5 + 0.5 * random.random(), 2)

def score_composite(coh, scal):
    return round((coh * 0.6 + scal * 0.4), 2)

def generate_explanation(text, coh, scal, comp):
    explanation = f"""
The statement "{text}" was evaluated for its resonance.

• Coherence Score ({coh}): This reflects how internally consistent and logically structured the statement is.
• Scalability Score ({scal}): This measures how well the idea holds across different contexts, communities, or scales of implementation.
• Composite Truth Score ({comp}): A weighted blend prioritizing coherence (60%) and scalability (40%).

Interpretation:
- The statement appears {'internally sound' if coh > 0.75 else 'somewhat fragmented'}.
- Its applicability {'extends broadly' if scal > 0.75 else 'may be limited to certain contexts'}.
- Overall, this claim {'resonates with systemic insight' if comp > 0.8 else 'shows room for deeper reflection'}.
"""
    return explanation.strip()

def evaluate_statement(text):
    coh = score_coherence(text)
    scal = score_scalability(text)
    comp = score_composite(coh, scal)
    explanation = generate_explanation(text, coh, scal, comp)
    return {
        "coherence": coh,
        "scalability": scal,
        "composite": comp,
        "explanation": explanation
    }
