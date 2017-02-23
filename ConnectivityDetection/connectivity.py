import collections
f = open('datasets.txt','r')
case = int(f.readline().split('\n')[0])
for i in range(case):
    cc = f.readline()
    n = int(cc.split('\t')[0])
    p = int(cc.split('\t')[1].split('\n')[0])
    group = [num for num in range(n)]
    print(len(group))
    for j in range(p):
        link = f.readline()
        a = int(link.split('\t')[0])
        b = int(link.split('\t')[1].split('\n')[0])
        item = group[b-1]
        for k in range(n):
            if group[k]==item:
                group[k] = group[a-1]
    print(collections.Counter(group))