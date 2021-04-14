import flask
import time
from flask import Flask
from flask import request
from flask import Flask, render_template, Response, request, redirect, jsonify, send_from_directory, abort, send_file
from flask_cors import CORS
import numpy as np 
import cv2
import base64
import os , io , sys

app = Flask(__name__)
CORS(app)

def get_products(dni):

    #get the data from the database

    


@app.route('/get_products', methods=['POST'])
def get_products():
    dni = request.form.get('dni')

    errors = {}
    success = False

    if not isinstance(dni, int):
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
        resp = jsonify({'message' : 'Files successfully processed', 'products': products})
        resp.status_code = 201
        resp.headers.add('Access-Control-Allow-Origin', '*')
        print('headers:: ', resp.headers)
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 500
        return resp

if __name__ == "__main__":
    


    app.run(host="0.0.0.0", port="9999")