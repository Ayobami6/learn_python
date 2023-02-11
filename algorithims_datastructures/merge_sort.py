items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def mergesort(data):
    if len(data) > 1:
        mid = len(data) // 2
        leftarr = data[:mid]
        rightarr = data[mid:]

        mergesort(leftarr)
        mergesort(rightarr)

        i = 0
        j = 0
        k = 0  # arrays index

        # while arrays has content
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                data[k] = leftarr[i]
                i += 1
            else:
                data[k] = rightarr[j]
                j += 1
            k += 1

        #  if leftarr has values
        while i < len(leftarr):
            data[k] = leftarr[i]
            i += 1
            k += 1

        # if rightarr has values

        while j < len(rightarr):
            data[k] = rightarr[j]
            j += 1
            k += 1


print(items)
mergesort(items)
print(items)
