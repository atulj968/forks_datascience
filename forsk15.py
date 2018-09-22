#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:58:37 2018

@author: atuljain
"""

import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('deliveryfleet.csv')
features = dataset.iloc[:, [1,2]].values

from sklearn.cluster import KMeans
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters  = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title['The elbow method']
plt.xlabel['Number of cluster']
plt.yalbel['WCSS']
plt.show()

kmeans = KMeans(n_clusters = 2, init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(features)

plt.scatter(features[y_kmeans == 0,0], features[y_kmeans == 0,1],s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(features[y_kmeans == 1,0], features[y_kmeans == 1,1],s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(features[y_kmeans == 2,0], features[y_kmeans == 2,1], s=100, c = 'green', label = 'Cluster 3')
plt.scatter(features[y_kmeans == 3,0], features[y_kmeans == 3,1],s = 100, c = 'cyan', label = 'cluster 4')
plt.scatter(features[y_kmeans == 4,0], features[y_kmeans == 4,1],s = 100, c = 'pink', label = 'Cluster 5')
plt.scattre(kmeans.cluster_centres_[:,0], kmeans.cluster_centers_[:,1], s = 300, c = 'yellow', labels = 'Centroids')
plt.title('Cluster of customers')
plt.xlabel('Distance')
plt.ylabel('speed')
plt.legend()
plt.show()
