items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def find_item(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i

    return None


print(find_item(items, 8))
print(find_item(items, 90))

print(7//2)
