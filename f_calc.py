class Stack:
    def __init__(self):
        self._data = []

    def push(self, el: int):
        self._data.append(el)

    def pop(self):
        self.data.pop()


def main():
    lines = input().split()

s = Stack()
s.push(123)
