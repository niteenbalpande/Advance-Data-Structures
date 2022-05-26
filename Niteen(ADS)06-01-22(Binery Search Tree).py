# -*- coding: utf-8 -*-
"""
Created by 203 Inc.

@author: Niteens
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node
def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current
def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key)+ "---", end='')
        inorder(root.right)
root = None
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 2)
root = insert(root, 3)
root = insert(root, 20)
root = insert(root, 10)
root = insert(root, 134)
root = insert(root, 4)
print("Inorder", end=' ')
inorder(root)
print("\nDeleting the node 20")
root = deleteNode(root, 20)
print("New genrated inorder", end=' ')
inorder(root)