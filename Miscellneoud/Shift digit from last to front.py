def shift_left(lst,n):
    return lst[-n:]+lst[:-n]

print(shift_left([12,7,4,6,77],3))




def shiftInPlace(l, n):
    n = n % len(l)
    head = l[:n]
    l[:n] = []
    l.extend(head)
    return l
print(shiftInPlace([1,2,3,4],3))


