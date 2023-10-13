""" Kth sorted array

Q) arr = [6, 5, 3, 2, 8, 10, 9]
    k = 3
O/P = [2, 3, 5, 6, 8, 9, 10]
Approach)
    k is defined    ->  use min heap as we need smallest frst element

By sorting  - O(nlogn)
By heap     - O(nlogk)
"""

import heapq

def kSortedArray(arr, k):
    """
    Find k sorted array
    """
    minh = []

    for i in arr:
        # For min heap, heapq by default do with min heap
        heapq.heappush(minh, i)
        if len(minh) > k:
            val = heapq.heappop(minh)
            print(val, end=' ')

    while len(minh) > 0:
        val = heapq.heappop(minh)
        print(val, end=' ')



if __name__ == "__main__":

    arr = [6, 5, 3, 2, 8, 10, 9]
    k = 3

    kSortedArray(arr, k)

    print()

