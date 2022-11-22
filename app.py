#import os
#from pathlib import Path
#import streamlit as st

from flask import Flask, jsonify, render_template, request

#import src.utils as utils


#from keras.models import load_model

#import segmentation_models as sm
#from segmentation_models import Unet
#from segmentation_models import get_preprocessing

#DATASET_PATH = "C:/Users/jketk/Desktop/p8data"



#Create an app object using the Flask class. 
app = Flask(__name__)

#Add reference fingerprint. 
#Cookies travel with a signature that they claim to be legit. 
#Legitimacy here means that the signature was issued by the owner of the cookie.
#Others cannot change this cookie as it needs the secret key. 
#It's used as the key to encrypt the session - which can be stored in a cookie.
#Cookies should be encrypted if they contain potentially sensitive information.








#home page
@app.route('/', methods = ['GET'])
def home_page():
    return flask.render_template('index.html')



if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)
# In[ ]:





# In[ ]:




