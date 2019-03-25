#Lab 4 Adolfo Flores, Dr. Olac Fuentes
#CS2302 1:30p.m., Anindita Nath, Maliheh Zargaran
#Last Edited 3/25, B-Tree management algorithms

class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
        
        
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])
        
#Lab algorithms from here on 
def Height(T):#function for finding the height with case for empty B-Tree
    if T.isLeaf:
        return 0
    elif T is None:
        return -1
    return 1 + Height(T.child[0])

def Extract(T, S):#Builds new sorted list with all the elements of B-Tree
    if T.isLeaf:
        S = S + T.item#S is the new List and uses concatination to build
    else:
        for i in range(len(T.item)):
            S = Extract(T.child[i], S)#Ensures S is maintaned through each recursive call
            S = S + [T.item[i]]#Concatenate elements from non-Leaf nodes
        S = Extract(T.child[len(T.item)], S)
    return S
    
def MinAtDepth(T, d):#Finds smallest element at specified depth 'd'
    if d == 0:
        print('Smallest number at specified depth is ', end='')
        print(T.item[0])
        return
    elif T is None:
        print('B Tree is empty')
        return
    elif T.isLeaf and d != 0:
        print('depth does not exist')
        return
    else:
        MinAtDepth(T.child[0], d-1)

def MaxAtDepth(T, d):#Finds largest element at specified depth 'd'
    if d == 0:
        print('Largest number at specified depth is ', end='')
        print(T.item[len(T.item)-1])
        return
    elif T is None:
        print('B Tree is empty')
        return
    elif T.isLeaf and d != 0:
        print('depth does not exist')
        return
    else:
        MaxAtDepth(T.child[len(T.item)], d-1)
        
def NodesAtDepth(T, d):#Counts how many nodes at depth 'd'
    if d == 0:#if depth is found, adds 1 to counter
        return 1
    elif T.isLeaf and d != 0:#if depth does not exist keeps counter at 0
        return 0
    else:
        count = 0#my counter
        for i in range(len(T.item)+1):#Loop to traverse to all of the Nodes children if exists
            count += NodesAtDepth(T.child[i], d-1)#Keeps track of counter value
        return count
    
def PrintAtDepth(T, d):#Prints all elements at depth 'd' as sets of lists
    if d == 0:
        print(T.item, end='')#Prints the Node or Leaf as a list [....][.....]
    elif T is None:
        print('B Tree is empty')
    elif T.isLeaf and d != 0:
        print('depth does not exist')
        return
    else:
        for i in range(len(T.item)+1):
            PrintAtDepth(T.child[i], d-1)

def FullNodes(T):#Counts how many non-Leaf Nodes that are full (max_items)
    if T.isLeaf:#stops recursive calls and won't count if Leaf
        return 0
    else:
        count = 0
        for i in range(len(T.item)+1):
            count += FullNodes(T.child[i])
            if IsFull(T):#if a Node and full, adds 1
                count += 1
        return count
    
def FullLeaves(T):#Counts how many Leaf Nodes that are full (max_items)
    if T.isLeaf:#if a Leaf and full, adds 1 and stops recursive calls
        if IsFull(T):
            return 1
        else:# if a leaf but not full, just stops recursive calls
            return 0
    else:
        count = 0
        for i in range(len(T.item)+1):
            count += FullLeaves(T.child[i])
        return count

def KeyAtDepth(T, k, h):#Finds depth 'd' of specified key 'k'
    if k in T.item:
        return 0
    if T.isLeaf:
        return (h+1)*(-1)#h is the height and is needed return -1 if key is not found
    d = 0
    d += 1 + KeyAtDepth(T.child[FindChild(T,k)], k, h)#keeps adding 1 until key is found or subtracts height + 1
    return d                                          #making -1 if key does not exist

#L is a general list of elements
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6, 125, 210, -1, -5, -4]
T = BTree()#Empty B-Tree
for i in L:#loop that inserts elements of 'L' into B-Tree 'T'
    Insert(T,i)

#Lab funtion calls    
print('B Tree height is ', end='')
print(Height(T))
Sorted_List = []#empty list for extracting elements of B-tree in ascending order
print(Extract(T, Sorted_List))

depth = 2#general depth for appropiate functions
MinAtDepth(T, depth)
MaxAtDepth(T, depth)

print('Number of Nodes is ', end='')
print(NodesAtDepth(T, depth))
PrintAtDepth(T, depth)
print()

print('Number of full Nodes is ', end='')
print(FullNodes(T))
print('Number of full Leaves is ', end='')
print(FullLeaves(T))

print('Key is at Depth ', end='')
print(KeyAtDepth(T, 30, Height(T)))
