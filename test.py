#%%
import pandas as pd 
import numpy as np 
import matplotlib as plt
import utils.simulator as simu 

#%%
df_final = pd.read_csv('Data\\df_final_target.csv')



# %%
productos = {
    'cluster': ['0', '1', '2', '3', '4'],
    'producto': [
        'Fondos mutuos',
        'Adelanto de sueldo, Depósito a plazo',
        'Cuentas de Ahorro, BBVA T-Cambio',
        'Tarjeta de Crédito',
        'Préstamo al Toque']
}
df = pd.DataFrame(productos)
df.to_csv('Data\\cluster_productos.csv')


# %%
# Cluster 0: # Perfil inversor, mayores ingresos, perfil de más consumo
# Fondos mutuos

# Cluster 1: # Percibe ingresos altos, probable moroso
# Adelanto de sueldo
# Depósito a plazo

# Cluster 2: # probable moroso, problable que se endeude
# Ctas de Ahorro
# T_cambio

# Cluster 3: # Buen pagador, perfil de consumo
# Tarjeta de crédito

# Cluster 4: # Percibe ingreso promedio, requiere de dinero inmediato
# Préstamo al toque