import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('CarSharing.csv')

# Extract 'temp' data
temp_data = df[['temp']]

# Perform K-Means clustering
k = 2
kmeans = KMeans(n_clusters=k)
clusters = kmeans.fit_predict(temp_data)

# Get the count of data points in each cluster
cluster_counts = pd.Series(clusters).value_counts().sort_index()

# Visualize the clustering
plt.figure(figsize=(10, 6))
plt.scatter(temp_data, [0] * len(temp_data), c=clusters, cmap='viridis')
plt.title('K-Means Clustering of Temperature Data')
plt.xlabel('Temperature')
plt.yticks([])  # Hide y-axis ticks
plt.colorbar(label='Cluster')

# Annotate the plot with cluster counts above the clusters
for i, count in enumerate(cluster_counts):
    plt.text(temp_data[clusters == i].mean(), 0.02, f'{count}', fontsize=12,
             verticalalignment='bottom', horizontalalignment='center', color='white')

plt.show()

# Print cluster assignments and counts
print('K-Means Clusters:')
print(cluster_counts)