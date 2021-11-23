from flask import Flask, request, jsonify, render_template
import sys
import os
import datetime

import scripts.google_full as model

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        #return '1'
        f = request.files['audio_data']
        now=datetime.datetime.now()
        print(type(now))
        filename = 'audio_{}.wav'.format(str(now).replace(":",''))
        with open(filename, 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')

        prediction = model.get_prediction_audio(filename)
        data = {'prediction': prediction}
        print(data)
        return render_template('index.html', request="POST")   
    else:
        return render_template("index.html")

    
        

if __name__ == "__main__":
    app.run()