""" Nearest Greater to Left

arr = [1, 3, 2, 4]
output = [-1. -1, 3, -1]

# Main Concept:
    1. Stack is Empty       ==> -1
    2. stack.top() > arr[i] ==> stack.top()
    3. stack.top() <= arr[i]
        - Pop untill the stack is empty
        - stack.top() > arr[i]
"""

from queue import LifoQueue

def nearestGreaterToLeft(arr, n):
    stack = LifoQueue()
    output = []

    for i in range(n):
        if stack.empty():
            output.append(-1)
        elif not stack.empty() and stack.queue[-1] > arr[i]:
            output.append(stack.queue[-1])
        elif not stack.empty() and stack.queue[-1] <= arr[i]:
            while not stack.empty() and stack.queue[-1] <= arr[i]:
                stack.get()
            if stack.empty():
                output.append(-1)
            else:
                output.append(stack.queue[-1])

        stack.put(arr[i])

    print(output)


if __name__ == "__main__":
    arr = [1, 3, 2, 4]
    # output = [-1, -1, 3, -1]

    nearestGreaterToLeft(arr, len(arr))
