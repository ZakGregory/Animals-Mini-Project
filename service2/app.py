from flask import Flask, request, jsonify, Response
import requests 
import random

app = Flask(__name__)

#animal_dictionary={"Crocodile":"hiss","Tiger":"Roar","Cat":"meow","Chicken":"Crow","Dog":"Bark"}
animal_list=["Cat","Chicken","Dog"]
#noise_list=["hiss"]

@app.route('/')
def home():
    return "Hello from service 2"

@app.route('/get/animal/', methods=["GET"])
def get_animal():
    n= random.randint(0, len(animal_list)-1)
    return_data = animal_list[n]
    return Response(return_data, mimetype='text/plain')

@app.route('/post/animal/', methods=["POST"])
def post_animal():
    post_data= request.data.decode("utf-8")
    if post_data == "Cat" :
        return_data = "Meow"
    elif post_data == "Dog" :
        return_data = "Bark"
    elif post_data == "Chicken" :
        return_data = "Cluck"
    return Response(return_data, mimetype='text/plain')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
