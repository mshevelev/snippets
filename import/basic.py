# @tags: import, init, basic

import os, sys, shutil, psutil, re, warnings, json
from glob import glob


import numpy as np
import pandas as pd
import xarray as xr
import scipy.stats
from statsmodels import api as sma

import holoviews as hv
import hvplot.pandas
import hvplot.xarray

for local_package in ('/home/mshevelev/git/ms_utils', ):
  if local_package not in sys.path:
    sys.path.insert(0, local_package)
import ms_utils; print(f"{ms_utils.__path__}")

from ms_utils.holoviews.settings import apply_defaults
apply_defaults()
