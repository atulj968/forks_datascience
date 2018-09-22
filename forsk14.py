#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:01:01 2018

@author: atuljain
"""

import matplotlib.pyplot as plt
import pandas as pd

#importing data set
dataset = pd.read_csv('Mall_Costumers.csv')
features = dataset.iloc[:, [3,4]].values

from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters  = i, init = 'k-means++', random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of cluster')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_cluster = 5, init = 'k-means++', random_state = 0)
y_kmeans = kmeans.fit_predict(features)

plt.scatter(features[y_kmeans == 0,0])
plt.scatter(features[y_kmeans == 1,0], features[y_kmeans == 1,1],s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(features[y_kmeans == 2,0], features[y_kmeans == 2,1], s=100, c = 'green', label = 'Cluster 3')
plt.scatter(features[y_kmeans == 3,0], features[y_kmeans == 3,1],s = 100, c = 'cyan', label = 'cluster 4')
plt.scatter(features[y_kmeans == 4,0], features[y_kmeans == 4,1],s = 100, c = 'pink', label = 'Cluster 5')
plt.scattre(kmeans.cluster_centres_[:,0], kmeans.cluster_centers_[:,1], s = 300, c = 'yellow', labels = 'Centroids')
plt.title('Cluster of customers')
plt.xlabel('Annual income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()
