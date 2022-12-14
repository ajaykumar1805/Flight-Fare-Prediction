# -*- coding: utf-8 -*-
"""FFP_feature_transformation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13ezUr0m8SOBVEt8ZEmOxz8ebUEo_7j4I
"""

value_picker_airline = {
    'Air Asia' :                          [0] *11,
    'Air India' :                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'GoAir' :                             [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'IndiGo' :                            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    'Jet Airways' :                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    'Jet Airways Business' :              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    'Multiple carriers' :                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    'Multiple carriers Premium economy' : [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    'SpiceJet' :                          [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    'Trujet' :                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    'Vistara' :                           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    'Vistara Premium economy' :           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
}

value_picker_source = {
    'Bangalore' : [0]*4,
    'Chennai' :   [1, 0, 0, 0],
    'Delhi' :     [0, 1, 0, 0],
    'Kolkata' :   [0, 0, 1, 0],
    'Mumbai' :    [0, 0, 0, 1]
}

value_picker_destination = {
    'Bangalore' :   [0]*4,
    'Cochin' :      [1, 0, 0, 0],
    'Delhi' :       [0, 1, 0, 0],
    'Hyderabad' : [0, 0, 1, 0],
    'Kolkata' :     [0, 0, 0, 1],
}

value_picker_total_stops = {
    '1 stop' :  [0] * 4,
    '2 stops' :  [1, 0, 0, 0],
    '3 stops' :  [0, 1, 0, 0],
    '4 stops' :  [0, 0, 1, 0],
    'non-stop' : [0, 0, 0, 1]
}

def transform_feature(user_input):

  user_input.pop('submit')

  airline = value_picker_airline[ user_input['Airline'] ]
  source = value_picker_source[ user_input['Source'] ]
  destination = value_picker_destination[ user_input['Destination'] ]
  total_stops = value_picker_total_stops[ user_input['Total_Stops']]

  departure_date = user_input['Departure_Date']
  date_splited = departure_date.split('-')
  date_splited.pop(0) 
  date_splited = [ int(i) for i in date_splited ]
  date_splited.reverse() # day and then month

  combined_values = date_splited + airline + source + destination + total_stops

  return list(combined_values)

# user_input = {'Airline': 'Vistara', 'Source': 'Bangalore', 'Destination': 'Delhi', 'Departure_Date': '2021-03-01', 
#               'Total_Stops': 'non-stop', 'submit': ' Calculate Flight Fare '}
# y = transform_feature(user_input)