import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

#load csv into dataframe
df = pd.read_csv("CarSharing.csv")

# Convert timestamp to pandas datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

#Filter for 2017
df_2017 = df[df['timestamp'].dt.year == 2017]

#Using only the temp column 
temp_2017 = df_2017[['temp']]

#Hierarchial Clustering 
k = 12 
Hclustering = AgglomerativeClustering(n_clusters=k, linkage='average')
Hclustering.fit(temp_2017)
silhouette_AVG = silhouette_score(temp_2017, Hclustering.labels_)
clusters = Hclustering.fit_predict(temp_2017)
print('The average silhouette score is:', silhouette_AVG)
print(clusters)

Z = linkage(temp_2017, 'average')
dendrogram(Z, truncate_mode='lastp', p=k, leaf_rotation=45., leaf_font_size= 15., show_contracted=True)
plt.title('Truncated Hierachical Clustering Dendrogram')
plt.xlabel('Cluster Size')
plt.ylabel('Distance')

plt.show() 
