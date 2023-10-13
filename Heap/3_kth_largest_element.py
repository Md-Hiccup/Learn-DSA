""" Kth smallest element

Q) arr = [7, 10, 4, 3, 20, 15]
    k = 3
O/P = [10, 15, 20]
Approach)
    k is defined and largest is defined    ->  use min heap

By sorting  - O(nlogn)
By heap     - O(nlogk)
"""
import heapq


def kthLargestElement(arr, k):
    minh = []
    for i in arr:
        # For min heap, heapq by default do with min heap
        heapq.heappush(minh, i)
        if len(minh) > k:
            heapq.heappop(minh)

    print(f"{k} largest element: ", end=' ')
    for i in minh:
        print(i, end=' ')

if __name__ == "__main__":

    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    print(f"arr = {arr}")
    kthLargestElement(arr, k)