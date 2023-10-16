""" Nearest Greater to Right

arr = [1, 3, 2, 4]
O/P = [3, 4, 4, -1]

arr = [1, 3, 0, 0, 1, 2, 4]
O/P = [3, 4, 1, 1, 2, 4, -1]


# Main Concept:
    1. Stack is Empty       ==> -1
    2. stack.top() > arr[i] ==> stack.top()
    3. stack.top() <= arr[i]
        - Pop untill the stack is empty
        - stack.top() > arr[i]
"""

from collections import deque

def nearestGreaterToRight(arr, n):
    stack = deque()
    output = []

    for i in range(n-1, -1, -1):
        if len(stack) == 0:
            output.append(-1)
        elif len(stack) > 0 and stack[-1] > arr[i]:
            output.append(stack[-1])
        elif len(stack) > 0 and stack[-1] <= arr[i]:
            while (len(stack) > 0 and stack[-1] <= arr[i]):
                stack.pop()
            if len(stack) == 0:
                output.append(-1)
            else:
                output.append(stack[-1])
        stack.append(arr[i])

    output = output[::-1]
    print(output)

if __name__ == "__main__":

    arr = [1, 3, 2, 4]
    # output = [3, 4, 4, -1]

    # arr = [1, 3, 0, 0, 1, 2, 4]
    # output = [3, 4, 1, 1, 2, 4, -1]

    nearestGreaterToRight(arr, len(arr))