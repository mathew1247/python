from collections import defaultdict
a=['cat', 'dog', 'cat', 'cat', 'dog', 'bird']  ## words of list
d=defaultdict(list) ## creating default dictionary
for i in a:
    key = ''.join(sorted(i)) ## sort and then join the words 
    d[key].append(i) ## append the sorted word to the original word
print(d)