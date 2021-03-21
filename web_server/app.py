#Install Libraries
from flask import Flask, request, jsonify
import joblib
import traceback
import pandas as pd
import numpy as np
from os import sys



application = Flask(__name__)


@application.route('/prediction', methods=['POST'])

def predict():
    if lr:
        try:
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=rnd_columns, fill_value=0)
            predict = list(lr.predict(query))
            print(lr.predict_proba(query))
            return jsonify({'prediction': str(predict)})
        except:
            return jsonify({'error': 'invalid input'})
    else:
        print ('error with the model')
        return ('errors')



if __name__ == '__main__':
    try:
        port = int(sys.argv[1])
    except:
        port = 8080

    lr = joblib.load('web_server/XGBOOST.pkl') 
    print ('Model loaded')
    rnd_columns = joblib.load("web_server/rnd_columns.pkl") # Load “rnd_columns.pkl”
    print('Model columns loaded')
   
application.run(port=port, debug=True, host='0.0.0.0')