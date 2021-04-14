import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler, MinMaxScaler
from sklearn.metrics import silhouette_score,classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
import pickle
import lightgbm as lgb


COLS_YES = ["log_ingreso_mens", "log_num_seguros_salud", "log_rcc_nro_prod", "log_rcc_linea_tc_max", 
            "log_rcc_num_ent_sbs", "log_edad", "log_diff_lj_created","enc_rcc_cal_gral",
            "enc_nse", "enc_segmento", "enc_gender"]

class Model():
    def __init__(self, path_filename):
        self.loaded_model = pickle.load(open(path_filename, 'rb'))

    def predict(self, data):
        data = process_data(data)

        return self.loaded_model.predict(data[COLS_YES])

