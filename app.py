import streamlit as st
from recommender import AssessmentRecommender
import os

csv_path = os.path.join(os.path.dirname(__file__), "data", "shl_catalogue.csv")
recommender = AssessmentRecommender(data_path=csv_path)

# Check if a query parameter exists
query_params = st.experimental_get_query_params()
if "query" in query_params:
    query = query_params["query"][0]
    results = recommender.recommend(query)

    # Return JSON
    st.write([{"name": name, "score": float(score)} for name, score in results])
else:
    # UI Interface
    st.title("Assessment Recommendation Engine")
    st.write("Enter a job description or query below to get recommended assessments.")

    input_text = st.text_area("Job Description / Query")
    if st.button("Recommend"):
        if input_text.strip() == "":
            st.warning("Please enter a query.")
        else:
            results = recommender.recommend(input_text)
            st.subheader("Recommended Assessments")
            for name, score in results:
                st.write(f"**{name}** — Similarity: {score:.2f}")
