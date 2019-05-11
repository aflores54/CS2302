#CS2302, Adolfo Flores 80457200, Lab 8, Dr. Olac Fuentes
#TA's Anindita Nath, Maliheh Zargaran
#Last Edit 5/10, Check trig identities using Randomization Advanced Programming,
#and finds two subsets of a list S whose sum are equal to each other
#and do not contain any similar elements by using Backtracking Advanced Programming
import random
import numpy as np
from math import *

def equal(f1, f2,tries=1000,tolerance=0.0001):#Method to test trig identities
    if f1 == 'sec(t)\n':#If sec is tested will change to a known trig identity
            f1 = '1/cos(t)\n'#Since sec is not recognized in Python
    if f2 == 'sec(t)\n':
            f2 = '1/cos(t)\n'
    for i in range(tries):#Tests 'tries' number of times
        t = random.uniform(0 - np.pi, np.pi)#Picks a float number between negative pi and pi
        y1 = eval(f1)#evaluates the string if it resembles a function
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:#Checks if the functions equal each other
            return False
    return True

def subset_sum(SS):#Method that returns the sum of a list
    sum = 0
    for i in SS:
        sum += i
    return sum

def equal_subset_sum(S,last,goal):#Method that creates two subsets of a list whose sums are equal to each other
                                #and union of the subsets equal the list
    if  goal==0 and last<0:#If a solution is found, return True
        return True, []
    if goal==0 and last>0:#Prevents the method from returning an incomplete solution
        return False, []
    if goal<0 or last<0:#If the sum of S1 is greater than S2, or if there is no solution, return False
        return False, []
    res, S1 = equal_subset_sum(S,last-1,goal-S[last])#Subtracts from the sum of S2 in order to find a solution
    if res:#if Solution is found, builds S1
        S1.append(S[last])
        return True, S1
    else:#Builds S2
        S2.append(S[last])
        return equal_subset_sum(S,last-1,goal+S[last])

file = open('test_functions.py','r', encoding="utf8")#Reads the text file that contains the trig functions
list = []
for i in file:#Builds a list of strings that contains the trig functions
    list += [i]
file.close()

for x in range(len(list)):#Nested for loop that tests every possible combination
    for y in range(x + 1, len(list)):
        print("Functions compared are:", list[x],"and", list[y], end=' ')
        print(equal(list[x],list[y]))
        print()

S = [2,5,8,9,12,21,33]#Initial list

S2 = [S[len(S)-1]]#Global variable that is built in equal_subset_sum method

a, S1 = equal_subset_sum(S,len(S)-2,subset_sum(S2))#Method call that returns True and a built S1 if a solution is found
                                                #and False if no solution is found
if a:#If solution is found, sorts S2, prints out what the subsets sum equals, and prints the subsets
    for i in range(len(S2)):
        for j in range(len(S2)-1):
            if S2[j]>S2[j+1]:
                temp = S2[j]
                S2[j]=S2[j+1]
                S2[j+1]=temp
    print("Solution found and subset sums is ",subset_sum(S1))
    print("S1 = ", S1)
    print("S2 = ", S2)
else:#If False prints no solution found
    print("Solution not found")