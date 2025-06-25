
import streamlit as st
from resonance_engine import evaluate_resonance

st.set_page_config(page_title="Truth Resonance Evaluator", layout="centered")
st.title("Truth Resonance Evaluator")
st.caption("Evaluate the coherence, scalability, and composite resonance of any idea, quote, or claim.")

user_input = st.text_area("Enter a claim or quote to evaluate:")

if st.button("Evaluate"):
    if not user_input.strip():
        st.warning("Please enter a statement to evaluate.")
    else:
        result = evaluate_resonance(user_input)

        st.subheader("📊 Truth Resonance Scores")
        st.write(f"**Coherence Score (TSI)**: {result['coherence']}")
        st.write(f"**Scalability Score (VDI)**: {result['scalability']}")
        st.write(f"**Composite Truth Score (TRE)**: {result['composite']}")

        st.subheader("🧠 Explanation")
        st.markdown(result["explanation"])
