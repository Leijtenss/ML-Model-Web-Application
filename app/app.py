# app/app.py

# Common python package imports.
from flask import Flask, jsonify, request, render_template
import pickle
import numpy as np

# Import from model_api/app/features.py.
from features import FEATURES


# Initialize the app and set a secret_key.
app = Flask(__name__)
app.secret_key = 'something_secret'

# Load the pickled model.
#MODEL = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,6)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        
        if int(result)==0:
            prediction='Worthless house'
        else:
            prediction='Predicted value of the house (*1000) is $'+str(round(result, 2))
            
        return render_template("result.html",prediction=prediction)


#@app.route('/api', methods=['GET'])
#def api():
#    """Handle request and output model score in json format."""
#    # Handle empty requests.
#    if not request.json:
#        return jsonify({'error': 'no request received'})
#
#    # Parse request args into feature array for prediction.
#    x_list, missing_data = parse_args(request.json)
#    x_array = np.array([x_list])
#
#    # Predict on x_array and return JSON response.
#    estimate = int(MODEL.predict(x_array)[0])
#    response = estimate
#
#    return jsonify(response)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)