from flask import Flask, request, jsonify, Response
import requests 

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    animal_response = requests.get('172.17.0.0:5001/get/animal/').text
    noise_response= requests.post('172.17.0.0:5001/post/animal/', animal_response).text
    a= animal_response+noise_response
    return a

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
