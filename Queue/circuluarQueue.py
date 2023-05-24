class CirculuarQueue:
    def __init__(self, n):
        self.MAX_QSIZE = n
        self.Queue = [None]*self.MAX_QSIZE
        self.front = self.rear = 0

    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front == (self.rear+1)%self.MAX_QSIZE
    def clear(self):
        self.front=self.rear

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%self.MAX_QSIZE
            self.Queue[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%self.MAX_QSIZE
            return self.Queue[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.Queue[(self.front+1)%self.MAX_QSIZE]

    def size(self):
        return(self.rear - self.front + self.MAX_QSIZE) % self.MAX_QSIZE

    def display(self):
        out = []
        if self.front < self.rear:
            out = self.Queue[self.front+1:self.rear+1]
        else:
            out = self.Queue[self.front+1:self.MAX_QSIZE] + self.Queue[0:self.rear+1]
        print("[f=%s, r=%d] ==> "%(self.front, self.rear), out)
