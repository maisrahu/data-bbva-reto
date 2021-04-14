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
        ['Cuentas de Ahorro', 'Tarjeta de Crédito', 'Tarjeta Adicional', 'BBVA T-Cambio'],
        ['Préstamo al Toque', 'Adelanto en Sueldo'],
        ['Depósito a Plazo','Fondos Mutuos']]
}

df = pd.DataFrame(productos)
df.to_csv('Data\\cluster_productos.csv')


# %%
