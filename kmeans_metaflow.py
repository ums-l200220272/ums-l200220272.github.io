from metaflow import FlowSpec, step
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

class ManyKmeansFlow(FlowSpec):
    """
    Alur untuk melakukan pengelompokan KMeans pada data obrolan grup WhatsApp.
    """

    @step
    def start(self):
        print("Loading cleaned data...")
        # Load the cleaned CSV data
        self.data = pd.read_csv('cleaned_dat3.csv')

        # Combine relevant columns (e.g., assuming 'cleaned_message' contains cleaned text)
        self.text_data = self.data['cleaned_message'].astype(str).fillna('')
        
        print(f"Total cleaned messages: {len(self.text_data)}")
        self.next(self.vectorize)

    @step
    def vectorize(self):
        """
        Convert text data to TF-IDF vectors.
        """
        print("Vectorizing text data using TF-IDF...")
        self.vectorizer = TfidfVectorizer(
            stop_words='english', max_features=5000
        )
        self.vectors = self.vectorizer.fit_transform(self.text_data)

        print(f"TF-IDF matrix shape: {self.vectors.shape}")
        self.next(self.cluster)

    @step
    def cluster(self):
        """
        Clustering with 3, 4, and 5 clusters.
        """
        print("Clustering data...")
        self.results = {}

        for n_clusters in [3, 4, 5]:
            print(f"Running KMeans for {n_clusters} clusters...")
            kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            kmeans.fit(self.vectors)

            # Get top terms per cluster
            order_centroids = kmeans.cluster_centers_.argsort()[:, ::-1]
            terms = np.array(self.vectorizer.get_feature_names_out())

            clusters = []
            for i in range(n_clusters):
                top_terms = terms[order_centroids[i, :3]]  # Top 3 terms
                clusters.append(top_terms.tolist())

            self.results[n_clusters] = clusters

        self.next(self.end)

    @step
    def end(self):
        """
        Display results
        """
        print("Clustering complete! Results:")
        for n_clusters, clusters in self.results.items():
            print(f"\nNumber of clusters: {n_clusters}")
            for i, top_terms in enumerate(clusters):
                print(f"Cluster {i + 1}: {', '.join(top_terms)}")

if __name__ == '__main__':
    ManyKmeansFlow()