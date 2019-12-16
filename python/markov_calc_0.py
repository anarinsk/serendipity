#%%
import numpy as np 
import numpy.linalg as LA
# %%
#P = [[0.9, 0.5], [0.1, 0.5]]
P = [[0.9, 0.15, 0.25], [0.075, 0.8, 0.25], [0.025, 0.05, 0.5]]
# %%
def get_limiting_markov(mat): 
    eigvals, eigvecs = LA.eig(mat)
    idx = np.where(eigvals == 1)
    sdist = eigvecs[:, idx] / eigvecs[:, idx].sum()
    return print(np.ndarray.flatten(sdist)) 
# %%
get_limiting_markov(P)
# %%
P = [[1.0, 0.0, 0.0],
     [0.1, 0.8, 0.1],
     [0.0, 0.2, 0.8]]
np.matmul(P, P)
# %%
P = [[0, 1, 0],
     [0, 0, 1],
     [1, 0, 0]]
np.matmul(P,P)
# %%
P = np.array([[0.4, 0.6],
              [0.2, 0.8]])
ψ = (0.25, 0.75)
ψ @ P
evl, evc = LA.eig(P.T)
evl
np.where(evl == 1)
#get_limiting_markov(P.T)
# %%
evc[:,1]/evc[:,1].sum()
get_limiting_markov(P.T)
# %%
