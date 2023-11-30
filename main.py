from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics.cluster import normalized_mutual_info_score, adjusted_rand_score
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def dim_red(mat, p, method):
    if method=='ACP':
        pca = PCA(n_components=p)
        pca_result = pca.fit_transform(mat)
    elif method=='AFC':
        red_mat = mat[:,:p]
    elif method=='UMAP':
        umap_model = UMAP(n_components=p)
        red_mat = umap_model.fit_transform(mat)    
    else:
        raise Exception("Please select one of the three methods : APC, AFC, UMAP")
    return red_mat


def clust(mat, k):
    kmeans = KMeans(n_clusters=k, random_state=42)
    pred = kmeans.fit_predict(mat)
    return pred

# import data
data = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
corpus = data.data[:2000]
labels = data.target[:2000]
k = len(set(labels))

# embedding
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
embeddings = model.encode(corpus)

# Perform dimensionality reduction and clustering for each method
methods = ['ACP', 'AFC', 'UMAP']
for method in methods:
    # Perform dimensionality reduction
    red_emb = dim_red(embeddings, 20, method)

    # Perform clustering
    pred = clust(red_emb, k)

    # Evaluate clustering results
    nmi_score = normalized_mutual_info_score(pred, labels)
    ari_score = adjusted_rand_score(pred, labels)

    # Print results
    print(f'Method: {method}\nNMI: {nmi_score:.2f} \nARI: {ari_score:.2f}\n')from sklearn.datasets import fetch_20newsgroups