import os
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class AssessmentRecommender:
    def __init__(self, data_path=None):
        if data_path is None:
            # Use default path relative to this file
            data_path = os.path.join(os.path.dirname(__file__), "data/shl_catalogue.csv")
        
        # Check if file exists
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"CSV file not found: {data_path}")
        
        self.df = pd.read_csv(data_path)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = self.model.encode(self.df['description'].tolist())
