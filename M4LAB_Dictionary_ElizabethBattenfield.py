# dictionaary of countries
# 3/29/2021
# CSC121 M4LAB --Dictionary Manipulations
# Elizabeth Battenfield

import sys
#global variable
tld={'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}

# part 1 of the assignment
def partOne():

    """
    part 1 of the assignment,creating and manipulating dictionary
    """
    print ("PART ONE OF ASSIGNMENT:")
    print()
    # creates dictionary containting countries with abbr
    tlds = {'Canada': 'ca', 'United States': 'us', 'Mexico': 'mx'}
    
    # a.check whether it contains key 'Canada' and display
    print("Does tlds contain Canada?")
    print('Canada' in tlds)
    print()
    
    # b.check whether it contains key 'France' and display
    print("Does tlds contain France?")
    print('France' in tlds)
    print()
    
    # c.iterate through the key-value pairs and displays them in table
    print("{:<18} {:10}".format('Country','TLD'))
    print("-----------------------")
          
    for key, value in tlds.items():
        print("{:<18} {:<10}".format(key,value))
        
    # d.add key-value pair 'Sweden' and 'sw'
    print()
    tlds.update({'Sweden':'sw'})
    for index, (key,value) in enumerate(tlds.items()):
        if index ==  3:
            print(key, value)
            print()
    
    # e.update the value for key 'Sweden' to 'se'
    tlds['Sweden']='se'
    for index, (key,value) in enumerate(tlds.items()):
        if index ==  3:
            print(key, value)
            print()
    
    # f.use dictionary comprehension to reverse keys and values
    tlds2 = dict(map(reversed, tlds.items()))
    print(tlds2)
    
    # g.using f result use a comprehension to convert the country names to all uppercase letters
    tlds3 = {k.lower():v.upper() for k,v in tlds2.items()}
    print(tlds3)



# convert to menu driven program. 
# main program
def main(tld):
    """
    main menu for program that manipulates dictionary
    """    
    # declare variable
    userChoice = 0

    #display menu for user
    while (userChoice != 6):
        print()
        print("MENU")
        print("------------------")
        print()
        print("{:>5} {:>10}".format("1)", "Create dictionary"))
        print("{:>5} {:>10}".format("2)", "Search for TLD"))
        print("{:>5} {:>10}".format("3)", "Add to dictionary"))
        print("{:>5} {:>10}".format("4)", "Update dictionary"))
        print("{:>5} {:>10}".format("5)", "Display dictionary content"))
        print("{:>5} {:<10}".format("6)", "Exit"))    
    
        # get choice from user
        userChoice = input()
        
        # calls function depending on choice
        
        if userChoice == '1':
            createDict(tld)
        
        elif userChoice == '2':
            searchTLD(tld)
            
        elif userChoice == '3':
            addToDict(tld)
        
        elif userChoice == '4':
            updateDict(tld)
            
        elif userChoice == '5':
            displayDict(tld)
        
        elif userChoice == '6':
            exitDict()
            
        else:
            print ("Invalid choice. Try again.")
            




def createDict(tld):
    """
    User is prompted to enter dictionary values
    """
    # get user to enter values and keys for dictionary
    howMany = int(input("How many enteries are in your dictionary?: "))
    for count in range(howMany):
        value = input("Enter a value for the dictionary: ")
        key = input("Enter the key for that value: ")
        tld.update({value:key})
    input("Press enter to continue.") #pauses program until user presses enter
    main(tld) #returns to main menu


def searchTLD(tld):
    """
    User is to enter country name and TLD will be displayed
    """
    # as user for country to search for 
    print()
    search = input("Please enter the country you want to search for: ")
    # prints the searched tld
    print(tld[search])


    print()
    
    input("Press enter to continue.") #pauses program until user presses enter
    
    main(tld) #returns to main menu   
    
def addToDict(tld):
    """
    User is prompted for country name and TLD and will add to dictionary
    """    
    print()
    # asks user for new value and key
    newKey = input("Please enter your the new country: ")
    newValue = input("Please enter the abbriviation for the country:")
    #updates dictionary with value and key
    tld.update({newKey:newValue})   
    
    input("Press enter to continue.") #pauses program until user presses enter

    main(tld) #returns to main menu    
    
def updateDict(tld):
    """
    User is promtped to enter key and new TLD, updates dictionary accordingly
    """ 
    #gets user country and new tld for that key
    country = input("Please enter the key: ")
    newValue = input("Pleae enter the new TLD: ")
    
    # updates dictionary with new value
    tld[country]=newValue   
    
    input("Press enter to continue.") #pauses program until user presses enter

    main(tld) #returns to main menu
    
def displayDict(tld):
    """
    Displays content of dictionary in tabular format
    """
    #displays dictionary in table
    print("{:<18} {:10}".format('Key','TLD'))
    print("-----------------------")
          
    for key, value in tld.items():
        print("{:<18} {:<10}".format(key,value))
        
    input("Press enter to continue.") #pauses program until user presses enter

    main(tld) #returns to main menu

    
def exitDict():
    """
    exits the program
    """
    sys.exit(0)

#shows the first 
partOne()
if __name__=='__main__':
    main(tld)
