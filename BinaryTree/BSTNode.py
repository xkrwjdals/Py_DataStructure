import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Queue import circuluarQueue as cq

# 이진탐색트리
# 1. 모든 노드는 유일한 키를 가진다.
# 2. 왼쪽 서브트리의 키들은 루트의 키보다 작다.
# 3. 오른쪽 서브트리의 키들은 루트의 키보다 크다.
# 4. 왼쪽과 오른쪽 서브트리도 이진탐색트리이다.

class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def search_bst(n, key): # 순환함수로 이진탐색트리 탐색연산
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

def search_bst_iter(n, key):
    while n != None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        elif key > n.key:
            n = n.right
    return None

# 삽입연산은 탐색에 실패한 위치에 넣는다.
def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else:
        return False

# 값을 이용한 탐색
def search_value_bst(n, value):
    if n == None: return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value) # 왼쪽 서브트리부터 탐색
    if res is not None: # 왼족 서브트리에서 탐색 성공했다면,
        return res # 그 값을 리턴
    else: # 왼쪽 서브트리에서 탐색하지 못했다면,
        return search_value_bst(n.right, value) # 오른쪽 서브트리 탐색 호출!

# 삭제연산은 3가지의 경우로 나뉜다.
# 1. 단말 노드 삭제 -> Parent -> node 의 연결을 끊는다.
# 2. 삭제 노드가 왼쪽이나 오른쪽 서브 트리만 가지고 있는 경우 -> parent에 child node를 연결한다.
# 3. 삭제 노드가 두 개의 서브트리를 가지고 있는 경우
# -> 삭제할 Node의 오른쪽 자식중 가장 작은값을 Parent Node가 가리키도록 한다.
# 또는 삭제할 노드의 왼쪽 자식 중 가장 큰값을 Parent Node가 가리키게 한다.
def delete_bst_case1(parent, node, root):
    if parent is None:
        root = None
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None
    return root

def delete_bst_case2(parent, node, root):
    if node.left is not None:
        child = node.left
    else:
        child = node.right
    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child
    return root

def delete_bst_case3(parent, node, root):
    succp = node
    succ = node.right
    while (succ.left != None):
        succp = succ
        succ = succ.left
    if (succ.left == succ):
        succp.left = succ.right
    else:
        succp.right = succ.right

    node.key = succ.key
    node.value = succ.value
    node = succ

    return root # root가 가리키는 객체의 내용만 바뀌고 객체 자체가 변경되지 않기 때문에 root를 반호나할 필요는 없지만 일관성을 위해 반환

def delete_bst(root, key):
    if root == None: return None

    parent = None
    node = root

    while node != None and node.key != key:
        parent = node
        if key < node.key : node = node.left
        else: node = node.right

    if node == None: return None
    if node.left == None and node.right == None:
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None:
        root = delete_bst_case2(parent, node, root)
    else:
        root = delete_bst_case3(parent, node, root)
    return root

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)

def levelorder(root):
    queue = cq.CirculuarQueue(20)
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
