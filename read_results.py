"""
SSW533-read_results by Yuning Sun
5:34 PM 12/7/20
Module documentation: 
"""
import matplotlib.pyplot as plt

with open('results.txt') as f:
    results = eval(f.read())
    a = dict()
    results = sorted(results.items(), key=lambda x: x[1]['volunteers_code'], reverse=True)
    results = list(results)[:26]
    print()
    all_ec = 0
    all_vc = 0
    all_code = 0
    max_vc = 0
    for result in results:
        repo_name = result[0]
        contri = result[1]
        ec = contri['employees_code']
        vc = contri['volunteers_code']
        if repo_name.startswith('third_party') or repo_name.startswith('vendor'):
            all_code += ec + vc
        else:
            if vc > max_vc:
                max_vc = vc
                max_vc_ec = ec
                max_repo = repo_name
            all_code += ec + vc
            all_vc += vc
        if repo_name.startswith('doc'):
            doc_vc = vc
    print(all_vc / all_code)
    print(max_vc)
    print(max_vc_ec)
    print(max_repo)
