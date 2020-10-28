time = float(input())
timestamp = [0.00,0.04,0.09,0.15,0.19,0.22]
if time <= 24.00:
    L = [(time+i) for i in timestamp]
elif time > 24.00 and time < 0:
    print('invalid time')
else:
    pass
print(L)