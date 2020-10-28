import itertools
for i in range(4):
    i = input()
    l.append(i)
a = list(itertools.combinations(l,2))
print(' Total matches are {} '.format(len(a)))
for i in a:
    print(i[0] +' .VS. ' +i[1])