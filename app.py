import os
import io
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, request, redirect, url_for, jsonify
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

model = LinearSVC()
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.33, random_state=42)
X_train_counts=count_vect.fit_transform(X_train)
X_train_tfidf=tfidf_transformer.fit_transform(X_train_counts)
svc=model.fit(X_train_tfidf, y_train)


#Title = the title input you're getting from post method
#Plot=session.query(Movies.Plot).filter(Movies.Title=='{}'.format(Title)).all()
#prediction=svc.predict(count_vect.transform([the session.query]))
#print(f"The primary movie genre is:{prediction[0]})


#@app.route("/index")
#def home():
#    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def predict_model():
     if request.method == 'POST':
         title=request.form["Movie Title"]
         plot = session.query(Movies.Plot).filter(Movies.Title=='{}'.format(title)).all()
         prediction=svc.predict(count_vect.transform(plot))
         return f"The primary movie genre is:{prediction[0]}"
         




if __name__ == "__main__":
    app.run(debug=True)
