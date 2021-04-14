import flask
import time
from flask import Flask
from flask import request
from flask import Flask, render_template, Response, request, redirect, jsonify, send_from_directory, abort, send_file
from flask_cors import CORS
import numpy as np 
import os , io , sys
import lightgbm as lgb
from models import *
from utils import *

app = Flask(__name__)
CORS(app)

MODEL = None

def predict_products(dni):

    #get the data from the database
    #data = get_data(dni)
    data = pd.DataFrame()
    data = data.append({'dni': dni, '_last_judgment_at': "10/26/15 23:24", 'gender': "male", 'created': "12/5/13 1:48",
            'edad': 47, 'provincia': "COMAS", "rcc_cal_gral": "PER",
            'rcc_num_ent_sbs': 4, 'rcc_linea_tc_max': 561.364765, 
            'rcc_nro_prod': 5, 'num_seguros_salud': 1, 
            'ingreso_mens': 480.752552, 'tipo_vivienda': "alqui",
            'tipo_vivienda': "alqui",
            'sit_laboral':"DEP",
            'segmento':"SEGM1"}, ignore_index=True)


    cluster = MODEL.predict(data)
    productos = get_list_products(cluster[0])    

    return productos


@app.route('/get_products', methods=['POST'])
def get_products():
    dni = request.form.get('dni')

    errors = {}
    success = False

    if not isinstance(dni, str):
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp 

    if dni:
        products = predict_products(dni)
        success = True
    else:
        errors[dni] = 'File type is not allowed'

    if success and errors:
        errors['message'] = 'dni successfully uploaded'
        resp = jsonify(errors)
        resp.status_code = 500
        return resp
    if success:
        resp = jsonify({'message' : 'Files successfully processed', 'products': str(products)})
        resp.status_code = 201
        resp.headers.add('Access-Control-Allow-Origin', '*')
        print('headers:: ', resp.headers)
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp

if __name__ == "__main__":
    
    MODEL = Model('models/lightgbm_pred.pk')

    app.run(host="0.0.0.0", port="9999")