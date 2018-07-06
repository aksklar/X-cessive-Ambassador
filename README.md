# X-cessive-Ambassador
## Predicting movie genres with Natural Language Processing
For our final project, we decided to predict the primary genre of a movie based on it's plot summary. To achieve this, 
we used the OMDB API and the MovieLens dataset to obtain the title, movie genres, and the plot summary. We then tested and trained
our data using scikit learn and then measured the accuracy scores for Logistic Regression, Naive Bayes, and LinearSVC. Based on 
our models, the best accuracy score was with LinearSVC which we used in our Flask application to predict the movie genre.

Conclusion:
Our accuracy scores were still low even though we were able to predict the primary genre of a few movies correctly. If we had more time, we could have used XGBoost or words2vec to assist us as well. Misclassifications still happened but we also noticed that as well while researching this topic. 

## Webpage:
* https://mgp-flask.herokuapp.com/
