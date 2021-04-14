import pandas as pd
import numpy as np
import math
# import matplotlib.pyplot as plt
# import seaborn as sns


def simulate(n=100, seed=None):
    if seed==None:
        np.random.seed()
    else:
        np.random.seed(seed) 
    
    canal = np.random.choice( a=['CANAL1', 'CANAL2', 'CANAL3','CANAL4'],   size=n,    p=[0.3, 0.3, 0.2, 0.2]  )
    segmento = np.random.choice( a=['SEGM1', 'SEGM2', 'SEGM3','SEGM4'],   size=n,    p=[0.1, 0.3, 0.4, 0.2]  )
    perfil_rcc = np.random.choice( a=['RCC1', 'RCC2'],   size=n,    p=[0.3, 0.7]  )
    monto = np.random.exponential(scale = 1000,size=n)
    tasa = [np.random.triangular(3.0, 3.2, 3.6) for i in range(n)]
    edad = [int(np.random.triangular(18, 35, 75)) for i in range(n)]
    saldo_rcc = np.random.exponential(scale = 200,size=n)
    d = {
        'tasa': tasa,
        'monto': monto,
        'edad': edad,
        'saldo_rcc': saldo_rcc,
        'canal': canal,
        'segmento': segmento,
        'perfil_rcc': perfil_rcc}

    df = pd.DataFrame(data=d)
    
    return df