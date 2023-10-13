""" Connect ropes to minimise the cost

arr = [1,2,3,4,5]

way-1:
    [1, 2, 3+4, 5]  =>  [1, 2+7, 5]  => [1, 9+5]    =>  [1+14]
    Tot = 7 + 9 + 14 +  15
        => 45

way-2:
    [1+2, 3, 4, 5]  =>  [3+3, 4, 5] =>  [6+4, 5]    =>  [10+5]
    Tot = 3 + 6 + 10 + 15
        => 34

way-3:
    [1+2, 3, 4, 5]  =>  [3+3, 4, 5] =>  [6, 4+5]    =>  [6+9]
    Tot = 3 + 6 + 9 + 15
        => 33

O/P = 33

Note: Way-3 is giving the minimal cost => 33
"""

import heapq

def connectRopesToMinCost(arr):
    minh = arr[::]
    heapq.heapify(minh)

    cost = 0
    while len(minh) >= 2:
        top = heapq.heappop(minh)
        secondTop = heapq.heappop(minh)
        print(top, secondTop, minh)
        cost += top + secondTop
        heapq.heappush(minh, top+secondTop)
    print(cost)


if __name__ == "__main__":
    arr = [5,3,2,4,1]

    connectRopesToMinCost(arr)




