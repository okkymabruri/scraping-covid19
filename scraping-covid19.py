#!/usr/bin/env python
# coding: utf-8

import datetime
import json
import urllib.request
import pandas as pd

time = datetime.datetime.now().strftime("%m-%d-%Y %H %M")
url = "https://data.covid19.go.id/public/api/update.json"
response = urllib.request.urlopen(url)
text = response.read()
json_data = json.loads(text)
df = pd.json_normalize(json_data.get('update').get('harian'))
df.to_csv('./data/covid19-id ' + str(time) + '.csv', index=False)