d = {1:80.0,2:130.0,3:100.0,4:80.0,5:90.0,6:110.0,7:120.0,8:140.0,9:70.0,
    10:80.0,11:130.0,12:160.0,13:70.0,14:60.0,15:40.0,16:50.0,17:30.0,
    18:40.0,19:160.0,20:150.0}
l = []
while True:
    order = int(input('enter order number : '))
    quantity = int(input('enter quantity : '))
    if order >= 21:
        print('order not available')
    else:
        l.append(d[order] * quantity)
        more = input('Do you want more order :').lower()
        if more == 'yes':
            continue
        elif more == 'no':
            break
        else:
            pass
print('Total Bill is : ',sum(l),' INR')