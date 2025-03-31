"""
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

MyCircularQueue(k) Initializes the object with the size of the queue to be k.
int Front() Gets the front item from the queue. If the queue is empty, return -1.
int Rear() Gets the last item from the queue. If the queue is empty, return -1.
boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
boolean isEmpty() Checks whether the circular queue is empty or not.
boolean isFull() Checks whether the circular queue is full or not.
You must solve the problem without using the built-in queue data structure in your programming language. 
"""
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.capacity = k
        self.head = 0
        self.count = 0

    # append()
    def enQueue(self, value: int) -> bool:
        if self.count == self.capacity:
            return False
        # initially, tail=head, when count = 0
        new_tail = (self.head + self.count) % self.capacity
        self.queue[new_tail] = value
        self.count += 1
        return True

    # popleft()
    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    # peek()
    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.head]

    # peek tail value
    def Rear(self) -> int:
        if self.count == 0:
            return -1
        existing_tail = (self.head + self.count - 1) % self.capacity
        return self.queue[existing_tail]

    def isEmpty(self) -> bool:
        return self.count == 0


    def isFull(self) -> bool:
        return self.count == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()