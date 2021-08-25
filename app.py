from flask import Flask
from flask import request
import numpy as np
import pandas as pd
from modelService import get_model,pre_process

app = Flask(__name__)


@app.route('/home', methods=['GET'])
def getHome():
    return "HOME"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.json_normalize(data)
    data = pre_process(df).values.reshape(1, -1)
    model = get_model()
    print(data)
    return str(model.predict(data))
