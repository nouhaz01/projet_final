tsne = TSNE(n_components=3)
embedded_data = tsne.fit_transform(embeddings)
