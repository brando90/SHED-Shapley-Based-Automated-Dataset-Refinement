import os
import numpy as np

# Set environment variables to control threading for computational efficiency
os.environ["OPENBLAS_NUM_THREADS"] = "64"
os.environ["n_jobs"] = "64"
os.environ["OMP_NUM_THREADS"] = "64"

import json
import sys
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

def main():
    print(f"--- Running (within python): {os.path.abspath(__file__)}")
    
    # Get data path and number of clusters from command-line arguments
    data_path = str(sys.argv[1])
    num_clusters = int(sys.argv[2])
    print(f'{data_path=}')
    print(f'{num_clusters=}')
    
    # Initialize the sentence transformer model for embedding generation
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    print(f'{embedder.device=}')
    
    # Load data from the JSON file and extract the text corpus
    corpus = []
    with open(data_path) as f:
        json_object = json.load(f)
        for i in json_object:
            corpus.append(str(i))
    
    # Generate embeddings for the corpus
    corpus_embeddings = embedder.encode(corpus, show_progress_bar=True)
    
    # Perform KMeans clustering on the embeddings
    clustering_model = KMeans(n_clusters=num_clusters)
    clustering_model.fit(corpus_embeddings)
    cluster_assignment = clustering_model.labels_
    
    # Group sentences by their assigned clusters
    clustered_sentences = [[] for _ in range(num_clusters)]
    for sentence_id, cluster_id in enumerate(cluster_assignment):
        clustered_sentences[cluster_id].append(corpus[sentence_id])
    
    # Save sentences of each cluster to separate text files
    for i, cluster in enumerate(clustered_sentences):
        with open(f"./workspace/cluster_{num_clusters}_{i}.txt", 'a', encoding="utf-8") as file:
            for sentence in cluster:
                file.write(sentence + "\n")
    
    # Find the sentences closest to each cluster center and save them
    closest, _ = pairwise_distances_argmin_min(clustering_model.cluster_centers_, corpus_embeddings)
    with open(f"./workspace/cluster_center_{num_clusters}.txt", 'a', encoding="utf-8") as file:
        for index in closest:
            file.write(corpus[index] + "\n")

if __name__ == "__main__":
    main()
