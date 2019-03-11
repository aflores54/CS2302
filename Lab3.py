#Lab 3 Adolfo Flores, Dr. Olac Fuentes
#CS2302 1:30p.m., Anindita Nath, Maliheh Zargaran
#Last Edited 3/11, BST management algorithms

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):#Builds the BST Nodes
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
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
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')

def PrintBST(T,space):
    # Prints items and structure of BST
    if T is not None:
        PrintBST(T.right,space+'---')
        print(space,T.item, end='')
        PrintBST(T.left,space+'---')
        print()

def SearchIterative(T, k):#Search with out using recursion
    if T is None:#Check if BST is empty
        print("BST is empty")
        return
    temp = T#Navigate BST without changing it
    while temp is not None:
        if k == temp.item:
            print(k, end=' ')
            print("is found")
            return
        elif k < temp.item:#Check which pointer to use
            temp = temp.left
        else:
            temp = temp.right
    print("Item not found")#If key is not found
    
def PrintDepth(T, d):#Prints all the keys at the stated depth
    if T is not None:#won't print if key is empty
        if d == 0:
            print(T.item, end=' ')
        
        else:#Navigate BST until depth reached or empty
            PrintDepth(T.left,d-1)
            PrintDepth(T.right,d-1)    
    
# Code to test the functions above
T = None
A = [10, 4, 15, 2, 8, 12, 18, 1, 3, 5, 9, 7]
for a in A:
    T = Insert(T,a)
    
PrintBST(T,'')
SearchIterative(T, 7)
for i in range(5):#Prints all the keys at different depths
    print("Keys at depth", end=' ')
    print(i, end=': ')
    PrintDepth(T, i)
    print()
    
