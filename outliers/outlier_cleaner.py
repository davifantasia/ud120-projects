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

    # Get dict of errors
    error_dict = {}

    for index, pred in enumerate(predictions):
        error_dict[index] = pred[0] - net_worths[index][0]

    # Get integer of 10% of data points
    ten_percent_count = int(len(predictions) * 0.1)

    # Remove maxuimum residual errors ten_percent_count times
    for i in range(ten_percent_count):
        max_error = ('', 0)

        # find the current maximum error value
        for key, value in error_dict.iteritems():
            if abs(value) > abs(max_error[1]):
                max_error_list = list(max_error)
                max_error_list[0] = key
                max_error_list[1] = value
                max_error = tuple(max_error_list)

        del error_dict[max_error[0]]

    for key, value in error_dict.iteritems():
        cleaned_data.append((ages[key][0], net_worths[key][0], value))

    return cleaned_data

