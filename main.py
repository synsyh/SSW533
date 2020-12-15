"""
SSW533-test by Yuning Sun
12:03 AM 12/1/20
Module documentation: 
"""
import requests
import json


def get_repos():
    repo_url = 'https://gitee.com/api/v5/orgs/openharmony/repos'
    page = 1
    repo_params = {"per_page": 100, "page": page}
    repo_res = requests.get(url=repo_url, params=repo_params)
    repo_res = json.loads(repo_res.text)
    lens = len(repo_res)
    while lens == 100:
        page += 1
        repo_params["page"] = page
        new_repo_res = requests.get(url=repo_url, params=repo_params)
        new_repo_res = json.loads(new_repo_res.text)
        repo_res += new_repo_res
        lens = len(new_repo_res)
    return repo_res


def get_pulls(repo_res):
    for repo in repo_res:
        repo_name = repo['name']
        url = 'https://gitee.com/api/v5/repos/openharmony/' + repo_name + '/pulls'
        page = 1
        params = {"access_token": "fe852d2fa7720c25c20b6da32219379f", "state": "all", "pre_page": 100, "page": page}
        repo_logs = requests.get(url=url, params=params)
        repo_logs = json.loads(repo_logs.text)
        lens = len(repo_logs)
        while lens == 100:
            page += 1
            params["page"] = page
            new_repo_logs = requests.get(url=url, params=params)
            new_repo_logs = json.loads(new_repo_logs.text)
            repo_logs += new_repo_logs
            lens = len(new_repo_logs)
    return repo_logs
    # for repo_log in repo_logs:
    #     _id = repo_log['id']


def get_commits(repo_res):
    for repo in repo_res:
        repo_name = repo['name']
        url = 'https://gitee.com/api/v5/repos/openharmony/' + repo_name + '/commits'
        page = 1
        params = {"access_token": "fe852d2fa7720c25c20b6da32219379f", "pre_page": 100, "page": page}
        repo_logs = requests.get(url=url, params=params)
        repo_logs = json.loads(repo_logs.text)
        lens = len(repo_logs)
        while lens == 100:
            page += 1
            params["page"] = page
            new_repo_logs = requests.get(url=url, params=params)
            new_repo_logs = json.loads(new_repo_logs.text)
            repo_logs += new_repo_logs
            lens = len(new_repo_logs)
    return repo_logs


repo_res = get_repos()
get_commits(repo_res)
