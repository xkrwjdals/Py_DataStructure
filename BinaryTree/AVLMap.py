import BSTMap
import BSTNode
import binarytree as bt
import AVL as avl

class AVLMap(BSTMap.BSTMap):
    def __init__(self):
        super().__init__()

    def insert(self, key, value=None):
        n = BSTNode.BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            self.root = avl.insert_avl(self.root, n)

    def display(self, msg = 'AVL Map :'):
        print(msg, end='')
        BSTNode.levelorder(self.root)
        print()

node = [7,8,9,2,1,5,3,6,4]
map = AVLMap()

for i in node:
    map.insert(i)
    map.display("AVL(%d): "%i)

print(" 노드의 개수 = %d" % bt.count_node(map.root))
print(" 단말의 개수 = %d" % bt.count_leaf(map.root))
print(" 트리의 높이 = %d" % bt.calc_height(map.root))
