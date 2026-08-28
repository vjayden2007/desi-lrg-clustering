from pathlib import Path
import urllib.request

base = "https://data.desi.lbl.gov/public/dr1/survey/catalogs/dr1/LSS/iron/LSScats/v1.2/"
files = ["LRG_NGC_clustering.dat.fits", "LRG_NGC_0_clustering.ran.fits", "LRG_NGC_1_clustering.ran.fits", "LRG_NGC_2_clustering.ran.fits", "LRG_NGC_3_clustering.ran.fits", "LRG_NGC_nz.txt"]


for i in files:
    dest = Path("data") / i
    if dest.exists():
        print(i," is already downloaded")
    else:
        print(i," is downloading")
        urllib.request.urlretrieve(base + i, dest)
        print(i," is now downloaded")
