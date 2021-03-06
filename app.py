from flask import render_template, request, jsonify
import flask
import traceback
import pandas as pd
import os
import sys
import json
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import load_img,img_to_array
import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
from predict import prdct
from tensorflow.python.keras.backend import set_session



app = flask.Flask(__name__,template_folder='templates')

session =  tf.compat.v1.Session(graph=tf.Graph())
with session.graph.as_default():
    set_session(session)
    with open('model/model_in_json.json','r') as f:
        model_json = json.load(f)
    model2 = model_from_json(model_json)
    model2.load_weights('model/model_weights.h5')


@app.route('/')
def welcome():
   return "crop weed segmantation"

@app.route('/predict', methods=['POST'])
def segment():
    global model2,session
    if flask.request.method == 'GET':
        return "Prediction page"

    if 'file' not in flask.request.files:
        return "no file"

    file = flask.request.files['file']
    print(type(file))
    # print(file)

    if file.filename == '':
        return "no file name"

    if file:
        filename = file.filename
        file.save("./input/"+filename)
        res = prdct("./input/"+filename,session,model2)
        return res




if __name__ == "__main__":
   app.run(host='0.0.0.0')
