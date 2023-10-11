from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import sys

# Sample documents
document1 = sys.argv[1]
document2 = sys.argv[2]

# Create CountVectorizer object to convert text to tokens
vectorizer = CountVectorizer().fit_transform([document1, document2])

# Compute cosine similarity
cosine_similarities = cosine_similarity(vectorizer)

# Cosine similarity matrix
print("Cosine Similarity Matrix:")
print(cosine_similarities)

# Extract cosine similarity score between document1 and document2
similarity_score = cosine_similarities[0, 1]
print("\nCosine Similarity Score between training distribution and generated data distribution:", similarity_score)
