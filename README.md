# DESI DR1 LRG clustering

Measuring the two-point correlation function of Luminous Red Galaxies
from DESI Data Release 1, to recover the sound horizon scale and the
linear galaxy bias.

Work in progress.

## Setup

conda env create -f environment.yml
conda activate desi-lss
python check_install.py

## Data Notes

### Tracers & Redshift Ranges
Bright Galaxy Survey: 0-0.5, 6.3M
Luminous Red Galaxies: 0.4-1.1, 2.8M
Emission Line Galaxies: 0.6-1.6, 3.9M
Quasars: 0.6-3.5, 1.3M

### Weights
WEIGHT_FKP: an optimal weighting scheme that balances the contribution of regions with different number densities to minimise the variance of the clustering measurement, computed using density as function of both redshift and tile coverage
WEIGHT_SN: the neural net method SYSNET
WEIGHT_RF: the random forest method REGRESSIS
WEIGHT_ZFAIL: to account for changes in the relative redshift success rates
WEIGHT_SYS: corrects for target density fluctuations due to imaging conditions
WEIGHT_COMP: corrects for the fraction of targets that received a fibre, up-weighting observed galaxies to compensate for those that could not be observed

WEIGHT: the combination of all weights to use
WEIGHT = WEIGHT_COMP * WEIGHT_SYS * WEIGHT_ZFAIL as per eq. 7.1 of Ross et al. (2025)
However this is verified to not be true. The residual takes 7 discrete values that map one-to-one onto NTILE, rising monotonically from 0.61 at single tile coverage to 0.99 at seven tile coverage. WEIGHT is used as the total weight throughout.

### Random Catalogues
18 random files per tracer per region, 4 used here: LRG_NGC_0-3.
9,389,714 rows each giving around 25 times the galaxy density when concatenated.

Randoms are generated across the target footprint, only where DESI could have observed a galaxy.
They are then passed through the same fibre assignment logic as the real data, so they carrry the same geometry and observational selection as the survey
They have a TARGET_ID column linking each random to a real galaxy.
Their redshifts are drawn from the data to guarantee the number densities n(z) random = n(z) data.

### Fiducial Cosmology
Assumed reference cosmology.
Required to convert redshifts to distance before measurements can be made.

Parameter values loaded from cosmoprimo.fiducial.DESI:
Ωm = 0.3151917236644108: Total Mater Density Fraction
h = 0.6736: Dimensionless Hubble Constant, H0/100km/s/Mpc
Ωb = 0.049301692328524445: Baryon Density Fraction
ns = 0.9649: Primordial Spectral Index
σ8 = 0.8078314028262475: Present Day Matter Clustering Amplitude