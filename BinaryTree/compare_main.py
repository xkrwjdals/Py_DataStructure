import AVLMap
import BSTMap
import binarytree as bt

node = [0,1,2,3,4,5,6,7,8,9]
map = AVLMap.AVLMap()

for i in node:
    map.insert(i)
    map.display("AVL(%d): "%i)

print(" 노드의 개수 = %d" % bt.count_node(map.root))
print(" 단말의 개수 = %d" % bt.count_leaf(map.root))
print(" 트리의 높이 = %d" % bt.calc_height(map.root))

map2 = BSTMap.BSTMap()

for i in node:
    map2.insert(i)
    map2.display("BST(%d): "%i)

print(" 노드의 개수 = %d" % bt.count_node(map2.root))
print(" 단말의 개수 = %d" % bt.count_leaf(map2.root))
print(" 트리의 높이 = %d" % bt.calc_height(map2.root))
