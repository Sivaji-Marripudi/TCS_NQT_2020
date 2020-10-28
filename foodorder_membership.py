items = {1:50,2:100,3:40,4:200,5:300}
orders = list(map(int,input().split()))
quantities = list(map(int,input().split()))
membership = input().lower()
if len(orders) == len(quantities):
    if any([i for i in orders if i >= 6]):
        print('order not available')
    elif all([i for i in orders if i <= 5]):
        c = [(items[i]) for i in orders]
        c1 = list(zip(c,quantities))
        cost = 0
        for i in c1:
            cost += (i[0] * i[1])
        print('the total price is {} INR'.format(float(cost)))   
else:
    print('invalid input')
if membership == 'y':
    if cost >= 1000:
        final_price = (cost) - (cost * 15) / 100
        print('Final price is {} INR'.format(final_price))
    elif cost <= 999:
        final_price = (cost) - (cost * 5) / 100
        print('Final price is {} INR'.format(final_price))
    else:
        pass
else:
    if cost >= 1000:
        final_price = (cost) - (cost * 10) / 100
        print('Final price is {} INR'.format(final_price))
    elif cost <= 999:
        final_price = (cost) -  (cost * 5) / 100
        print('Final price is {} INR'.format(final_price))
    else:
        pass