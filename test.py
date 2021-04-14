import pandas as pd 
import numpy as np 
import matplotlib as plt
import utils.simulator as simu 

from sklearn.clusters import KMeans
from sklearn.metrics import pairwise_distances_argmin_min


df = simu.simulate(1000)
print(df)
