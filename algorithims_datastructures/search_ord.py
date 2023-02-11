items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def binary_search(data, value):
    datasize = len(data) - 1

    loweridx = 0
    upperIdx = datasize

    while loweridx <= upperIdx:

        midPt = (datasize + loweridx) // 2

        if data[midPt] == value:
            return midPt

        if value > data[midPt]:
            loweridx = midPt + 1
        else:
            upperIdx = midPt - 1

    return None


print(binary_search(items, 23))
print(binary_search(items, 87))
print(binary_search(items, 250))
