from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics.cluster import normalized_mutual_info_score, adjusted_rand_score
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from umap import UMAP
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def dim_red(mat, p, method):
    if method=='ACP':
        pca = PCA(n_components=p)
        red_mat = pca.fit_transform(mat)
    elif method=='TSNE':
        tsne = TSNE(n_components=p)
        red_mat = tsne.fit_transform(embeddings)
    elif method=='UMAP':
        umap_model = UMAP(n_components=p)
        red_mat = umap_model.fit_transform(mat)    
    else:
        raise Exception("Please select one of the three methods : ACP, TSNE, UMAP")
    return red_mat


def clust(mat, k):
    kmeans = KMeans(n_clusters=k, random_state=42)
    pred = kmeans.fit_predict(mat)
    return pred

# import data
# data = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
# all_indices = np.arange(len(data.data))
# np.random.shuffle(all_indices)
# selected_indices = all_indices[:2000]

# corpus = [data.data[i] for i in selected_indices]
# labels = [data.target[i] for i in selected_indices]
# train = pd.DataFrame({'Document': corpus, 'Category': labels})  

data = pd.read_csv('data.csv')

k = len(set(labels))

# embedding
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
embeddings = model.encode(corpus)

# Perform dimensionality reduction and clustering for each method
methods = ['ACP', 'TSNE', 'UMAP']
for method in methods:
    # Perform dimensionality reduction
    red_emb = dim_red(embeddings, 3, method)

    # Perform clustering
    pred = clust(red_emb, 20)

    # Evaluate clustering results
    nmi_score = normalized_mutual_info_score(pred, labels)
    ari_score = adjusted_rand_score(pred, labels)

    # Print results
    print(f'Method: {method}\nNMI: {nmi_score:.2f} \nARI: {ari_score:.2f}\n')
