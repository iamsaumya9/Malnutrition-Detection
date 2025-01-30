from flask import Flask, render_template, request, jsonify
import numpy as np
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

# Load model
(model == load_model('model.keras')
)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    img = request.files['file']  # Image upload
    img_path = './uploads/' + img.filename
    img.save(img_path)

    # Image preprocessing
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array)
    # Assuming binary classification: 0 = Healthy, 1 = Malnourished
    result = 'Malnourished' if prediction[0][0] > 0.5 else 'Healthy'
    
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)
