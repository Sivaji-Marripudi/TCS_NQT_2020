def check(l):
    i1 = int(input())
    if i1 == 1:
        carnumber = input()
        if len(carnumber) > 6 and len(carnumber) <= 12:
            l.append(carnumber)
        else:
             return 'car number should be 6 characters minium'
        return l
    elif i1 == 2:
        carnumber = input()
        if carnumber in l:
            return l.index(carnumber) + 1
        elif carnumber not in l:
            return 'CAR DOES NOT EXISTS'
    else:
        return 'invalid'
        
a = ['MH04CC2','MH04C2820','MH04BB3232','MH04CC2113','MH04CC2878','MH04BB8','MH04CC2888','MH04CC1313','MH04CC2222','MH04C1201','MH04CC555','MH04C6565','MH0404A7']
print(check(a))