from .simulator import *
from .preprocessing import *
import pandas


def get_list_products(result):
    productos = pd.read_csv("Data/cluster_productos.csv")
    lista = productos[productos['cluster']==result].producto.values[0]

    return lista