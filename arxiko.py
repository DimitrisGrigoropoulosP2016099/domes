import numpy as np



def __main__():
    print("choose algorithm or intialiaze array")
    print("1.random array \n2.Bubble-sort\n3.Quick-sort\n4.Merge-sort\n5.Selection-sort\n6.Insertion-sort\nshell-sort\n7.Diagram")
    UserChoice = input("enter : \n")
    if UserChoice == "1":
         RandomVector()
    if UserChoice == "2":
         Bubblesort()
    if UserChoice == "3":
         Quick()
    if UserChoice == "4":
         Merge()
    if UserChoice == "5":
         Selection()
    if UserChoice == "6":
         Insertion()
    if UserChoice == "7":
         Shell()
    

def RandomVector():
    radArray = np.random.randint(0, 1000000, 10)
    print(radArray)
    return radArray

def Bubblesort(radArray):
    print(radArray)
    print("\nOriginal array")
    n = len(radArray)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if radArray[j] > radArray[j+1]:
                radArray[j], radArray[j+1] = radArray[j+1], radArray[j]
    print("\n")
    print(radArray)


def Quick():
    print("12")
def Merge():
    print("sd")
def Selection():
    print("asssss")
def Insertion():
    print("aaaaa")
def Shell():
    print("4324")
