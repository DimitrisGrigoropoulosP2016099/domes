import numpy as np
import time
import copy as copy
from array import array
import sys
import os


n = 100

radArray = []


def main():

    print("____________________________\n")

    print(radArray)

    print("choose algorithm or initialize array\n")

    print("1.random array \n2.Bubble-sort\n3.Quick-sort\n4.Merge-sort\n5.Selection-sort\n6.Insertion-sort\n7.shell-sort\n8.Diagram\n9.exit")

    UserChoice = input("enter : ")

    print("\n")

    if UserChoice == "1":
        RandomVector(n)

    if UserChoice == "2":
        Bubblesort(radArray)

    if UserChoice == "3":
        megeArray = len(radArray)
        cpArray = copy.deepcopy(radArray)
        Quick(cpArray, 0, megeArray-1)
        print("\n")
        print(cpArray)
        print("\n")
        main()

    if UserChoice == "4":
        cpArray = copy.deepcopy(radArray)
        print(cpArray)
        Merge_sort(cpArray, 0, len(cpArray) - 1)
        print(cpArray)
        main()

    if UserChoice == "5":
        cpArray = copy.deepcopy(radArray)
        Selection(cpArray)

    if UserChoice == "6":
        cpArray = copy.deepcopy(radArray)
        Insertion(cpArray)

    if UserChoice == "7":
        cpArray = copy.deepcopy(radArray)
        Shell(cpArray)

    if UserChoice == "9":
        print("exiting program")
        sys.exit()


def RandomVector(megethos):
    global n, radArray
    radArray = np.random.randint(1000001, size=megethos)
    time.sleep(1)
    print(radArray)
    n = megethos + 100
    time.sleep(1)
    main()


def Bubblesort(radArray):
    copyOfArray = copy.deepcopy(radArray)
    print(copyOfArray)
    print("\nOriginal array")
    time.sleep(1)
    sizeof = len(copyOfArray)
    for i in range(n-1):
        for j in range(0, sizeof-i-1):
            if copyOfArray[j] > copyOfArray[j+1]:
                copyOfArray[j], copyOfArray[j +
                                            1] = copyOfArray[j+1], copyOfArray[j]
    time.sleep(1)
    print("\n")
    print("new array\n")
    print(copyOfArray)
    time.sleep(1)
    main()


def Quickpartition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:

            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)


def Quick(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = Quickpartition(arr, low, high)
        Quick(arr, low, pi-1)
        Quick(arr, pi+1, high)


def Merge_sort(cpArray, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    Merge_sort(array, left_index, middle)
    Merge_sort(array, middle + 1, right_index)
    Merge(array, left_index, right_index, middle)


def Merge(array, left_index, right_index, middle):

    aristero_copy = array[left_index:middle + 1]
    deksi_copy = array[middle+1:right_index+1]

    aristero_copy_index = 0
    deksi_copy_index = 0
    sorted_index = left_index

    while aristero_copy_index < len(aristero_copy) and deksi_copy_index < len(deksi_copy):

        if aristero_copy[aristero_copy_index] <= deksi_copy[deksi_copy_index]:
            array[sorted_index] = aristero_copy[aristero_copy_index]
            aristero_copy_index = aristero_copy_index + 1

        else:
            array[sorted_index] = deksi_copy[deksi_copy_index]
            deksi_copy_index = deksi_copy_index + 1

        sorted_index = sorted_index + 1

    while aristero_copy_index < len(aristero_copy):
        array[sorted_index] = aristero_copy[aristero_copy_index]
        aristero_copy_index = aristero_copy_index + 1
        sorted_index = sorted_index + 1

    while deksi_copy_index < len(deksi_copy):
        array[sorted_index] = deksi_copy[deksi_copy_index]
        deksi_copy_index = deksi_copy_index + 1
        sorted_index = sorted_index + 1


def Selection(cpArray):
    print(cpArray)
    print("Original array\n")
    for i in range(len(cpArray)):

        min_idx = i
        for j in range(i+1, len(cpArray)):
            if cpArray[min_idx] > cpArray[j]:
                min_idx = j

        cpArray[i], cpArray[min_idx] = cpArray[min_idx], cpArray[i]
    print(cpArray)
    print("new array\n\n")
    main()


def Insertion(cpArray):
    print(cpArray)
    print("Original array\n")
    for i in range(1, len(cpArray)):

        key = cpArray[i]

        j = i-1
        while j >= 0 and key < cpArray[j]:
            cpArray[j+1] = cpArray[j]
            j -= 1
        cpArray[j+1] = key
    print(cpArray)
    print("new array\n\n")
    main()


def Shell(cpArray):
    print(cpArray)
    print("\nOriginal array\n")
    inc = len(cpArray) // 2
    while inc:
        for i, el in enumerate(cpArray[inc:], inc):
            while i >= inc and cpArray[i - inc] > el:
                cpArray[i] = cpArray[i - inc]
                i -= inc
            cpArray[i] = el
        inc = 1 if inc == 2 else inc * 5 // 11
    print(cpArray)
    print("\n new array\n")
    main()


main()


# ToDo fix merge 
