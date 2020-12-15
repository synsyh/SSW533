"""
SSW533-test by Yuning Sun
8:03 PM 11/30/20
Module documentation: 
"""
import requests
import json
url = 'https://gitee.com/api/v5/orgs/openharmony/repos'
params = {"per_page": 10}
res = requests.get(url=url, params=params)
res = json.loads(res.text)
print()
