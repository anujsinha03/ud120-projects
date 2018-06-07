#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL", 0)
data = featureFormat(data_dict, features)


sol = [(s,data_dict[s]['salary'],data_dict[s]['bonus'] ) for s in sorted(list(data_dict.keys())) if ((data_dict[s]['salary'] and data_dict[s]['bonus']) != "NaN")]
def getKey(item):
    return item[1], 
print (sorted(sol, key=getKey, reverse = True)[:5])

def getKey1(item):
    return item[2]
print ""
print (sorted(sol, key=getKey1, reverse = True)[:5])

### your code below
for point in data:
    plt.scatter(point[0], point[1])
plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()




