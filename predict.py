import sys
import json
from keras.models import load_model
from keras.models import model_from_json
from keras.preprocessing.image import load_img,img_to_array
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
from tensorflow.python.keras.backend import set_session
import json


dim = 1024

def prdct(name,session,model2):
    img=load_img(name,target_size=(dim,dim))
    img = img_to_array(img)/255
    with session.graph.as_default():
        set_session(session)
        res=model2.predict(img.reshape(1,dim,dim,3))
    res = np.reshape(res,(dim,dim,3))
    res=res*255
    res=json.dumps({"arr":res.tolist()})
    return res
