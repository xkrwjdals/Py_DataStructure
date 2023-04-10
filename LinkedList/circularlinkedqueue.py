import linkedlist as l

class CircularLinkedQueue:
    def __init__(self):
        self.tail = None

    def isEmpty(self): return self.tail==None
    def clear(self): self.tail = None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data

    def enqueue(self, item):
        node = l.Node(item, None)
        if self.isEmpty(): # case 1 : 큐가 공백상태일 때,
            node.link = node # 원형큐이기 때문에, 자기 자신을 가리킨다.
            self.tail = node # tail은 방금 추가한 node를 가리킨다.
        else : # case 2 : 큐가 공백이 아닐 때(데이터가 있을 때), 마지막에 추가한다.
            node.link = self.tail.link # (step 2)
            self.tail.link = node # step 3
            self.tail = node # step 4

    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail: # case 1 : 하나만 있는 큐일 경우
                self.tail = None
            else:
                self.tail.link = self.tail.link.link # case 2 : 여러 개의 항목일 경우
            return data

    def size(self):
        if self.isEmpty(): return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node = node.link
                count += 1
            return count
        