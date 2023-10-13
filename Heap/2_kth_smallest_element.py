""" Kth smallest element

Q) arr = [7, 10, 4, 3, 20, 15]
    k = 3
O/P = 7
Approach)
    k is defined and smallest is defined    ->  use max heap

By sorting  - O(nlogn)
By heap     - O(nlogk)
"""

import heapq

def kthSmallestElement(arr, k):
    maxh = []
    for i in arr:
        # For max heap need to use -ve value so it sort with max value
        heapq.heappush(maxh, -i)
        if len(maxh) > k:
            heapq.heappop(maxh)

    print(maxh)
    print(f"{k}th smallest element: ", -maxh[0])


if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    print(f"arr = {arr}")
    kthSmallestElement(arr, k)


