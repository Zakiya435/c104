'''a = 23+25+26+30+35+23+46+55
avg = a/8
print(avg)

b = 25,30,35,23,46,55,23,26
b = 23,23,25,26,30,35,46,55
'''

import csv

with open("a.csv","r") as f:
    a = csv.reader(f)
    data_new = list(a)

print(data_new.pop(0))

list_a = []
for i in range(len(data_new)):
    wt = data_new[i][2]
    list_a.append(wt)

print(list_a)

length = len(wt)
abc = 0
for x in list_a:
    abc = abc + float(x)

mean = abc/length
print(mean)