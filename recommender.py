import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class AssessmentRecommender:
    def __init__(self, catalogue_path):
        self.data = pd.read_csv(catalogue_path)

        self.data["text"] = (
            self.data["description"].fillna("") + " " +
            self.data["skills"].fillna("") + " " +
            self.data["job_level"].fillna("")
        )

        # Using a lightweight pretrained model for semantic similarity
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.embeddings = self.model.encode(self.data["text"].tolist())

    def recommend(self, job_description, top_k=3):
        if not job_description:
            return []

        job_embedding = self.model.encode([job_description])
        scores = cosine_similarity(job_embedding, self.embeddings)[0]

        self.data["score"] = scores

        results = self.data.sort_values(
            by="score", ascending=False
        ).head(top_k)

        return results[["assessment_name", "score"]]
