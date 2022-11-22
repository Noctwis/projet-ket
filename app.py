#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# data p8 and not p8_data


# In[ ]:


import os
from pathlib import Path
import streamlit as st

from flask import Flask, jsonify, render_template, request

import src.utils as utils


from keras.models import load_model

import segmentation_models as sm
from segmentation_models import Unet
from segmentation_models import get_preprocessing

#DATASET_PATH = "C:/Users/jketk/Desktop/p8data"



#Create an app object using the Flask class. 
app = Flask(__name__)

#Add reference fingerprint. 
#Cookies travel with a signature that they claim to be legit. 
#Legitimacy here means that the signature was issued by the owner of the cookie.
#Others cannot change this cookie as it needs the secret key. 
#It's used as the key to encrypt the session - which can be stored in a cookie.
#Cookies should be encrypted if they contain potentially sensitive information.
app.secret_key = "secret key"


# same idea for dice and jaccard metrics
def dice_metric(y_true, y_pred):
    smooth = 1.
    y_true_f = K.flatten(y_true)
    y_pred_f = K.flatten(y_pred)
    intersection = K.sum(y_true_f * y_pred_f)
    score = (2. * intersection + smooth) / (K.sum(y_true_f) + K.sum(y_pred_f) + smooth)
    return score

def dice_loss(y_true, y_pred):
    loss = 1 - dice_metric(y_true, y_pred)
    return loss


# Model saved with Keras model.save()
MODEL_PATH = 'model_Unet_resNet_2.hdf5'

# Load your trained model

BACKBONE = 'resnet34'
model_resnet = Unet(BACKBONE, encoder_weights='imagenet', classes=8,activation='softmax')
model_resnet.compile('Adam', loss=dice_loss, metrics=[dice_metric])
#model = tf.keras.models.load_model('model_Unet_resNet_2-Copy1.hdf5')

# Loads the weights
model_resnet.load_weights('model.hdf5')

#model.make_predict_function()          # Necessary
MODEL_NAME = "model_resnet"
print('Model loaded. Start serving...')


@app.route("/")
@app.route("/api")
def index(image_id=""):
    original_img_str, labels_img_str, categories_img_str = (
        None,
        None,
        None,
    )

    if request.args.get("image_id"):
        image_id = request.args.get("image_id")
        (
            original_img_str,
            labels_img_str,
            categories_img_str,
        ) = utils.get_images(
           
            
            dataset_path=DATASET_PATH,
            image_id=image_id,
        )

    if request.path == "/api":
        return jsonify(
            original_img_str=original_img_str,
            labels_img_str=labels_img_str,
            categories_img_str=categories_img_str
        )

    return render_template(
        "index.html",
        image_id=image_id,
        original_img_str=original_img_str,
        labels_img_str=labels_img_str,
        categories_img_str=categories_img_str
    )


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)
# In[ ]:





# In[ ]:




