import pandas as pd
import numpy as np
import math
import random
#import requests 
import os
import matplotlib.pyplot as plt
#from bs4 import BeautifulSoup

# url: http://clientes.serpost.com.pe/prj_pjudicial/ubigeo.aspx

def simulate(data_path='Data\\', n=100, seed=None):
    if seed==None:
        np.random.seed()
    else:
        np.random.seed(seed) 
    
    # Generate ubigeo_list
    path = os.getcwd()
    print(os.path.abspath(os.path.join(path, os.pardir)))
    # data_path =  'Data\\'
    filename = 'ubigeo.csv'
    df_ubigeo = pd.read_csv(data_path + filename, sep=';')
    ubigeo_list = list(df_ubigeo[df_ubigeo.DEPARTAMENTO == 'LIMA'].UBIGEO.unique())
    ubigeo_prov = list(df_ubigeo[df_ubigeo.DEPARTAMENTO == 'LIMA'].PROVINCIA.unique())

    # Generate dataframe
    dni = random.sample(range(n), n)
    edad = [int(np.random.triangular(18, 35, 75)) for i in range(n)]
    cod_ubigeo = np.random.choice( a=ubigeo_list, size=n )
    provincia = np.random.choice( a=ubigeo_prov, size=n )
    rcc_cal_gral = np.random.choice( 
        a=["OK", "CPP", "PER", "DUD", "DEF"], 
        size=n, 
        p=[0.1, 0.3, 0.4, 0.1, 0.1] )
    rcc_num_ent_sbs = [int(np.random.triangular(1, 3, 10)) for i in range(n)]
    rcc_linea_tc_max = np.random.exponential(scale=1000, size=n)
    rcc_nro_prod = [int(np.random.triangular(1, 7, 20)) for i in range(n)]
    num_seguros_salud = [int(np.random.triangular(1, 1, 3)) for i in range(n)]
    ingreso_mens = np.random.exponential(scale=1000, size=n)
    es_cliente = np.random.choice( 
        a=['0','1'], 
        size=n, 
        p=['0.8', '0.2'])
    flg_viaje_tw = np.random.choice( 
        a=['0','1'], 
        size=n, 
        p=['0.7', '0.3'])
    tipo_vivienda = np.random.choice( 
        a=['propia', 'hipot', 'alqui', 'fami', 'otro'], 
        size=n, 
        p=[0.1, 0.3, 0.4, 0.1, 0.1])
    sit_laboral = np.random.choice( 
        a=['DEP','INDEP'], 
        size=n, 
        p=[0.6, 0.4]) 
    segmento = np.random.choice( 
        a=['SEGM1', 'SEGM2', 'SEGM3','SEGM4'],   
        size=n,    
        p=[0.1, 0.3, 0.4, 0.2]  )
    prod_interes = np.random.choice(
        a=['CTA_AHORRO','TC','T_CAMBIO','PREST', 'ADS', 'TA', 'DP', 'FM'], 
        size=n, 
        p=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.3])
    
    # tasa = [np.random.triangular(3.0, 3.2, 3.6) for i in range(n)]
    d = {
        'dni': dni, 
        'edad': edad,
        'cod_ubigeo': cod_ubigeo,
        'provincia': provincia,
        'rcc_cal_gral': rcc_cal_gral,
        'rcc_num_ent_sbs': rcc_num_ent_sbs,
        'rcc_linea_tc_max': rcc_linea_tc_max,
        'rcc_nro_prod': rcc_nro_prod,
        'num_seguros_salud': num_seguros_salud,
        'ingreso_mens': ingreso_mens,
        'es_cliente': es_cliente,
        'flg_viaje_tw': flg_viaje_tw,
        'tipo_vivienda': tipo_vivienda,
        'sit_laboral': sit_laboral,
        'segmento': segmento,
        'prod_interes': prod_interes}
    df = pd.DataFrame(data=d)

    return df