
import streamlit as st
from resonance_engine import evaluate_claim

st.set_page_config(page_title="Truth Resonance Evaluator", layout="centered")
st.title("🧭 Truth Resonance Evaluator")
st.write("Evaluate the coherence, scalability, and composite resonance of any idea, quote, or claim.")

user_input = st.text_area("Enter a claim or quote to evaluate:", height=150)

if st.button("Evaluate"):
    if user_input.strip():
        result = evaluate_claim(user_input)
        st.subheader("📊 Truth Resonance Scores")
        st.write(f"**Coherence Score:** {result['coherence']:.2f}")
        st.write(f"**Scalability Score:** {result['scalability']:.2f}")
        st.write(f"**Composite Truth Score:** {result['composite']:.2f}")

        st.subheader("🧠 Explanation")
        st.write(result["explanation"])
    else:
        st.warning("Please enter a statement to evaluate.")
