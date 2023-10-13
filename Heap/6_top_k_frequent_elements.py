""" Top K frequent elements

Q) arr = [1, 1, 1, 3, 2, 2, 4]
    k = 2
O/P = [2, 1] or [1, 2]
Approach)
    find top k frequent elements
"""

import heapq

def topKFrequentElements(arr, k):
    hmap = {}
    for num in arr:
        hmap[num] = hmap.get(num, 0) + 1

    minh = []
    for key, freq in hmap.items():
        # For min heap, heapq by default do with min heap
        heapq.heappush(minh, (freq, key))
        if len(minh) > k:
            heapq.heappop(minh)

    while len(minh) > 0:
        freq, key = heapq.heappop(minh)
        print(key, end=' ')

if __name__ == "__main__":

    arr = [1, 1, 1, 3, 2, 2, 4]
    k = 2

    topKFrequentElements(arr, k)

