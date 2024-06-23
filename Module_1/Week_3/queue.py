class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue_list = []

    def is_empty(self):
        return len(self.queue_list) == 0

    def is_full(self):
        return len(self.queue_list) == self.capacity

    def dequeue_list(self):
        if self.is_empty():
            return None
        return self.queue_list.pop(0)

    def enqueue_list(self, value):
        if self.is_full():
            return False
        self.queue_list.append(value)
        return True

    def front(self):
        if self.is_empty():
            return None
        return self.queue_list[0]


queue_1 = Queue(capacity=5)
queue_1.enqueue_list(1)
queue_1.enqueue_list(2)

print(queue_1.is_full())

print(queue_1.front())

print(queue_1.dequeue_list())
print(queue_1.dequeue_list())

print(queue_1.is_empty())
