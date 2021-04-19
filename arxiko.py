import numpy as np
import time
import copy as copy
from array import array
import sys
import os
import time 


n = 100

radArray = []
MergeStartTime = 0
TotalBubble = 0

def main():
    UserCalled = True

    print("____________________________\n")

    print("choose algorithm or initialize array\n")

    print("1.random array \n2.Bubble-sort\n3.Quick-sort\n4.Merge-sort\n5.Selection-sort\n6.Insertion-sort\n7.shell-sort\n8.Test-run(2.paradoteo)\n9.exit")

    UserChoice = input("enter : ")

    print("\n")

    if UserChoice == "1":
        RandomVector(n , UserCalled)
        main()

    if UserChoice == "2":
        Bubblesort(radArray, UserCalled)

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
        firstrun =  True
        mergeSort(cpArray, UserCalled , firstrun)
        main()

    if UserChoice == "5":
        cpArray = copy.deepcopy(radArray)
        Selection(cpArray, UserCalled)

    if UserChoice == "6":
        cpArray = copy.deepcopy(radArray)
        Insertion(cpArray, UserCalled)

    if UserChoice == "7":
        cpArray = copy.deepcopy(radArray)
        Shell(cpArray , UserCalled)
    if UserChoice == "8":
        testrun()

    if UserChoice == "9":
        print("exiting program")
        sys.exit()


def RandomVector(megethos ,UserCalled):
    global radArray
    radArray = np.random.randint(1000001, size=megethos)
    print(radArray)
    n = megethos + 100
    if UserCalled == True:
     return radArray
    



def Bubblesort(radArray , UserCalled ):
    copyOfArray = copy.deepcopy(radArray)
    #print("\nOriginal array\n")
    #print(copyOfArray)
    sizeof = len(copyOfArray)
    bubbleStartTime = time.perf_counter()
    for i in range(n-1):
        for j in range(0, sizeof-i-1):
            if copyOfArray[j] > copyOfArray[j+1]:
                copyOfArray[j], copyOfArray[j +
                                            1] = copyOfArray[j+1], copyOfArray[j]
    bubbleEndTime = time.perf_counter()
    print( bubbleEndTime - bubbleStartTime)
    #print("\nnew array\n")
    #print(copyOfArray)
    if UserCalled == True:
     main()
QuickStartTime = 0   
QuickEndTIme = 0
QuickTotalTime = 0
def Quick(array , firstrun):
    global QuickStartTime , QuickEndTIme , QuickTotalTime
    if firstrun == True:
        QuickStartTime = time.perf_counter()
        firstrun = False
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
       
        return Quick(less , False)+equal+Quick(greater , False)  
    
    else:  
        QuickEndTime = time.perf_counter()
        QuickTotalTime=QuickEndTime - QuickStartTime
        return array
MergeEndTime = 0
MergeTotalTime = 0
def mergeSort(radArray , UserCalled , firstrun):
    global MergeStartTime , MergeEndTime , MergeTotalTime
    if firstrun == True:
     #print("\nOriginal array\n")
     #print(radArray)
     firstrun = False 
     MergeStartTime = time.perf_counter()
    if len(radArray) > 1:
        mid = len(radArray) // 2
        left = radArray[:mid]
        right = radArray[mid:]

        mergeSort(left , UserCalled, firstrun)
        mergeSort(right , UserCalled, firstrun)

        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              radArray[k] = left[i]
              
              i += 1
            else:
                radArray[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            radArray[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            radArray[k]=right[j]
            j += 1
            k += 1
    MergeEndTime = time.perf_counter()
    MergeTotalTime = MergeEndTime - MergeStartTime
    if UserCalled == True:
      main()
    


def Selection(cpArray , UserCalled):
    #print(cpArray)
    #print("Original array\n")
    SelectionStartTime = time.perf_counter()
    for i in range(len(cpArray)):

        min_idx = i
        for j in range(i+1, len(cpArray)):
            if cpArray[min_idx] > cpArray[j]:
                min_idx = j

        cpArray[i], cpArray[min_idx] = cpArray[min_idx], cpArray[i]
    SelectionEndTime= time.perf_counter()
    print(SelectionEndTime - SelectionStartTime)
    #print(cpArray)
    #print("new array\n\n")
    if UserCalled == True:
     main()

def Insertion(cpArray , UserCalled):
    #print(cpArray)
    #print("Original array\n")
    InsertionStartTime = time.perf_counter()
    for i in range(1, len(cpArray)):

        key = cpArray[i]

        j = i-1
        while j >= 0 and key < cpArray[j]:
            cpArray[j+1] = cpArray[j]
            j -= 1
        cpArray[j+1] = key
    InsertionEndTime = time.perf_counter()
    print(InsertionEndTime - InsertionStartTime)
    #print(cpArray)
    #print("new array\n\n")
    if UserCalled == True:
     main()


def Shell(cpArray , UserCalled):
    #print(cpArray)
    #print("\nOriginal array\n")
    ShellStartTime = time.perf_counter()
    inc = len(cpArray) // 2
    while inc:
        for i, el in enumerate(cpArray[inc:], inc):
            while i >= inc and cpArray[i - inc] > el:
                cpArray[i] = cpArray[i - inc]
                i -= inc
            cpArray[i] = el
        inc = 1 if inc == 2 else inc * 5 // 11
    ShellEndTime = time.perf_counter()
    print(ShellEndTime - ShellStartTime)
    #print(cpArray)
    #print("\n new array\n")
    if UserCalled == True:
     main()

def testrun():
    n = 100
    global MergeTotalTime , QuickTotalTime
    UserCalled = False

    for i in range(10):
     arr1 = []

     arr1 = np.random.randint(1000001, size=n)

     n = n + 100

     print("\nThe ", i + 1 ,": \n" , "\n_____________________________________________________________________________________")

     print("\n Bubble Sort \n")

     copyBubble = copy.deepcopy(arr1)

     Bubblesort(copyBubble , UserCalled )

     print("\n Merge Sort \n")

     firstrun = True

     copyMerge = copy.deepcopy(arr1)

     mergeSort(copyMerge , UserCalled , firstrun)
     print(MergeTotalTime)

     #print("\nnew array \n \n" , copyMerge)

     print("\n Selection Sort \n")

     copySelection = copy.deepcopy(arr1)

     Selection(copySelection , UserCalled)

     print("\n Insertion Sort \n")

     copyInsertion = copy.deepcopy(arr1)

     Insertion(copyInsertion , UserCalled)

     print("\n Shell Sort \n")

     copyShell = copy.deepcopy(arr1)

     Shell(copyShell , UserCalled)

     print("\n Quick Sort \n")

     copyQuick = copy.deepcopy(arr1)
     print(QuickTotalTime)

     #print("\noriginal array\n" ,copyQuick)

     Quick(copyQuick , True)

     #print("\n new array\n",copyQuick)

     print("\nThe end of :", i + 1 ," array \n" ,  "\n_____________________________________________________________________________________")

    UserCalled = True

    main()




main()


# ToDo  runtime diagram  , quick time 
