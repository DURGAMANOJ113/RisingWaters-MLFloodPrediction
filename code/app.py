from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load("floods.save")
scaler = joblib.load("transform.save")

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        cloud_cover = float(request.form['cloud'])
        annual_rainfall = float(request.form['annual'])
        jan_feb_rain = float(request.form['janfeb'])
        mar_may_rain = float(request.form['marMay'])
        jun_sep_rain = float(request.form['juneSept'])

        features = np.array([[cloud_cover, annual_rainfall, jan_feb_rain, mar_may_rain, jun_sep_rain]])
        features_scaled = scaler.transform(features)
        
        # Predict the class
        prediction = model.predict(features_scaled)

        # ✅ Show probability in terminal (optional)
        if hasattr(model, "predict_proba"):
            prob = model.predict_proba(features_scaled)
            print("🔍 Flood Probability:", prob[0][1])  # This prints probability of class 1

        # Render result
        if prediction[0] == 1:
            return render_template("chance.html")
        else:
            return render_template("no_chance.html")

    except Exception as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(debug=True)    
    