#!/usr/bin/python python -W ignore::DeprecationWarning

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf = GaussianNB()
t0 = time()
clf.fit(features_train,labels_train)
print("Training time is:","%0.4f"%(time() - t0))

t1 = time()
pred = clf.predict(features_test)
print("Prediction time is:","%0.4f"%(time() - t1))

print("Accuracy:","%0.4f"%accuracy_score(labels_test, pred))


