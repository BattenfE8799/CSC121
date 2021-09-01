# intake student names and scores into a DataFrame
# 4/29/2021
# CSC121 M5Lab--DataFrame
# Elizabeth Battenfield

import pandas as pd 






def main():

    """
    program to create dataframe containing testnames, students, their grades for those tests
    """
    # declare variables
    tempList = []
    # ask user how many tests the grades are for
    numTest = int(input("How many tests are there?(3 minimum) "))
    for x in range(numTest):
        # ask user to enter test names (used as indices)
        test = input("Enter the test name: ")
        tempList.append(test)
    # create dictionary of students names and their grades
    studentDict = createDict(numTest)
    
    #create dataframe of information
    gradesDF = pd.DataFrame(studentDict)
    
    #use custome indexes as test names given by user
    gradesDF.index = [tempList]
    print(gradesDF)
     

def createDict(numTest):
    """
    User is prompted to enter dictionary values for students and their grades
    """
    # ask user the number of students they would like to enter grades for
    # ask user to enter dictionary info, student Name, list of grades (3 min)
    studentDict = {}
    gradeList = []
    count = int(input("How many students are you entering grades for? "))
    for num in range(count):
        studentKey = input("Enter student name: ")
        gradeList = []
        for num in range(numTest):
            gradeValue = int(input("Enter grade: "))
            gradeList.append(gradeValue)
           
        studentDict.update({studentKey:gradeList})
    print(studentDict)
    #returns to main menu 
    return (studentDict)
    
if __name__=='__main__':
    main()
    