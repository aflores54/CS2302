#Lab 2 Adolfo Flores, Dr. Olac Fuentes
#CS2302 1:30p.m., Anindita Nath, Maliheh Zargaran
#Last edited 2/24, Sorting Algorithms
import random

def Median(L):
    C = L[len(L)//2]
    return C

def Bubblesort(L):#sort list by checking consecutive elements
    if len(L) == 0:#check if list is empty
        print("List is empty")
        return
    else:
        repeat = True
        while repeat:
            repeat = False#to stop program if list is sorted
            for i in range(len(L)-1):
                if L[i] > L[i+1]:
                    temp = L[i]
                    L[i] = L[i+1]
                    L[i+1] = temp
                    repeat = True
    return L

def Mergesort(L):#sort list by splitting list with recursion and merging them in order
    if len(L) == 0:
        print("List is empty")
        return  
    elif len(L) == 1:
        return
    else:
        mid = len(L)//2
        #recursive call that splits the list
        r1 = L[:mid]
        r2 = L[mid:]
        Mergesort(r1)
        Mergesort(r2)
        if r1[len(r1)-1] > r2[0]:#puts the two lists together
            L = r2 + r1
            return L
        else:
            L = r1 + r2
            return L
        return L

List = [0, 1, 2, 3, 4, 5]
for i in range(len(List)):#changes list with random numbers from 0 to 100
    List[i] = random.randint(0, 101)

print(List)
print()
B = Bubblesort(List)
print(B)
print(Median(B))
print()

for i in range(len(List)):
    List[i] = random.randint(0, 101)
print(List)
print()
M = Mergesort(List)
print(M)
print(Median(M))
