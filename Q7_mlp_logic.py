# Question 7: Write a program to implement MultiLayer Perceptron model
# (i) To implement AND
# (ii) To implement OR

import numpy as np

# Sigmoid and its derivative
def sig(x): return 1/(1+np.exp(-x))
def d_sig(x): return x*(1-x)

# Training Data
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y_and = np.array([[0],[0],[0],[1]])
y_or = np.array([[0],[1],[1],[1]])

def train_gate(X, y, name):
    w1 = np.random.randn(2, 2)
    w2 = np.random.randn(2, 1)
    for _ in range(10000):
        # Forward
        l1 = sig(np.dot(X, w1))
        l2 = sig(np.dot(l1, w2))
        # Backward
        l2_err = y - l2
        l2_delta = l2_err * d_sig(l2)
        l1_err = l2_delta.dot(w2.T)
        l1_delta = l1_err * d_sig(l1)
        # Update
        w2 += l1.T.dot(l2_delta) * 0.1
        w1 += X.T.dot(l1_delta) * 0.1
    
    print(f"\n{name} Results:")
    for i in range(4):
        pred = sig(np.dot(sig(np.dot(X[i], w1)), w2))
        print(f"{X[i]} -> {pred[0]:.4f} (Round: {int(pred[0]>0.5)})")

train_gate(X, y_and, "AND Gate")
train_gate(X, y_or, "OR Gate")
