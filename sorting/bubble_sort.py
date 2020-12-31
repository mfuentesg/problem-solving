def bubble_sort(elements):
    for i in range(len(elements)):
        for j in range(i, len(elements)):
            if elements[i] > elements[j]:
                temp = elements[i]
                elements[i] = elements[j]
                elements[j] = temp
    return elements


print(bubble_sort([500, 2, -2, 200, 60, 5, 0]))
