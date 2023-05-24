# 힙은 보통 배열을 이용하여 구현
class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap.append(0) # 리스트의 0번항목은 사용하지 않음

    def size(self): return len(self.heap) - 1
    def isEmpty(self): return self.size() == 0
    def Parent(self, i): return self.heap[i//2]
    def Left(self, i): return self.heap[i*2]
    def Right(self, i): return self.heap[i*2+1]
    def display(self, msg = '힙 트리 : '):
        print(msg, self.heap[1:])

    def insert(self, n):
        self.heap.append(n)
        i = self.size()
        while(i != 1 and n > self.Parent(i)):
            self.heap[i] = self.Parent(i)
            i = i // 2
        self.heap[i] = n

    def delete(self):
        if not self.isEmpty():
            hroot = self.heap[1]
            self.heap[1] = self.heap[self.size()]
            i = 1
            while (self.heap[i] < self.size()):
                if (self.heap[i] < self.Left(i) and self.Left(i) > self.Right(i)):
                    self.heap[i], self.heap[i*2] = self.heap[i*2], self.heap[i]
                elif (self.heap[i] < self.Right(i) and self.Right(i) > self.Left(i)):
                    self.heap[i], self.heap[i*2+1] = self.heap[i*2+1], self.heap[i]
                i = i * 2
            self.heap.pop(-1)
            return hroot

