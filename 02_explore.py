import fitsio
d = fitsio.read("data/LRG_NGC_clustering.dat.fits")
print(d.dtype.names)
print(len(d))
print(d["Z"].min(), d["Z"].max())

r = fitsio.read("data/LRG_NGC_0_clustering.ran.fits")
print(r.dtype.names)
print(len(r))
print(r["Z"].min(), r["Z"].max())

import numpy as np
w = d["WEIGHT_COMP"] * d["WEIGHT_SYS"] * d["WEIGHT_ZFAIL"]
r = d["WEIGHT"] / w
print(np.unique(np.round(r, 4))[:20])
print(np.median(r), r.min(), r.max())

print(np.unique(d["NTILE"]))

for n in np.unique(d["NTILE"]):
    print(n, np.median(r[d["NTILE"] == n]))

from cosmoprimo.fiducial import DESI
cosmo = DESI(engine='camb')
print(cosmo.Omega0_m, cosmo.h, cosmo.Omega0_b, cosmo.n_s, cosmo.sigma8_m)