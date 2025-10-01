class Stack:
    def __init__(self): self.stack : list[any] = []

    def is_empty(self) -> bool: return len(self.stack) == 0

    def peek(self) -> any:
        if self.is_empty(): return "Stack is Empty! {}".format(self.stack)
        return self.stack[len(self.stack) - 1]
    
    def push(self , item : any) -> None: self.stack.append(item)

    def pop(self) -> any: 
        if self.is_empty(): return "Stack is Empty! {}".format(self.stack)
        item = self.stack[len(self.stack) - 1]
        self.stack.remove(item)
        return item
    
    def size(self) -> int: return len(self.stack)




s = Stack()

s.push("Hello World!")
s.push(3)
s.push(1.2)
s.push("1")

print("Size after push: {}".format(s.size()))
print("Top element: {}".format(s.peek()))

print("Pop:{}".format(s.pop()))
print("Pop:{}".format(s.pop()))
print("Pop:{}".format(s.pop()))
print("Pop:{}".format(s.pop()))

print("Is empty? {}".format(s.is_empty()))
print("Pop from empty: {}".format(s.pop()))