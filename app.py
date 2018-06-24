import os
import io
import numpy as np


from flask import Flask, request, redirect, url_for, jsonify

app = Flask(__name__)

#we're going to need a route that will do get post since we are taking user input
#we can also create a route for jsonifying the data after the sql lite file to make sure 
#also route for recommendations? That actually might end up being a part of the get post aspect

@app.route('/', methods=['GET', 'POST'])



@app.route('/data') #jsonifies the data we have


if __name__ == "__main__":
    app.run(debug=True)
