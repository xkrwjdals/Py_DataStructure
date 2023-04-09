import circuluarQueue as q

class CircularDeque(q.CirculuarQueue):
    def __init__(self, n):
        super().__init__(n)

    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): self.dequeue()
    def getFront(self): return self.peek()

    def addFront(self, item):
        if not self.isFull():
            self.Queue[self.front] = item
            self.front = self.front - 1
            if self.front < 0 : self.front = self.MAX_QSIZE - 1

    def deleteRear(self):
        if not self.isEmpty():
            item = self.Queue[self.rear]
            self.rear = self.rear - 1
            if self.rear < 0 : self.rear = self.MAX_QSIZE - 1
            return item

    def getRear(self):
        return self.Queue[self.rear]