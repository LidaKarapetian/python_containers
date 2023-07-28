#!/usr/bin/python

# w3resource/dictionary 

#Python program to combine two dictionary by adding values for common keys

from collections import Counter

d1 = {'a': 500, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

#variant_1
d = Counter(d1) + Counter(d2)
print(d)

# #variant_2
for k in d2:
        if k in d1:
            d2[k] = d1[k] + d2[k]

for k, v in d1.items():
    if k not in d2:
        d2[k] = v
print(d2)


#Write a Python program to combine values in a list of dictionaries.

ls = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

#variant_1
new_ls = Counter()
for i in ls:
    new_ls[i['item']] += i['amount']
print(new_ls)

#variant_2
from collections import defaultdict

new_ld = defaultdict(int)
for i in ls:
    item = i['item']
    amount = i['amount']
    new_ld[item] += amount

print(new_ld)

#Write a Python program to get the top three items in a shop.

ld = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
ls = ld.values()
s = sorted(ls)[::-1]
print(s[:3])


