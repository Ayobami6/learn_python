def bubble_sort(data):
    for i in range(len(data) - 1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp

    return data


new_list = [9, 0, 0, 3, 3, 7, 6, 23, 23, 98, 24, 17, 67, 56]
print(bubble_sort(new_list))

# Time Complexity O(n^2)
