from flask import *
import pickle
import numpy as np

app=Flask('__name__')
 
with open ("house_price_model.pkl","rb") as f:
   model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['Post'])
def predict():
    try:
        features=[float(x) for x in request.form.values()]
        features_array = np.array([features])
        prediction = model.predict(features_array)[0]
        return render_template("index.html",prediction_text=f"predicted house price ${prediction:.2f}")
    
    except Exception as e:
        return jsonify({"error": str(e)})



if __name__ == "__main__":
    app.run(debug=True)
