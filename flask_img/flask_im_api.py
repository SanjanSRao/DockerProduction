# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:33:02 2019

@author: rao_s
"""

from keras.models import load_model
from PIL import Image
import numpy as np
from flasgger import Swagger
import os
os.environ['KERAS_BACKEND'] = 'theano'

from flask import Flask, request
app = Flask(__name__)
swagger = Swagger(app)

model = load_model('./img_reco_model.h5')

@app.route('/predict_digit', methods=['POST'])
def predict_digit():
    """Example endpoint returning prediction of mnist
    ---
    parameters:
        - name: image
          in: formData
          type: file
          required: true
    definitions:
        value:
            type: object
            properties:
                value_name:
                    type: string
                    items:
                        $ref: '#/definitions/Color'
        Color:
            type: string
    responses:
        200:
            description: OK
            schema:
                $ref: '#/definitions/value'
    
    """
    im = Image.open(request.files['image'])
    im2arr = np.array(im).reshape((1, 1, 28, 28))
    return str(np.argmax(model.predict(im2arr, batch_size=1)))

if __name__ == '__main__':
    app.run()