import numpy as np
import astropy, fitsio, healpy, camb, emcee, corner
from sklearn.cluster import KMeans
import cosmoprimo, pycorr
from Corrfunc.theory.DD import DD

rng = np.random.default_rng(0)
x, y, z = rng.random((3, 1000)) * 100.0
res = DD(1, 1, np.linspace(1, 10, 5), x, y, z, periodic=False)

print("all imports fine")
print("corrfunc pair counts:", res["npairs"])
