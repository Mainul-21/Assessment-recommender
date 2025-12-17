from recommender import AssessmentRecommender

engine = AssessmentRecommender("data/shl_catalogue.csv")

job_description = """
Software Engineer role requiring Python programming,
logical reasoning and problem solving skills.
"""

recommendations = engine.recommend(job_description)

print("Recommended Assessments:\n")
for _, row in recommendations.iterrows():
    print(f"{row['assessment_name']} (score: {round(row['score'], 3)})")
