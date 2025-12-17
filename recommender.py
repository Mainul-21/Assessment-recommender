import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class AssessmentRecommender:
    def __init__(self, data_path="data/shl_catalogue.csv"):
        # Load CSV
        self.df = pd.read_csv(data_path)

        # Check columns exist
        if 'name' not in self.df.columns or 'description' not in self.df.columns:
            raise ValueError("CSV must contain 'name' and 'description' columns")

        # Load model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

        # Precompute embeddings
        self.embeddings = self.model.encode(self.df['description'].tolist())

    def recommend(self, query, top_k=5):
        if not isinstance(query, str) or query.strip() == "":
            return []

        query_emb = self.model.encode([query])
        scores = cosine_similarity([query_emb[0]], self.embeddings)[0]
        self.df['score'] = scores
        top_results = self.df.sort_values('score', ascending=False).head(top_k)
        return list(zip(top_results['name'], top_results['score']))
