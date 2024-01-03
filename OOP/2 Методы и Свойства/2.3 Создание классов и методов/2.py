
class Stack:

    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if len(self.values) == 0:
            print("Empty Stack")
        else:
            removed = self.values.pop()
            return removed

    def peek(self):
        if self.values:
            return self.values[-1]
        else:
            print("Empty Stack")

    def is_empty(self):
        if len(self.values) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.values)

s = Stack()
s.pop()
s.push("777")
s.push("222")
s.push("888")
print(s.peek())
s.pop()
print((s.peek()))
print(s.size())
print(s.is_empty())
