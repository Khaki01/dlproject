from flask import Flask, request, jsonify
import  sys


app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        video_path = request.args.get('path')

    try:
        prediction = get_prediction(video_path)
        data = {'prediction': prediction}
        return jsonify(data)

    except:
        return jsonify({'error': 'error during prediction'})