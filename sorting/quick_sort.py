def quick_sort(items):
    def swap(i, j):
        if i == j:
            return
        temp = items[i]
        items[i] = items[j]
        items[j] = temp

    def partition(left, right):
        pivot = items[right]
        pointer = left - 1

        for i in range(left, right):
            if items[i] < pivot:
                pointer += 1
                swap(i, pointer)

        swap(pointer + 1, right)
        return pointer + 1

    def qs(left, right):
        if left >= right:
            return

        pi = partition(left, right)
        qs(left, pi - 1)
        qs(pi + 1, right)

    qs(0, len(items) - 1)


ll = [10, 80, 30, 90, 40, 50, 70]
quick_sort(ll)
print(ll)
