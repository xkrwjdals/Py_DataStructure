import BSTNode as btn
import binarytree as bt

class BSTMap():
    def __init__(self):
        self.root = None

    def isEmpty(self): return self.root == None
    def clear(self): self.root = None
    def size(self): return bt.count_node(self.root)
    def search(self, key): return btn.search_bst(self.root, key)
    def searchValue(self, key): return btn.search_value_bst(self.root, key)

    def insert(self, key, value=None):
        n = btn.BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            btn.insert_bst(self.root, n)

    def delete(self, key):
        self.root = btn.delete_bst(self.root, key)

    def display(self, msg = 'BSTMap :'):
        print(msg, end='')
        btn.inorder(self.root)
        print()

map = BSTMap()
data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]

print("[삽입 연산] : ", data)
for key in data :
    map.insert(key)
map.display("[중위 순회] : ")

if map.search(26) != None : print("[탐색 26] : 성공")
else : print("[탐색 26] : 실패")

if map.search(25) != None : print("[탐색 25] : 성공")
else : print("[탐색 25] : 실패")

map.delete(3)
map.display("[삭제 3] : ")
map.delete(68)
map.display("[삭제 68] : ")
map.delete(18)
map.display("[삭제 18] : ")