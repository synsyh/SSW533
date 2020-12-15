"""
SSW533-get_logs by Yuning Sun
11:54 PM 11/30/20
Module documentation: 
"""
import json
import requests

repo_name = 'kernel_liteos_a'
url = 'https://gitee.com/api/v5/repos/openharmony/' + repo_name + '/pulls'
params = {"access_token": "5b304d9b1353007d8891cc3ea2c84841", "state": "merged"}
res = requests.get(url=url, params=params)
res = json.loads(res.text)
print()
