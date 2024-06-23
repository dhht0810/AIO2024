class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack_list = []

    def is_empty(self):
        return len(self.stack_list) == 0

    def is_full(self):
        return len(self.stack_list) == self.capacity

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()

    def push(self, value):
        if self.is_full():
            return False
        self.stack_list.append(value)
        return True

    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]
    
stack_1 = Stack(capacity=5)
stack_1.push(1)
stack_1.push(2)

print(stack_1.is_full())
print(stack_1.pop())
print(stack_1.pop())
print(stack_1.is_empty())