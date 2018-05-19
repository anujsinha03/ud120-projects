#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]

"""
#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score

clf = [KNeighborsClassifier(4),
       RandomForestClassifier(max_depth=10, n_estimators=10, min_samples_split = 70),
       AdaBoostClassifier(learning_rate = 0.77)]


acc = []
for x in clf:
    x.fit(features_train, labels_train)
    pred = x.predict(features_test)
    print round(accuracy_score(labels_test, pred), 3)

"""
### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
i = 0
for x in clf:
    try:
        plt.figure(i)
        i = i+1
        prettyPicture(x, features_test, labels_test)
        plt.title(x)
    except NameError:
        pass
"""