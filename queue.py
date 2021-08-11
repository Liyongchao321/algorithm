
class Queue:
    def __init__(self, size):
        self.size = size
        self.space = [None] * size
        self.front = 0
        self.rear = 0

    def enqueue(self, x):
        if (self.rear + 1)%self.size == self.front:
            raise Exception("Out of space")
        self.space[self.rear] = x
        self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        if self.rear == self.front:
            raise Exception("Vide Queue")
        temp = self.space[self.front]
        self.front = (self.front + 1) % self.size
        return temp

    def print_queue(self):
        i = self.front
        while i != self.rear:
            print(self.space[i % self.size])
            i =  i + 1

class PythonQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self,x):
        self.queue.append(x)

    def dequeue(self):
        res = self.queue[0]
        self.queue = self.queue[1:]
        return res

    def print_queue(self):
        print(self.queue)

if __name__ == '__main__':
    # q = Queue(5)
    q = PythonQueue()
    print("********* enqueue *********")
    q.enqueue(0)
    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(6)
    q.enqueue(8)
    q.enqueue(10)
    print("********* print queue *********")
    q.print_queue()
    print("********* dequeue *********")
    print(q.dequeue())
    print(q.dequeue())
    print("********* print queue *********")
    q.print_queue()



