from flask import Flask , request, jsonify
import pickle
import numpy as np


app = Flask(__name__)

#import the model
with open('model.pkl','rb') as file:
    model = pickle.load(file)


#define the route
@app.route('/predict', methods = ['POST'])
def predict():    
    data = request.get_json()
    features = data['features']
    prediction = model.predict([features])
    prediction = prediction.tolist() if isinstance(prediction, np.ndarray) else prediction
    return jsonify({'prediction': prediction[0]}) 



if __name__ == '__main__':
    app.run(debug = True,host="0.0.0.0",port=8080)

