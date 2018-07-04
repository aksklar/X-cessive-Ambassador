import os
import io
import numpy as np
import pandas as pd
import sqlalchemy
import csv
import json
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, request, redirect, url_for, jsonify, render_template
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################


engine = create_engine("sqlite:///data/1500_movies_data.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Movies = Base.classes.full_movie_data
session = Session(engine)
#################################################
#Model setup to predict movie genre
#################################################

df = pd.read_csv('data/1500_movies_data.csv')
from io import StringIO
col = ['Genre', 'Plot']
df = df[col]
df = df[pd.notnull(df['Plot'])]

df.columns = ['Genre', 'Plot']


df['category_id'] = df['Genre'].factorize()[0]
category_id_df = df[['Genre', 'category_id']].drop_duplicates().sort_values('category_id')
category_to_id = dict(category_id_df.values)
id_to_category = dict(category_id_df[['category_id', 'Genre']].values)

#For the prediction, we use Linear SVC because that had the best accuracy score
X=df['Plot']
y=df['Genre']
count_vect=CountVectorizer(stop_words='english', max_df=0.5, ngram_range=(1,2))
model = LinearSVC()
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.33, random_state=42)
X_train_counts=count_vect.fit_transform(X_train)
tfidf_transformer=TfidfTransformer(sublinear_tf=True,smooth_idf=False)
X_train_tfidf=tfidf_transformer.fit_transform(X_train_counts)
svc=model.fit(X_train_tfidf, y_train)

###################################################
#Routes
###################################################

@app.route("/")
def home():
    return render_template("index.html") 

@app.route('/predict', methods=['GET', 'POST'])
def predict_model():
    global prediction
    if request.method == 'POST':
        title=request.form["MovieTitle"]
        plot = session.query(Movies.Plot).filter(Movies.Title=='{}'.format(title)).all()
        prediction=svc.predict(count_vect.transform(['{}'.format(plot[0])]))
        return render_template("index.html", title=title, prediction=prediction[0])


@app.route("/data")
def data():
    data = pd.read_json("data/1500_movies_data.json")

    return jsonify(data.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)


