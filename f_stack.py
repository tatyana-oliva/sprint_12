class Stack:
    def __init__(self):
        self._data = []
        self._max = None

    def push(self, el):
        self._data.append(int(el))

    def pop(self):
        if self._data:
            self._data.pop()
        else:
            print('error')

    def get_max(self):
        if self._data:
            print(max(self._data))
        else:
            print('None')


if __name__ == '__main__':
    commands_count = int(input())
    stack = Stack()
    for _ in range(commands_count):
        command, *args = input().split()
        method = getattr(stack, command)
        method(args[0]) if args else method()
