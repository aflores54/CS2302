#CS2302, Adolfo Flores 80457200, Lab 6, Dr. Olac Fuentes
#TA's Anindita Nath, Maliheh Zargaran
#Last Edit 4/15, Build Maze using a Disjoint Set Forest

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
def Create_maze(walls, maze_rows, maze_cols):#Creates maze by removing walls through 
                                            #Disjoint Set Forest
    S = np.zeros(maze_rows*maze_cols,dtype=np.int)-1#Builds forest starting with cells in sepeparate sets
   
    while NumSets(S) > 1:#Continues until there is a single path to every cell (i.e. every cell in the same set)
        d = random.randint(0,len(walls)-1)#Picks a random wall from walls list
        
        cell = walls[d]#cell, c1, c2 are variables to be used for determing if the
        c1 = cell[0]    #two cells are in the same set before removing wall[d]
        c2 = cell[1]
        if find(S,c1) != find(S,c2) and find(S,c1) != -1 and find(S,c2) != -1:#If the two cells are in different sets, 
            union(S, c1, c2) #joins them to each other
            union(S, c2, c1)
            walls.pop(d)#Then remove the wall from the walls list
    return walls#returns new maze

plt.close("all") 
maze_rows = 10#variables for setting maze dimensions
maze_cols = 15

walls = wall_list(maze_rows,maze_cols)#Builds maze with all walls set
draw_maze(walls,maze_rows,maze_cols,cell_nums=True)#Draws maze with all walls and numbered cells

walls = Create_maze(walls, maze_rows, maze_cols)#Calls the Create_maze function

draw_maze(walls,maze_rows,maze_cols)#Draws completed maze without numbers
