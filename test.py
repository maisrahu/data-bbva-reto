#%%
import pandas as pd 
import numpy as np 
import matplotlib as plt
import utils.simulator as simu 

#%%
df_final = pd.read_csv('Data\\df_final_target.csv')



# %%
productos = {
    'cluster': ['0', '1', '2'],
    'producto': [
        ['tarjeta de crédito', 'tarjeta adicional', 't_cambio'],
        ['préstamo al toque', 'adelanto en sueldo'],
        ['depósito a plazo','fondos mutuos']]
}

df = pd.DataFrame(productos)



# %%
