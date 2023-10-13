""" Frequency Sort
arr = [1, 1, 1, 3, 2, 2, 4]

Sort this arr based on frequency

Output = [1, 1, 1, 2, 2, 3, 4]
"""

import heapq

def frequencySort(arr):
    hmap = {}
    for num in arr:
        hmap[num] = hmap.get(num, 0) + 1

    maxh = []
    for k, v in hmap.items():
        # For max heap need to use -ve value so it sort with max value
        heapq.heappush(maxh, (-v, k))

    print(maxh)
    while len(maxh) > 0:
        freq, num = heapq.heappop(maxh)
        freq = -freq
        while freq > 0:
            print(num, end=' ')
            freq -= 1


if __name__ == "__main__":

    arr = [1, 1, 1, 3, 2, 2, 4]

    # arr = [2, 5, 2, 8, 5, 6, 8, 8]
    # O/P = [8, 8, 8, 2, 2, 5, 5, 6]
    frequencySort(arr)