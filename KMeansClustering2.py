import numpy as np
import random
import pylab

#generate a thousand random numbers
def initialize(N, range_r):
	X = []
	for i in range(N):
		X.append([random.uniform(0, range_r), random.uniform(0, range_r)])
	return X

def clusterred_points(X, mu):
	#create an empty dictionary
	clusters = {}
	#Find the minimum distance between the point and the centeroid
	for i in range(len(X)):
		distances = []
		for e, k in mu.items():
			#print('k = ', k)
			distance = 0
			for j in range(2):
				distance += (X[i][j] - k[j])**2
			distance = distance**(1/2)
			distances.append(distance)
		best_key = distances.index(min(distances))
		try:
			#clusters[best_key].append(X[i].tolist())
			clusters[best_key].append(X[i])
		except KeyError:
			#clusters[best_key] = [X[i].tolist()]
			clusters[best_key] = [X[i]]
	return clusters

def cluster_centers(clusters):
	mu = {}
	for key in clusters:
		meand = np.average(clusters[key], axis = 0)
		try:
			mu[key].append(meand.tolist())
		except KeyError:
			mu[key] = meand.tolist()
	return mu


size_of_array = 100
range_r = 1000
X = initialize(size_of_array, range_r)
ClusterNo = 4

mu = {}
oldmu = {}

for i in range(ClusterNo):
	mu[i] = X[random.randint(0,size_of_array - 1)][:]
	oldmu[i] = X[random.randint(0,size_of_array - 1)][:]

#print('mu = ', mu)
#print('oldmu = ', oldmu)

while(mu!=oldmu):
	oldmu = mu
	clusters = clusterred_points(X, oldmu)
	mu = cluster_centers(clusters)


colours=['r','g','b','k']
for key in clusters:
	x = []
	y = []
	for i in range(len(clusters[key])):
		x.append(clusters[key][i][0])
		y.append(clusters[key][i][1])
	pylab.plot(x, y, str(colours[key%4])+'o', markersize=4)

for key in mu:
	key_x = []
	key_y = []
	key_x.append(mu[key][0])
	key_y.append(mu[key][1])
	pylab.plot(key_x, key_y, str(colours[key%4])+'^', markersize=8)

pylab.axis([0-range_r*0.1, range_r*1.1, 0 - range_r*0.1, range_r*1.1])
pylab.show()