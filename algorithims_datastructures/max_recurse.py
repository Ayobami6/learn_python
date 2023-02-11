def max_(data):

    if len(data) == 1:
        return data[0]

    tmp1 = data[0]
    tmp2 = max_(data[1:])

    if tmp1 > tmp2:
        return tmp1
    else:
        return tmp2


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print(max_(items))
