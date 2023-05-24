import binarytree as bt
import heap as h

d = bt.TNode('D', None, None)
e = bt.TNode('E', None, None)
f = bt.TNode('F', None, None)
c = bt.TNode('C', f, None)
b = bt.TNode('B', d, e)
root = bt.TNode('A', b, c)

print('In-Order : ', end='')
bt.inorder(root)
print('\nPre-Order : ', end='')
bt.preorder(root)
print('\nPost-Order : ', end='')
bt.postorder(root)

heap = h.MaxHeap()
data = [2, 5, 4, 8, 9, 3, 7, 3]
print("[삽입 연산] : " + str(data))
for elem in data :
    heap.insert(elem)
heap.display('[삽입 후] : ')
heap.delete()
heap.display('[삭제 후] : ')
