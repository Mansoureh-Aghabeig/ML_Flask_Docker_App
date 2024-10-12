from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the machine learning model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')  # No need to include 'templates/'

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    try:
        features = [float(x) for x in request.form.values()]
        # Make predictions using the model
        prediction = model.predict([features])
        result = prediction[0]
    except ValueError:
        result = "Invalid input. Please enter numeric values."

    return render_template('result.html', prediction=result)  # No need to include 'templates/'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5053)
