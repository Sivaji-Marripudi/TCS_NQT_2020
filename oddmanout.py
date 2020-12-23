L = []
test_cases = int(input('enter test cases : '))
for i in range(test_cases):
    j = int(input('enter the length : '))
    l = []
    for i in range(j):
        a = int(input('enter the numbers : '))
        l.append(a)
    L.append(l)
L1 = []
for i in L:
    d = {'evens':[],'odds':[]}
    for j in i:
        if j % 2 == 0:
            d['evens'].append(j)
        else:
            d['odds'].append(j)
    L1.append(d)
L2 = []
for i in L1:
    for a,b in i.items():
        if len(b) == 1:
            L2.extend(b)
R = list(zip(L,L2))
for i in R:
    j = i[0].index(i[1])
    print(j)
