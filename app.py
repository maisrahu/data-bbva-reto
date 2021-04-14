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

if __name__ == "__main__":
    


    app.run(host="0.0.0.0", port="9999")