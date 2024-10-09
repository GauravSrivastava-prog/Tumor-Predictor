from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('final_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    features = [float(request.form.get(f)) for f in [
        'radius1', 'texture1', 'perimeter1', 'area1', 'smoothness1',
        'compactness1', 'concavity1', 'concave_points1', 'symmetry1', 'fractal_dimension1',
        'radius2', 'texture2', 'perimeter2', 'area2', 'smoothness2',
        'compactness2', 'concavity2', 'concave_points2', 'symmetry2', 'fractal_dimension2',
        'radius3', 'texture3', 'perimeter3', 'area3', 'smoothness3',
        'compactness3', 'concavity3', 'concave_points3', 'symmetry3', 'fractal_dimension3'
    ]]
    
    # Make prediction
    prediction = model.predict([features])[0]
    
    # Return result
    result = 'Malignant' if prediction == 'M' else 'Benign'
    
    return f'The tumor is {result}.'

if __name__ == '__main__':
    app.run(debug=True)
