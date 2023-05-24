import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from LinkedList import linkedlist as l
import entry as e

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
        node = l.Node(entry)
        node.link = self.table[idx]
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

map = HashChainMap(10)
map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('sequential search', '선형 탐색')
map.insert('game', '게임')
print("탐색 : game --> ", map.search('game'))
print("탐색 : game --> ", map.search('data'))
print("탐색 : game --> ", map.search('structure'))
