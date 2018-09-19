# Gerardo I. Armenta
# Lab1-optA
# date last modified Sept. 17, 2018



import os
import random


def get_dirs_and_files(path):
    #provided method by teacher, not used!
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):     # Provided by teacher, checks path to differentiate dog and cat pics
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2
        print('test')

    return random.random() / 2


def process_dir(path):      # Method used uses time complexity of O(n)

    dir_list, file_list = get_dirs_and_files(path)   # provided code by teacher, not used!

    cat_list = []
    dog_list = []
    all_pics = []

    list = cat_dog(path, all_pics)       # This method lists all paths to cat and dog pics into an array

    for i in range(len(list)):      # for loop used to order dog_list and cat_list
        pic = classify_pic(list[i])
        if pic >= 0.5:
            dog_list.append(list[i])
        else:
            cat_list.append(list[i])

    print(*dog_list, sep ='\n')     # Lines 45 thru 47 tests that dog_list and cat_list are filled // may be erased or marked out
    print('\n')
    print(*cat_list, sep ='\n')

    return cat_list, dog_list


def cat_dog(path, list):        # Method used uses time complexity of O(n)

    for file in os.listdir(path):
        # identifies all files and subdirs in Pictures root dir and creates a for loop the size of all files and sub dirs
        dir_path = os.path.join(path, file)     # This is the path for one file or sub dir
        if dir_path.endswith('jpg'):
            # base case, checks if path contains files that are in jpg format and adds them to the array
            list.append(dir_path)
        elif os.path.isdir(dir_path):
            # recursive step, checks if path contais a sub dir and if it does it calls itself with that new path
            cat_dog(dir_path, list)

    return list


def main():

    start_path = './' # current directory

    process_dir(start_path)



main()
