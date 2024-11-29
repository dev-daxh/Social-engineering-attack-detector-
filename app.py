from flask import Flask, request, jsonify,render_template
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load models once during initialization
url_model = joblib.load('url_model.joblib')
email_model = joblib.load('email_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

# Endpoint for URL prediction
@app.route('/predict-url', methods=['POST'])
def predict_url():
    data = request.json
    if 'url' not in data:
        return jsonify({"error": "URL not provided"}), 400

    user_url = data['url']
    prediction = url_model.predict([user_url])[0]
    result = "malicious" if prediction == 1 else "safe"
    return jsonify({"url": user_url, "prediction": result})

# Endpoint for Email prediction
@app.route('/predict-email', methods=['POST'])
def predict_email():
    data = request.json
    if 'email' not in data:
        return jsonify({"error": "Email content not provided"}), 400

    user_email = data['email']
    prediction = email_model.predict([user_email])[0]
    result = "malicious" if prediction == 1 else "safe"
    return jsonify({"email": user_email, "prediction": result})

if __name__ == '__main__':
    app.run(debug=True)
