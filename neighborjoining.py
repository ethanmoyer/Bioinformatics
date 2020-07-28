import numpy as np


# Accept d as numpy array, return d_ as numpy array
def neighbor_joining_matrix(d):
	
	d_ = np.empty((4,4))
	d_[:] = 0
	for i in range(n):
		for j in range(n):
			if d[i, j] != 0:
				d_[i, j] = (n - 2) * d[i, j] - total_distance[i] - total_distance[j]

	return d_

D = [[0, 13, 21, 22], [13, 0, 12, 13], [21, 12, 0, 13], [22, 13, 13, 0]]
d = np.array(D)
total_distance = np.sum(d, axis=1)

n = d.shape[0]

print(d)
d_= neighbor_joining_matrix(d)
print(d_)

delta = np.empty((4,4))
delta[:] = 0

ind = np.unravel_index(np.argmin(d_, axis=None), d_.shape)
i = ind[0]
j = ind[1]
delta[i, j] = (total_distance[i] - total_distance[j]) / (n - 2)

limblength = np.empty((1,4,))
limblength[:] = 0

limblength[0, i] = (d[i, j] + delta[i, j]) / 2
limblength[0, j] = (d[i, j] - delta[i, j]) / 2

d__ = np.delete(np.delete(d, i, 0), i, 1)
d__ = np.delete(np.delete(d__, j, 0), j, 1)

c = np.zeros((n - 2, 1))
r = np.zeros((1, n - 1))
d__ = np.hstack((c, d__))
d__ = np.vstack((r, d__))

for i_ in range(n - 2):
	for j_ in range(1, n - 1):
		for k_ in range(1, n - 1):
	d__[1 + i_, 0] = (d[i_, k_] + d[j_, k_] - d[i_, j_]) / 2

for j_ in range(n - 1):
	d__[0, j_] = 