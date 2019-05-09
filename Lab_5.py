#CS2302, Adolfo Flores 80457200, Lab 5, Dr. Olac Fuentes
#TA's Anindita Nath, Maliheh Zargaran
#Last Edit 5/8, Build Binary Search Tree and Hash Table with Chaining and measure similarity

import math
import time

class BST(object):
    # Constructor
    def __init__(self, word, embedding, left=None, right=None):  
        self.word = word
        self.embedding = embedding
        self.left = left 
        self.right = right      

def Height(T):
    if T == None:
        return 0
    return 1 + max(Height(T.left), Height(T.right))

def Insert(T,NewWord, NewEmbedding):
    if T == None:
        T =  BST(NewWord, NewEmbedding)
    elif T.word > NewWord:
        T.left = Insert(T.left,NewWord, NewEmbedding)
    else:
        T.right = Insert(T.right,NewWord, NewEmbedding)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = SmallestL(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T

def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.word == k:
        return T
    if T.word < k:
        return Find(T.right,k)
    return Find(T.left,k)

def Similarity(BST, w1, w2):
    compare1 = Find(BST, w1)
    compare2 = Find(BST, w2)
    dot_product = 0
    mag1 = 0
    mag2 = 0
    for i in range(50):
        dot_product += (compare1.embedding[i]*compare2.embedding[i])
        mag1 += compare1.embedding[i]*compare1.embedding[i]
        mag2 += compare2.embedding[i]*compare2.embedding[i]
    return dot_product/math.sqrt(mag1*mag2)
  
class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        self.num_items = num_items
        for i in range(size):
            self.item.append([])
    
        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k,len(H.item))
    H.item[b].append([k,l]) 
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return b, i, H.item[b][i][1]
    return b, -1, -1
 
def h(s,n):
    r = 0
    for c in s:
        r = (r*255 + ord(c))% n
    return r

print("Type 1 for binary search tree or 2 for hash table with chaining")
data_type = input("Choice: ")
print("Binary Search Tree Results")
num_nodes = 0

if data_type == '1':
    start = time.time()
    bst = None
    file = open('glove.6B.50d.py','r',encoding="utf8")
    for i in file:
        line = i.split()
        if line[0].islower():
            num_list = []
            for j in line[1:]:
                num_list += [float(j)]
            bst = Insert(bst, line[0], num_list)
            num_nodes += 1
    file.close()
    end = time.time()
    file = open('text_file.py','r',encoding="utf8")
    for i in file:
        line = i.split()
        print("Similarity: ", line[0]," ", line[1]," ", Similarity(bst, line[0], line[1]))
    print("Number of Nodes ", num_nodes)
    print("Height ", Height(bst))
    print("Running time for BST build ", end - start," seconds")
if data_type == 2:
    
    file = open('glove.6B.50d.py','r',encoding="utf8")
    for i in file:
        line = i.split()
        if line[0].islower():
            num_list = []
            for j in line[1:]:
                num_list += [float(j)]
             
    file.close()