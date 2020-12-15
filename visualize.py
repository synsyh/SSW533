"""
SSW533-visualize by Yuning Sun
3:20 PM 12/8/20
Module documentation: 
"""
from collections import defaultdict
import matplotlib.pyplot as plt

with open('trans.txt') as f:
    r = []
    for line in f.readlines():
        d = []
        es = line.strip().split('\t')
        if len(es[3]) == 1:
            month = '0' + es[3]
        else:
            month = es[3]
        if len(es[4]) == 1:
            day = '0' + es[4]
        else:
            day = es[4]
        date = es[2] + month + day
        d.append(date)
        d.append(es[0])
        d.append(es[1])
        r.append(d)
r.sort(key=lambda x: x[0])
r = r[17:]
nr = []
vd = defaultdict(int)
ed = defaultdict(int)
for e in r:
    date = e[0]
    nd = e[0][:6]
    if e[1].startswith('volun'):
        vd[nd] += int(e[-1])
    else:
        ed[nd] += int(e[-1])
keys = []
for i in range(4, 13):
    if i < 10:
        keys.append('20190' + str(i))
    else:
        keys.append('2019' + str(i))
for i in range(1, 12):
    if i < 10:
        keys.append('20200' + str(i))
    else:
        keys.append('2020' + str(i))
el = []
vl = []
for key in keys:
    if key in vd.keys():
        vl.append(vd[key])
    else:
        vl.append(0)
    if key in ed.keys():
        el.append(ed[key])
    else:
        el.append(0)
x_data = keys
y_data = el
y_data2 = vl
# 绘图
plt.bar(x=x_data, height=y_data, label='Employee', width=0.8, color='steelblue', alpha=0.8)
# plt.bar(x=x_data, height=y_data2, width=0.8, label='Volunteer', color='indianred', alpha=0.8)
# 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for x, y in enumerate(y_data):
    plt.text(x, y + 1500, '%s' % y, ha='center', va='bottom')
# for x, y in enumerate(y_data2):
#     plt.text(x, y + 1500, '%s' % y, ha='center', va='top')
# 设置标题
plt.title("Employee Contribution")
# 为两条坐标轴设置名称
# 显示图例
# plt.figure(figsize=(20, 10))
plt.show()
