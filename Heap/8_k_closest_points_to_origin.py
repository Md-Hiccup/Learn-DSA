""" K Closest Points to Origin

arr = [
    [1, 3],
    [-2, 2],
    [5, 8],
    [0, 1]
]
k = 2
O/P = (-2,2), (0,1)
"""

import heapq

def kClosestPointsToOrigin(arr, k):
    maxh = []

    for i in range(len(arr)):
        dist = pow(arr[i][0], 2) + pow(arr[i][1], 2)
        # For max heap need to use -ve value so it sort with max value
        heapq.heappush(maxh, (-dist, (arr[i][0], arr[i][1])))
        if len(maxh) > k:
            heapq.heappop(maxh)

    print(maxh)
    while len(maxh) > 0:
        dist, (x, y) = heapq.heappop(maxh)
        print(f'({x},{y}) ', end=" ")

if __name__ == "__main__":

    arr = [
        [1, 3],
        [-2, 2],
        [5, 8],
        [0, 1]
    ]
    k = 2

    kClosestPointsToOrigin(arr, k)
