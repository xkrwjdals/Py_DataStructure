class PriorityQueue():
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list)==0
    def size(self): return len(self.list)
    def clear(self): self.list = []

    def enqueue(self, item):
        self.list.append(item)

    def findMaxIndex(self):
        if self.isEmpty(): return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.list[i] > self.list[highest]:
                    highest = i
            return highest

    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.list.pop(highest)

    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.list[highest]



