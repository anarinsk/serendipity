#%%
import numpy as np 
import numpy.linalg as LA

# %%
#P = [[0.9, 0.5], [0.1, 0.5]]
P = [[0.9, 0.15, 0.25], [0.075, 0.8, 0.25], [0.025, 0.05, 0.5]]
# %%
eigvals, eigvecs = LA.eig(P)
np.where(max(eigvals))
# %%
eigvecs[:, 0] / eigvecs[:, 0].sum()

# %%
def get_limiting_markov(P): 
    eigvals, eigvecs = LA.eig(P)
    idx = np.where(max(eigvals))
    return eigvecs[:, 0] / eigvecs[:, 0].sum()

# %%
get_limiting_markov(P)

# %%
