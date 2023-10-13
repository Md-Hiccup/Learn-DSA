""" K closest number

Q) arr = [5, 6, 7, 8, 9]
    k = 3
    x = 7
O/P = [6, 8]
Approach)
    k is defined    ->  use max heap as we need smallest difference element

"""

import heapq


def kClosestNumber(arr, k, val):
    """
    Find k closest element to a given value
    """
    maxh = []

    for num in arr:
        if num == val:
            continue

        diff = abs(num - val)
        # For max heap need to use -ve value so it sort with max value
        heapq.heappush(maxh, (-diff, num))

        if len(maxh) > k:
            heapq.heappop(maxh)

    print(maxh)
    res = []
    while(len(maxh)>0):
        diff, num = heapq.heappop(maxh)
        res.append(num)

    print(res)



if __name__ == "__main__":

    arr = [5, 6, 7, 8, 9]
    k = 2
    x = 7

    # arr = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
    # k = 4
    # x = 35
    # O/P = [45, 42, 30, 39]

    kClosestNumber(arr, k, x)