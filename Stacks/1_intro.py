""" Stack

Way of implementing Stack in python
    - list
    - collections.deque
    - queue.LifoQueue
"""

## 1. List
def listStack():
    stack = []

    stack.append('a')
    stack.append('b')
    stack.append('c')

    print('List Stack -', stack)
    print('Top element -', stack[-1])

    a = stack.pop()
    print(a)
    print(stack.pop())
    print(stack.pop())
    # stack.pop()


## 2. collections.deque
def dequeStack():
    from collections import deque
    stack = deque()

    stack.append('a')
    stack.append('b')
    stack.append('c')

    print('Collections.deque Stack - ', stack)
    print('Top element -', stack[-1])

    print(stack.pop())
    b = stack.pop()
    print(b)
    print(stack.pop())


## 3. queue.LifoQueue
def lifoQueueStack():
    from queue import LifoQueue

    stack = LifoQueue()
    stack.put('a')
    stack.put('b')
    stack.put('c')

    print('queue.LifoQueue Stack - ', stack)
    print('Top element -', stack.queue[-1])

    print(stack.get())
    print(stack.get())
    c = stack.get()
    print(c)



if __name__ == "__main__":
    # 1. List
    listStack()

    # 2. Collections.deque
    dequeStack()

    # 3. queue.LifoQueue
    lifoQueueStack()