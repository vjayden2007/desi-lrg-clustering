import numpy as np
import matplotlib.pyplot as plt
import fitsio

data = fitsio.read("data/LRG_NGC_clustering.dat.fits")
cut = data[(data["Z"] > 0.6) & (data["Z"] < 0.8)]
print(len(cut))

RA = cut["RA"]
Dec = cut["DEC"]
plt.figure(figsize=(10, 6))
plt.title("Footprint")
plt.xlabel("Right Ascension")
plt.ylabel("Declination")
plt.scatter(RA, Dec, s=0.05, alpha=0.05, color="r")
plt.gca().set_aspect('equal')
plt.grid(True)
plt.savefig("results/figures/footprint.png", dpi=250)
#
bins = np.linspace(0.4, 1.1, 36)
plt.figure(figsize=(10, 6))
plt.title("Redshift Distribution")
plt.xlabel("Redshift")
plt.ylabel("Number of Galaxies")
plt.hist(data["Z"], bins=bins, label="Z<0.6, 0.8<Z")
plt.hist(cut["Z"], bins=bins, label="0.6<Z<0.8", color="r")
plt.legend()
plt.savefig("results/figures/redshift_distribution.png", dpi=250)
#
wbins = np.linspace(0, 4, 100)
fkpbins = np.linspace(0, 0.3, 100)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
axes[0].set_title("Total weight")
axes[0].set_xlabel("WEIGHT")
axes[0].set_ylabel("Number of galaxies")
axes[1].set_title("FKP weight")
axes[1].set_xlabel("WEIGHT_FKP")
for i in np.unique(cut["NTILE"]):
    m = cut["NTILE"] == i
    axes[0].hist(cut["WEIGHT"][m], bins=wbins, alpha=0.6, label=f"NTILE={i}")
    axes[1].hist(cut["WEIGHT_FKP"][m], bins=fkpbins, alpha=0.6, label=f"NTILE={i}")
axes[0].legend()
fig.savefig("results/figures/weight_distribution.png", dpi=250)

nz = np.loadtxt("data/LRG_NGC_nz.txt")
zmid = nz[:, 0]
zlow = nz[:, 1]
zhigh = nz[:, 2]
n_z = nz[:, 3]
Nbin = nz[:, 4]
volbin = nz[:, 5]
print((Nbin / volbin)[:5])
print(n_z[:5])

bins = np.append(zlow, zhigh[-1])
counts, edges = np.histogram(data["Z"], bins=bins)
my_nz = counts / volbin
counts_w, _ = np.histogram(data["Z"], bins=bins, weights=data["WEIGHT"])
my_nz_w = counts_w / volbin
comp = data["WEIGHT"] / (data["WEIGHT_COMP"] * data["WEIGHT_SYS"] * data["WEIGHT_ZFAIL"])
w_corr = data["WEIGHT"] / comp
counts_c, _ = np.histogram(data["Z"], bins=edges, weights=w_corr)
my_nz_c = counts_c / volbin

plt.figure(figsize=(10,6))
plt.title("Reproducing DESI number density")
plt.xlabel("Redshift")
plt.ylabel("n(z) [h³ Mpc⁻³]")
plt.plot(zmid, n_z, label="DESI published")
plt.plot(zmid, my_nz, label="Mine")
plt.plot(zmid, my_nz_w, label="Mine(weighted)")
plt.plot(zmid, my_nz_c, label="Mine(completeness-corrected)")
plt.legend()
plt.savefig("results/figures/nz.png")