"""
SSW533-get_repo_test by Yuning Sun
4:20 PM 12/6/20
Module documentation: 
"""
import requests
import json
import numpy as np
from collections import defaultdict


# def get_prs():
#     url = 'https://gitee.com/api/v5/repos/openharmony/kernel_liteos_a/pulls'
#     page = 1
#     params = {"access_token": "fe852d2fa7720c25c20b6da32219379f", "state": "all", "pre_page": 100, "page": page}
#     repo_logs = requests.get(url=url, params=params)
#     with open('prs.txt', 'w') as f:
#         f.write(repo_logs.text)
#
#
# def get_commits():
#     url = 'https://gitee.com/api/v5/repos/openharmony/kernel_liteos_a/commits'
#     page = 1
#     params = {"access_token": "fe852d2fa7720c25c20b6da32219379f", "pre_page": 100, "page": page}
#     repo_logs = requests.get(url=url, params=params)
#     with open('commits.txt', 'w') as f:
#         f.write(repo_logs.text)

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


def get_pulls(url):
    page = 1
    params = {"access_token": "8ca1da03a355df2fa055647553cfe447", "state": "all", "pre_page": 100, "page": page}
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


def get_commits(url):
    page = 1
    params = {"access_token": "8ca1da03a355df2fa055647553cfe447", "pre_page": 100, "page": page}
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


def get_is_employee(prs):
    identification = {}
    employees = set()
    volunteers = set()
    for pr in prs:
        is_employee = True
        labels = pr['labels']
        for label in labels:
            if 'cla' in label['name']:
                is_employee = False
                break

        if is_employee:
            employees.add(pr['user']['id'])
        else:
            volunteers.add(pr['user']['id'])
    identification['employee'] = employees
    identification['volunteer'] = volunteers
    return employees, volunteers


def get_contribution(commits, employees, volunteers):
    code_contributions = defaultdict(int)
    for commit in commits:
        if commit['author']:
            author = commit['author']['id']
            changed_code = commit['stats']['total']
            code_contributions[author] += changed_code
        else:
            if 'huawei' in commit['commit']['author']['email']:
                author = 1
                changed_code = commit['stats']['total']
                code_contributions[author] += changed_code
            else:
                author = 2
                changed_code = commit['stats']['total']
                code_contributions[author] += changed_code
    employees_code = 0
    volunteers_code = 0
    for key, value in code_contributions.items():
        if key in employees:
            employees_code += value
        elif key in volunteers or key == 2:
            volunteers_code += value
        elif key == 7387629 or key == 1:
            employees_code += value
        else:
            employees_code += value
    return employees_code, volunteers_code


def main():
    repos = get_repos()
    code_contribution = {}
    for i, repo in enumerate(repos):
        print(i)
        url = 'https://gitee.com/api/v5/repos/openharmony/' + repo['name'] + '/pulls'
        prs = get_pulls(url)
        url = 'https://gitee.com/api/v5/repos/openharmony/' + repo['name'] + '/commits'
        commits = get_commits(url)
        employees, volunteers = get_is_employee(prs)
        employees_code, volunteers_code = get_contribution(commits, employees, volunteers)
        repo_contribution = {}
        repo_contribution['employees_code'] = employees_code
        repo_contribution['volunteers_code'] = volunteers_code
        code_contribution[repo['name']] = repo_contribution
    with open('results.txt', 'w') as f:
        f.write(str(code_contribution))


def test():
    repos = get_repos()
    commits_len = 0
    pr_len = 0
    for repo in repos:
        url = 'https://gitee.com/api/v5/repos/openharmony/' + repo['name'] + '/pulls'
        prs = get_pulls(url)
        url = 'https://gitee.com/api/v5/repos/openharmony/' + repo['name'] + '/commits'
        commits = get_commits(url)
        commits_len += len(commits)
        pr_len += len(prs)
    print(commits_len)
    print(pr_len)


if __name__ == '__main__':
    test()
