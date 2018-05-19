#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

##### How many data points (people) are in the dataset?
print len(enron_data) 

##### For each person, how many features are available?
print len( enron_data["SKILLING JEFFREY K"].keys()) 

##### The “poi” feature records whether the person is a person of interest, according to our definition. How many POIs are there in the E+F dataset?
print len( [1 for person in enron_data if enron_data[person]['poi'] ] ) 

##### What is the total value of the stock belonging to James Prentice?
print [s for s in enron_data.keys() if "PRENTICE" in s] 
print enron_data['PRENTICE JAMES'].keys()
print enron_data['PRENTICE JAMES']['total_stock_value'] 

##### How many email messages do we have from Wesley Colwell to persons of interest?
print [s for s in enron_data.keys() if "WESLEY" in s] 
print enron_data['COLWELL WESLEY']['from_this_person_to_poi'] 

##### What’s the value of stock options exercised by Jeffrey Skilling?
print [s for s in enron_data.keys() if "SKILLING" in s] 
print enron_data['SKILLING JEFFREY K']['exercised_stock_options'] 

##### Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)? 
##### How much money did that person get?
sol = [(s,enron_data[s]['total_payments']) for s in sorted(list(enron_data.keys())) if (('LAY' in s) or ('SKILLING' in s) or ('FASTOW' in s))]
def getKey(item):
    return item[1]
print (max(sol, key=getKey))

####If unfilled value of a dataset, it will be represent as NaN

##### How many folks in this dataset have a quantified salary? What about a known email address?
print len([(s, enron_data[s]['salary']) for s in list(enron_data.keys()) if (enron_data[s]['salary'] != 'NaN')])
print len([(s, enron_data[s]['salary']) for s in list(enron_data.keys()) if (enron_data[s]['email_address'] != 'NaN')])

#####How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? What percentage of people in the dataset as a whole is this?
num = len([s for s in list(enron_data.keys()) if (enron_data[s]['total_payments'] == 'NaN')])
percent = (num*100*1.0)/len(enron_data)
print "percent: ", round(percent,0)

#####How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this?
num = len([s for s in list(enron_data.keys()) if (enron_data[s]['total_payments'] == 'NaN' and enron_data[s]['poi'] == True)])

##### What is the new number of people of the dataset? What is the new number of folks with “NaN” for total payments?
print len( [ enron_data[person]['total_payments'] for person in enron_data if enron_data[person]['total_payments'] =='NaN' ] ) # 31 
print len(enron_data) # 156
 
 
 
 
 
 
 
 