import streamlit as st
from resonance_engine import evaluate_claim

st.set_page_config(page_title="Truth Resonance Evaluator", layout="centered")
st.title("Truth Resonance Evaluator")
st.markdown("Evaluate the coherence, scalability, and composite resonance of any idea, quote, or claim.")

claim = st.text_area("Enter a claim or quote to evaluate:", height=150)

if st.button("Evaluate Truth Resonance"):
    if claim.strip():
        with st.spinner("Evaluating..."):
            result = evaluate_claim(claim)

        st.success("Evaluation Complete")

        st.subheader("📊 Truth Resonance Scores")
        st.markdown(f"**Coherence Score:** {result['coherence_score']:.2f}")
        st.markdown(f"**Scalability Score:** {result['scalability_score']:.2f}")
        st.markdown(f"**Composite Truth Score:** {result['composite_score']:.2f}")

        st.subheader("🧠 Explanation")
        st.markdown(result['explanation'])
    else:
        st.warning("Please enter a quote or statement to evaluate.")
