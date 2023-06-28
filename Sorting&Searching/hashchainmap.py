import entry as e

class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link
class HashChainMap:
    def __init__(self, M):
        self.table = [None]*M # 크기가 M인 테이블을 만든다.
        self.M = M

    def hashFn(self, key):
        sum = 0
        for c in key:
            sum = sum + ord(c) # key의 문자 하나하나를 ord() 함수로 문자->숫자로 바꾸어서 더해줌
        return sum % self.M

    def insert(self, key, value):
        idx = self.hashFn(key)
        entry = e.Entry(key, value)
        node = Node(entry, self.table[idx])
        self.table[idx] = node # 왜 오류?

    def search(self, key):
        idx = self.hashFn(key)
        node = self.table[idx]
        while node is not None:
            if node.data.key == key:
                return node.data
            node = node.link
        return None

    def delete(self, key):
        idx = self.hashFn(key)
        node = self.table[idx]
        before = None
        while node is not None:
            if node.data.key == key:
                if before == None:
                    self.table[idx] = node.link
                else:
                    before.link = node.link
                return
            before = node
            node = node.link

    def display(self, msg):
        print(msg)
        for idx in range(len(self.table)):
            node = self.table[idx]
            if node is not None:
                print("[%2d] -> "%idx, end='')
                while node is not None:
                    print(node.data, end=' -> ')
                    node = node.link
                print()


map = HashChainMap(10)
map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('sequential search', '선형 탐색')
map.insert('game', '게임')
map.insert('binary search', '이진 탐색')
map.display("나의 단어장 : ")
print("탐색 : game --> ", map.search('game'))
print("탐색 : game --> ", map.search('data'))
print("탐색 : game --> ", map.search('structure'))
