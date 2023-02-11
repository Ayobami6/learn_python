
def is_sorted(dataset):
    return all([dataset[i] <= dataset[i+1] for i in range(len(dataset) - 1)])


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

print(is_sorted(items1))
print(is_sorted(items2))
