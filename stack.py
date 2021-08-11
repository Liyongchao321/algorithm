

class FakeStack:
    def __init__(self, size):
        self.size = size
        self.space = [None] * size
        self.top = 0

    def push(self, x):
        if self.top > self.size-1:
            raise Exception("out of space")
        self.space[self.top] = x
        self.top = self.top + 1

    def pop(self):
        res = self.space[self.top-1]
        self.top = self.top - 1
        return res

    def print_stack(self):
        print(self.space[:self.top])

class PythonStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def print_stack(self):
        print(self.stack)
    


if __name__ == '__main__':
    # s = FakeStack(5)
    s = PythonStack()
    print('********** push *********')
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    # s.push(6)
    print("******* print stack ********")
    s.print_stack()
    print('********** pop *********')
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print("******* print stack ********")
    s.print_stack()