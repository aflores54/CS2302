#CS2302, Adolfo Flores 80457200, Lab 7, Dr. Olac Fuentes
#TA's Anindita Nath, Maliheh Zargaran
#Last Edit 5/6, Build Maze Path using a Adjacency List, Breadth First Search, and Depth First Search

import matplotlib.pyplot as plt
import numpy as np
import random


def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):#Draws the maze
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
        
def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def NumSets(S):#returning the number of -1's
    count =0
    for i in range(len(S)):
        if S[i]<0:
            count += 1
    return count

def union(S,c1,c2):
    # Joins cell1 and cell2, if they are in different sets
    ri = find(S,c1) 
    rj = find(S,c2)
    if ri != rj:
        S[rj] = ri

#Original code for assignment from here on
def Create_maze(walls, maze_rows, maze_cols, M):#Creates maze by removing walls through 
                                            #Disjoint Set Forest
    S = np.zeros(maze_rows*maze_cols,dtype=np.int)-1#Builds forest starting with cells in sepeparate sets
    N = NumSets(S) - M#Variable for while loop condition
    
    while NumSets(S) > 1 and NumSets(S) > N:#Continues until there is a single set or reaches M
        d = random.randint(0,len(walls)-1)#Picks a random wall from walls list
        
        cell = walls[d]#cell, c1, c2 are variables to be used for determing if the
        c1 = cell[0]    #two cells are in the same set before removing wall[d]
        c2 = cell[1]
        if find(S,c1) != find(S,c2) and find(S,c1) != -1 and find(S,c2) != -1:#If the two cells are in different sets, 
            union(S, c1, c2) #joins them to each other
            union(S, c2, c1)
            walls.pop(d)#Then remove the wall from the walls list
    if N > 1:#This prints a text statement if path 0 to the upper right corner may or may not exist
        print("A single path to destination may not exist")
    if N == 1:
        print("A single path to destination exists")
    if N < 1:#This is for when NumSets reached 1 instead of N, so we remove more walls to match M
        N = N*(-1)
        for i in range(M):
            d = random.randint(0,len(walls)-1)
            walls.pop(d)
        print("More than one path to destination may exist")
    return walls#returns new maze

def Build_AL(walls, mr, mc):#Builds the Adjacency List
    AL = []#Sets a list of maze_rows*maze_cols number of empty lists which the edges will be added to
    for i in range(mr*mc):
        AL += [[]]
    
    for u in range((mr*mc)-1):#This loop checks the walls list, starting from the bottom row, if a wall does not exist
                            #Then an edge between the two cells exist and is concatenated the Adjacency List to both vertices
                            #The only cell not to be checked is the upper right corner which will not have a "wall" in the walls list
        if u%mc < mc - 1 and u//mc < mr - 1:#This checks all the cells in a row minus the last cell and the top row of the maze
            if [u,u+1] not in walls and [u,u+mc] not in walls:
                AL[u] += [u+1] + [u+mc]
                AL[u+1] += [u]
                AL[u+mc] += [u]
            if [u,u+1] not in walls and [u,u+mc] in walls:
                AL[u] += [u+1]
                AL[u+1] += [u]
            if [u,u+1] in walls and [u,u+mc] not in walls:
                AL[u] += [u+mc]
                AL[u+mc] += [u]
                
        elif u%mc == mc - 1 and u//mc < mr - 1:#This checks the last cell in a row
            if [u,u+mc] not in walls:
                AL[u] += [u+mc]
                AL[u+mc] += [u]
                
        else:#This checks the top row
            if [u,u+1] not in walls:
                AL[u] += [u+1]
                AL[u+1] += [u]
    return AL

def breadth_first_search(G, s, f):#This builds a path from 0 to all reachable cells using Breadth First Search
    visited1 = []#List to state True or False statements whether we have already been to cell before
    for i in range(len(G)):
        visited1 += [False]
        
    prev1 = np.zeros(len(G),dtype=np.int) - 1#List to build a path from 0 to goal
    Q = [s]#Our Queue list
    visited1[s] = True#changes location to True, we have visited
    while Q != []:#Loop to build prev1 path until all cells within reach from start have been visited
            u = Q[0]
            Q = Q[1:]#Our dequeue statement
            for t in G[u]:#Checks all reachable cells from current cell
                if visited1[t] == False:#If condition is True, we have not visited the adjacent cell
                    visited1[t] = True
                    prev1[t] = u#A path from current cell to adjacent cell now exists
                    Q += [t]#Our add to queue statement
                    if t == f:#If we reach goal, end loop
                        return prev1
    
    return prev1

def depth_first_search_stack(G, s, f):#This builds a path from 0 to all reachable cells by using a Stack
    visited2 = []
    for i in range(len(G)):
        visited2 += [False]
        
    prev2 = np.zeros(len(G),dtype=np.int) - 1
    S = [s]
    visited2[s] = True
    while S != []:
            u = S[-1]
            S = S[:-1]#Our pop statement
            for t in G[u]:
                if visited2[t] != True:
                    visited2[t] = True
                    prev2[t] = u
                    S += [t]
                    if t == f:
                        return prev2
    return prev2

def depth_first_search_rec(G, s, f):#This builds a path from 0 to all reachable cells with recursion
    visited[s] = True#global variable
    for t in G[s]:
        if visited[t] != True:
            prev[t] = s#global variable
            if t == f:
                return prev
            depth_first_search_rec(G, t, f)
    return prev
    
plt.close("all") 
maze_rows = 10#variables for setting maze dimensions
maze_cols = 15
M = int(input("Enter number of walls to be removed: "))#User input to determine how many walls to be removed

walls = wall_list(maze_rows,maze_cols)#Builds maze with all walls set
draw_maze(walls,maze_rows,maze_cols,cell_nums=True)#Draws maze with all walls and numbered cells

walls = Create_maze(walls, maze_rows, maze_cols, M)#Calls the Create_maze function

draw_maze(walls,maze_rows,maze_cols,cell_nums=True)#Draws completed maze without numbers

AL = Build_AL(walls, maze_rows, maze_cols)#Adjacency list function call
print("Adjacency List")
print(AL)
print()

BFS_result = breadth_first_search(AL, 0, (maze_rows*maze_cols) - 1)#Breadth First Search function call

DFS_result = depth_first_search_stack(AL, 0, (maze_rows*maze_cols) - 1)#Depth First Search with Stack function call

visited = []#Define global variable
for i in range(len(AL)):#Build global variable
    visited += [False]    
prev = np.zeros(len(AL),dtype=np.int) - 1#Define and build global variable

DFSR_result = depth_first_search_rec(AL, 0, (maze_rows*maze_cols) - 1)#Depth First Search with Recursion function call

if M >= maze_rows*maze_cols -1:#If there is at least a single path from start to goal a single path will be compressed
                                #This implies all cells that point to 0 is a single path from 0 to goal
    union_c(BFS_result,0,maze_rows*maze_cols -1)
    union_c(DFS_result,0,maze_rows*maze_cols -1)
    union_c(DFSR_result,0,maze_rows*maze_cols -1)
#These print statements print results
print("Breadth First Search")
print(BFS_result)
print()
print("Depth First Search Stack")
print(DFS_result)
print()
print("Depth First Search Recursion")
print(DFSR_result)