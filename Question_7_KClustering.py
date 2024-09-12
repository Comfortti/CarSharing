import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#load csv into dataframe
df = pd.read_csv("CarSharing.csv")

# Convert timestamp to pandas datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

#Filter for 2017
df_2017 = df[df['timestamp'].dt.year == 2017]

#Using only the temp column 
temp_2017 = df_2017[['temp']]

#K-Means Clustering with 2 Clusters 
k = 12
kmeans = KMeans(n_clusters=k)
kmeans.fit(temp_2017)
df_2017['kmeans_cluster'] = kmeans.labels_

# Output the clusters
print('K-Means Clusters:')
print(df_2017[['timestamp','temp', 'kmeans_cluster']])

#Visualise the Clustering 
plt.figure(figsize=(10, 6))
plt.scatter(df_2017['timestamp'], df_2017['temp'], c=df_2017['kmeans_cluster'], cmap='gnuplot')
plt.title('K-Means Clustering of Temperature Data in 2017 From CarSharing')
plt.xlabel('Dates in 2017')
plt.ylabel('Temperature (Celsius)')
plt.colorbar(label='Cluster')
plt.show()

# Get the count of data points in each cluster
clusters = kmeans.fit_predict(temp_2017)
cluster_counts = pd.Series(clusters).value_counts().sort_index()
print('K-Means Clusters:')
print(cluster_counts)