import pandas as pd 
import numpy as np 
import matplotlib as plt
import utils.simulator as simu 

from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, max_error


df = simu.simulate(1000)
print(df)

