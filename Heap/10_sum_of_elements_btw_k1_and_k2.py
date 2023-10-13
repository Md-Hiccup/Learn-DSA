""" Sum of Elements between k1 smallest and k2 smallest numbers

arr = [1, 3, 12, 5, 15, 11]
k1 = 3
k2 = 6
O/P = 23

after sorting arr = [1, 3, 5, 11, 12, 15]
    - 3rd smallest = 5
    - 6th smallest = 15
    - b/w 3rd and 6th smallest elements sum = 11 + 12 => 23

"""

import heapq

def kthSmallest(arr, k):
    maxh = []

    for num in arr:
        heapq.heappush(maxh, -num)
        if len(maxh) > k:
            heapq.heappop(maxh)
    print(maxh)
    return -maxh[0]

def sumOfElementsBtwK1Andk2(arr, k1, k2):
    first = kthSmallest(arr, k1)
    second = kthSmallest(arr, k2)

    total = 0
    for num in arr:
        if num > first and num < second:
            total += num

    print(total)


if __name__ == "__main__":
    arr = [1, 3, 12, 5, 15, 11]
    k1 = 3
    k2 = 6

    # arr = [20, 8, 22, 4, 12, 10, 14]
    # k1 = 3
    # k2 = 6
    # Output = 26

    sumOfElementsBtwK1Andk2(arr, k1, k2)
