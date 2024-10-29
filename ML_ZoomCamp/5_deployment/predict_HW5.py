import pickle

from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model1.bin'
dv = 'dv.bin'

with open(model_file, 'rb') as f_in_model:
    model = pickle.load(f_in_model)

with open(dv, 'rb') as f_in_dv:
    dv = pickle.load(f_in_dv)

app = Flask('client')

@app.route('/subscription', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform([client]) 
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        'subscription_probability': float(y_pred),
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)