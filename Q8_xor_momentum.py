import numpy as np

def sig(x): return 1/(1+np.exp(-x))
def d_sig(x): return x*(1-x)

X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0],[1],[1],[0]]) # XOR target

# Initial weights and momentum variables
w1, w2 = np.random.randn(2,2), np.random.randn(2,1)
v1, v2 = np.zeros_like(w1), np.zeros_like(w2)
alpha, lr = 0.9, 0.1 # Momentum factor and learning rate

print("Training XOR with Momentum...")
for i in range(20000):
    l1 = sig(np.dot(X, w1))
    l2 = sig(np.dot(l1, w2))
    
    l2_delta = (y - l2) * d_sig(l2)
    l1_delta = l2_delta.dot(w2.T) * d_sig(l1)
    
    # Update with Momentum: v = alpha*v + lr*gradient
    v2 = alpha * v2 + l1.T.dot(l2_delta) * lr
    v1 = alpha * v1 + X.T.dot(l1_delta) * lr
    w2 += v2
    w1 += v1

for x in X:
    out = sig(np.dot(sig(np.dot(x, w1)), w2))
    print(f"Input:{x} Output:{out[0]:.4f} Prediction:{int(out[0]>0.5)}")
