# Question 2: Given following relations:
# R1 = "x is relevant to y", R2 = "y is relevant to z"
# Where X = {1, 2, 3}, Y = {a, b, c, d}, Z = {One, two}
# Assuming appropriate values for R1 and R2, Calculate the max-min and 
# max Product composition for (3, one).

import numpy as np

X = [1,2,3]
Y = ['a','b','c','d']
Z = ['One', 'two']

R1 = np.array([
    [0.2,0.6,0.8,0.4],
    [0.9,0.1,0.5,0.7],
    [0.3,0.4,0.6,0.9]
])

R2 = np.array([
    [0.7,0.2],
    [0.5,0.0],
    [0.6,0.3],
    [0.8,0.4]
])

i = X.index(3)
k = Z.index('One')

max_min = np.max(np.minimum(R1[i, :], R2[:, k]))

max_prod = np.max(np.round(R1[i, :]*R2[:, k] ,2))

print("Max-min composition (3,One):", max_min)
print("Max_product composition (3, One):", max_prod)
