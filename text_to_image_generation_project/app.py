from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
COLAB_BACKEND_IMAGE_URL = 'https://2822a1e59b89.ngrok-free.app//generate-image' #if this url doesn't work copy the url given by ngrok in your google colab.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data= request.form['text']
    
    response = requests.post(COLAB_BACKEND_IMAGE_URL, json={'text': data}, stream=True)
    if response.status_code == 200:
        
        return response.content
    else:
        return jsonify({'error': 'Failed to generate image'}), 500

if __name__ == '__main__':
    app.run(port=8000, debug=True)

