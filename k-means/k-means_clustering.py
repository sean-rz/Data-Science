'''
Unsupervised learning means that there is no outcome to be predicted, and just tries to find patterns in the data. 
K-means randomly assigns each observation to a cluster, and finds the centroid of each cluster. 
Then, iterates through two steps: 1) Reassign data points to the cluster whose centroid is the closest. 
2) Calculate new centroid of each cluster. The within cluster variation is calculated as the sum of the 
euclidean distance between the data points and their respective cluster centroids
'''
import matplotlib as mpl 
import matplotlib.pyplot as plt
import seaborn as sns

mpl.rcParams['patch.force_edgecolor'] = True # gridlines between bins
sns.set_style('darkgrid')

# create data

from sklearn.datasets import make_blobs

data = make_blobs(n_samples=200, n_features=2, centers=4, cluster_std=1.8, random_state=101)

print(data[0].shape)
print(data[1])

# visualize data
plt.scatter(data[0][:,0], data[0][:,1], c=data[1], cmap='rainbow')

# creating clusters
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4)
kmeans.fit(data[0])

print('Centroids:\n', kmeans.cluster_centers_)
print(kmeans.labels_)


fig, (ax1,ax2) = plt.subplots(1, 2, sharey=True, figsize=(10,6))
ax1.set_title('K Means')
ax1.scatter(data[0][:,0],data[0][:,1], c=kmeans.labels_, cmap='rainbow')
ax2.set_title("Original")
ax2.scatter(data[0][:,0],data[0][:,1], c=data[1], cmap='rainbow')
plt.show()
