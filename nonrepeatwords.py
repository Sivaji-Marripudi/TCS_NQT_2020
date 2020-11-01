from collections import Counter
s = 'hello world'
c = Counter(s)
l = []
for i,j in c.items():
    if j > 1:
        l.append(i)
print(' '.join(l))
