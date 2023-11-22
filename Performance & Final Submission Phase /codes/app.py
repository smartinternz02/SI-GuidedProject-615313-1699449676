from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load your model
model = load_model('weights.h5',compile=False)  # Update with your actual path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
    
        file = request.files['file']
    
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'del', 'nothing', 'space']
    
        # Process the image for prediction (you might need to resize, normalize, etc.)
        img = Image.open(file)
        img = img.resize((32, 32))  # Adjust the size according to your model's input shape
        img_array = np.array(img) / 255.0  # Normalize
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
        # Make prediction
        prediction = model.predict(img_array)
    
        predicted_class = labels[np.argmax(prediction)]
        
        text = "Your image represents "+predicted_class
        return jsonify({'prediction': text})


if __name__ == '__main__':
    app.run(debug=False, threaded = False)

