#!/usr/bin/env python


import json
import http.client
import csv
import ast
import urllib.parse


connection = http.client.HTTPSConnection('api.parse.com', 443)
connection.connect()

w = None
with open('output.csv', 'w') as f:
    for i in range(4):
        params = urllib.parse.urlencode({"limit": 1000, "skip": 1000*i})
        connection.request('GET', '/1/classes/Data?%s' % params, '', {
               "X-Parse-Application-Id": "4BwfSJLkrDszyRLdn95mxV4RkYJPcQUmlyxKP0ht",
               "X-Parse-REST-API-Key": "h8uv70eYQFNlQu8nlcoDhYuNm7iXmhZEnMk0rPx4"
             })

        my_dict = ast.literal_eval(connection.getresponse().read().decode())

        if not i:
            w = csv.DictWriter(f, my_dict['results'][0].keys())
            w.writeheader()

        for d in my_dict['results']: 
            w.writerow(d)