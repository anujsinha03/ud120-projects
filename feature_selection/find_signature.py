#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)
import sys


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "C:/Users/sinhaanuj1996/Desktop/ud120-projects/text_learning/your_word_data.pkl" 
authors_file = "C:/Users/sinhaanuj1996/Desktop/ud120-projects/text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation, tree
from sklearn.metrics import accuracy_score
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train).toarray()
features_test  = vectorizer.transform(features_test).toarray()

###print len(vectorizer.get_feature_names())
### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150]
labels_train   = labels_train[:150]

### your code goes here

df = tree.DecisionTreeClassifier()
df.fit(features_train, labels_train)
pred = df.predict(features_test) 

print "Accuracy Score:",accuracy_score(labels_test, pred)*1.0

len(features_train)
maxi = (0, 0)
importance = df.feature_importances_
for index, item in enumerate(importance):
    if item > 0.2:
        print index + 1, item
        if item > maxi[1]:
            maxi = (index + 1, item)
print maxi

print vectorizer.get_feature_names()[maxi[0] - 1]
###features = vectorizer.get_feature_names()
###print features[maxi[0] - 1]
"""
for index, item in enumerate(features):
    if (index == maxi[0] - 1):
        print item
"""

