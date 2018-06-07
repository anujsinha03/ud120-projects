#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    def getKey(item):
        return item[2]
    
    result = list(zip(ages, net_worths, net_worths-predictions))
    result = sorted(result, key=getKey, reverse = True)
    cleaned_data = result[:int(0.9*len(result))]
    
    return cleaned_data

