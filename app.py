import streamlit as st
from recommender import AssessmentRecommender

st.set_page_config(page_title="Assessment Recommendation Engine")

st.title("Assessment Recommendation Engine")

st.write(
    "Enter a job description or query below to get recommended assessments."
)

query = st.text_area("Job Description / Query")

if st.button("Recommend"):
    if query.strip() == "":
        st.warning("Please enter a query.")
    else:
        recommender = AssessmentRecommender(
            data_path="data/shl_catalogue.csv"
        )
        results = recommender.recommend(query)

        st.subheader("Recommended Assessments")
        for name, score in results:
            st.write(f"**{name}** — Similarity: {score:.2f}")
