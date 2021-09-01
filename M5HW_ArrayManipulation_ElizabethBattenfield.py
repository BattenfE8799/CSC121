# creates and manipulates NumPy Arrays
# 4/29/2021
# CSC121 M5HW--Array Manipluations
# Elizabeth Battenfield


import sys
import numpy as np

def main(array1):
    """
    main menu for program creates and manipulates array
    """    
    # declare variable
    userChoice = 0

    #display menu for user
    while (userChoice != 6):
        print()
        print("MENU")
        print("------------------")
        print()
        print("{:>5} {:>10}".format("1)", "Create a 3-by-3 Array"))
        print("{:>5} {:>10}".format("2)", "Display square Values for elements in array"))
        print("{:>5} {:>10}".format("3)", "Add 4 to every element and display result"))
        print("{:>5} {:>10}".format("4)", "Multiply elements by 6 and display result"))
        print("{:>5} {:<10}".format("5)", "Exit"))    
    
        # get choice from user
        userChoice = input()
        
        # calls function depending on choice
        
        if userChoice == '1':
            array1 = createArray()
        
        elif userChoice == '2':
            squareValues(array1)
            
        elif userChoice == '3':
            addFour(array1)
        
        elif userChoice == '4':
            timesSix(array1)
               
        elif userChoice == '5':
            exitDict()
            
        else:
            print ("Invalid choice. Try again.")



def createArray():
    """
    User is prompted to enter dictionary values
    """
    # get user to enter values for array
    value1 = int(input("Enter an int value for the first part of 3-by-3 Array: "))
    value2 = int(input("Enter an int value for the first part of 3-by-3 Array: "))
    value3 = int(input("Enter an int value for the first part of 3-by-3 Array: "))
    value4 = int(input("Enter an int value for the second part of 3-by-3 Array: "))
    value5 = int(input("Enter an int value for the second part of 3-by-3 Array: "))
    value6 = int(input("Enter an int value for the second part of 3-by-3 Array: "))
    value7 = int(input("Enter an int value for the third part of 3-by-3 Array: "))
    value8 = int(input("Enter an int value for the third part of 3-by-3 Array: "))
    value9 = int(input("Enter an int value for the third part of 3-by-3 Array: "))
    print()
    
    #create array
    array1 = np.array([[value1,value2,value3],[value4,value5,value6],[value7,value8,value9]])
    array1 = array1.astype(int)
    # display array without square brackets
    print()
    for x in array1:
        for y in x:
            print(y, end=" ")
        print()
    print()
    
    
    input("Press enter to continue.") #pauses program until user presses enter
    main(array1) #returns to main menu
    
def squareValues(array1):
    """
    calculates the square value for each element in an array and displays it
    """
    #check if array is empty
    if len(array1) == 0:
        print("There array is empty. Choose option 1 next time.")
        main(array1)
        
    #make deep copy of array
    array2 = array1.copy()
    #square deep copy
    array2S = np.square(array2)
    
    # display array without square brackets
    print()
    for x in array2S:
        for y in x:
            print(y, end=" ")
        print()
    print()
    
    
    input("Press enter to continue.") #pauses program until user presses enter
    main(array1) #returns to main menu
    
def addFour(array1):
    """
    Add 4 to every element of array and display result
    """    
    #check if array is empty
    if len(array1) == 0:
        print("There array is empty. Choose option 1 next time.")
        main(array1)
        
    #make deep copy of array
    a = array1.copy()
    
    #add four for each element of array
    a += 4
    
    # display array without square brackets
    print()
    for x in a:
        for y in x:
            print(y, end=" ")
        print()
    print()
    
    
    input("Press enter to continue.") #pauses program until user presses enter
    main(array1) #returns to main menu    


def timesSix(array1):
    """
    Multiply elements in array by 6 and display result
    """
    #check if array is empty
    if len(array1) == 0:
        print("There array is empty. Choose option 1 next time.")
        main(array1)
        
    #make deep copy of array
    a = array1.copy()
    
    #multiply all elements in array by 6
    a *= 6
    
    # display array without square brackets
    print()
    for x in a:
        for y in x:
            print(y, end=" ")
        print()
    print()
    
    
    input("Press enter to continue.") #pauses program until user presses enter
    main(array1) #returns to main menu    


    
def exitDict():
    """
    exits the program
    """
    sys.exit(0)


if __name__=='__main__':
    array1 = ([])
    main(array1)
    