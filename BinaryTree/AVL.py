import binarytree as bt

def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B

def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

def calc_height_diff(n):
    Left = bt.calc_height(n.left)
    Right = bt.calc_height(n.right)
    return Left - Right

def reBalance(parent):
    hDiff = calc_height_diff(parent)

    if hDiff > 1 :
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else :
            parent = rotateLR(parent)
    elif hDiff < -1 :
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else :
            parent = rotateRL(parent)
    return parent

def insert_avl(parent, node):
    if node.key < parent.key:
        if parent.left != None:
            parent.left = insert_avl(parent.left, node)
        else:
            parent.left = node
        return reBalance(parent)
    elif node.key > parent.key:
        if parent.right != None:
            parent.right = insert_avl(parent.right, node)
        else:
            parent.right = node
        return reBalance(parent)
    else:
        print("중복된 키 에러")

