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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

data_points = len(enron_data)
print 'Data points in dataset:', data_points
number_of_features = len(enron_data[enron_data.keys()[0]])
print 'Number of features for each person:', number_of_features
pois_from_enron_data = {key: value for key, value in enron_data.iteritems() if value.get('poi')}
print 'Number of POIs from enron_data:', len(pois_from_enron_data)


def read_names():
    poi_from_names_list = {}

    with open("../final_project/poi_names.txt") as f:
        for index, line in enumerate(f):
            if index > 1:
                name_and_is_poi_list = line.strip().split(') ')
                poi_from_names_list[name_and_is_poi_list[1]] = name_and_is_poi_list[0][1]
    return poi_from_names_list


pois_from_names_list = read_names()

print 'Number of POIs from names list:', len(pois_from_names_list)

poi_with_y_from_names_list = {key: value for key, value in pois_from_names_list.iteritems() if value == 'y'}

print 'Number of POIs from names list with y:', len(poi_with_y_from_names_list)

print 'Total value of stock belonging to James Prentice:', enron_data['PRENTICE JAMES']['total_stock_value']

print 'Email messages from Wesley Colwell to persons of interest:', enron_data['COLWELL WESLEY']['from_this_person_to_poi']

print 'Value of stock options exercised by Jeffrey K Skilling:', enron_data['SKILLING JEFFREY K']['exercised_stock_options']

print 'Total payments for LAY KENNETH L:', enron_data['LAY KENNETH L']['total_payments']
print 'Total payments for FASTOW ANDREW S:', enron_data['FASTOW ANDREW S']['total_payments']
print 'Total payments for SKILLING JEFFREY K:', enron_data['SKILLING JEFFREY K']['total_payments']


print 'Number of people with quantified salary:', len({key: value for key, value in enron_data.iteritems() if value.get('salary') != 'NaN'})

print 'Number of people with known emails:', len({key: value for key, value in enron_data.iteritems() if value.get('email_address') != 'NaN'})

num_of_people_without_total_payments = len({key: value for key, value in enron_data.iteritems() if value.get('total_payments') == 'NaN'})
perc_of_people_without_total_payments = num_of_people_without_total_payments / float(data_points)
print 'Percentage of people without quantified salary:', perc_of_people_without_total_payments

num_of_pois_without_total_payments = len({key: value for key, value in pois_from_enron_data.iteritems() if value.get('total_payments') == 'NaN'})
print 'Num of POIs without total payments:', num_of_pois_without_total_payments

for index in range(10):
    enron_data[index] = {'poi': True, 'total_payments': 'NaN'}

print 'new number of people of the dataset:', len(enron_data)
print 'new number of people without total payments:', len({key: value for key, value in enron_data.iteritems() if value.get('total_payments') == 'NaN'})

new_pois = {key: value for key, value in enron_data.iteritems() if value.get('poi')}

print 'new num of pois:', len(new_pois)
print 'new num of pois without total payments:', len({key: value for key, value in new_pois.iteritems() if value.get('total_payments') == 'NaN'})

# for key in pois_from_names_list.keys():
#     uppercaseKey = ' '.join(key.split(', ')).upper()
#     print uppercaseKey
#     if not enron_data.get('uppercaseKey'):
#         print uppercaseKey, 'was not found in enron_data'
