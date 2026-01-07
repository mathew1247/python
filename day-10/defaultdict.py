from collections import defaultdict
a = defaultdict(list)
d=['cat', 'dog', 'cat', 'cat', 'dog', 'bird']
for i in d:
    a[len(i)].append(i)
print(a)