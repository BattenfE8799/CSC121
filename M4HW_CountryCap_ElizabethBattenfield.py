# creates a country quiz using a dictionary
# 3/29/2021
# CTI-110 M4HW--Country Capitals
# Elizabeth Battenfield

import random
import sys

# create a dictionary containing 20 countries-capitals
countryDict = {"United States": "Washington DC", "Mexico": "Mexico City", 
               "Bulgaria": "Sofia", "Brazil": "Brasilia", "Norway": "Oslo",
               "New Zealand": "Wellington", "Oman": "Muscat", "China": "Bejing",
               "Canada": "Ottawa", "Chile": "Santiago", "Peru":"Lima",
               "Panama": "Panama City", "Greece": "Athens",
               "Cuba": "Havana", "Czechia": "Prague", "Egypt":"Cario",
               "Dominican Republic": "Santo Domingo", "Samoa":"Apia",
               "Germany": "Berlin", "San Marino": "San Marino"}
def main():
    """
    plays game that takes global dictionary of countries to quiz the user about their capitals
    """

    #calls title screen
    title()
    #calls game
    g,b = game()
    #calls end of game and totals
    donePlaying(g,b)
        
def title():
    """
    Shows title screen, and gives users instructions for game
    """
    # Quiz Title Screen
    print("         WELECOME TO             ")
    print("                                 ")
    print("              ____               ")
    print("            /}  { \              ")
    print("           | \  \  |              ")
    print("            \/___\/               ")
    print("                                 ")
    print("      WORLD GEOGRAPHY QUIZ!      ")
    print()
    print()
    input("Please press enter to continue!")
    
    
    #instructions for user
    print()
    print()
    print("                                 ")
    print("              ____               ")
    print("            /}  { \              ")
    print("           | \  \  |              ")
    print("            \/___\/               ")
    print("                                 ")
    print("Instructions are Easy!")
    print("I will give you a Country and you will guess its Capital.")
    print()
    print("The quiz will continue until you choose press -1")
    print()
    print("Here we go! Good Luck :)")
    print()
    input("Please press enter to continue!")
    return()
    
def game():   
    """
    quiz that pulls random key and asks user for its captial
    """

    # create quiz that pulls random key and asking for its capital(value)    
    
    # declare variables
    answer = '0'
    countG = 0
    countB = 0
    
    #create while loop with sentinel
    while answer != '-1':
        
    #pull random key for quiz
        key = random.choice(list(countryDict))
    
    #ask user random question
        print()
        print()
        print("                                 ")
        print("              ____               ")
        print("            /}  { \              ")
        print("           | \  \  |              ")
        print("            \/___\/               ")
        print("                                 ")
        answer = input("What is the capital of "+ key +"? ")
        
        #verify their answer
        if answer == countryDict[key]:
            countG += 1

            print()
            print()
            print("   Congratz! You got it Right!   ")
            print("              ____               ")
            print("            /}  { \              ")
            print("           | \  \  |              ")
            print("            \/___\/               ")
            print("                        ")
            print("                     Correct:",countG)
            print("                     Incorrect:",countB)
            print()
            
                  
        else:
            countB += 1
            print()
            print()
            print()
            print()
            print("            Wrong :(             ")
            print("              ____               ")
            print("            /}  { \              ")
            print("           | \  \  |              ")
            print("            \/___\/               ")
            print("                                 ")
            print("                     Correct:",countG)
            print("                     Incorrect:",countB)
            print()
      
    # user gets sent to the total and exit screen
    return(countG, countB)

def donePlaying(g,b):
    """
    Displays total correct and incorrect when user is done playing game.
    """
    #declare local variables
    countG = g
    countB = b
        # and display when user chooses to stop playing 
    print()
    print()
    print()
    print()
    print(" Correct: ",countG,"  Incorrect: ",countB)
    print("              ____               ")
    print("            /}  { \              ")
    print("           | \  \  |              ")
    print("            \/___\/               ")
    print("                                 ")
    print("    Thank you for playing!")
    print()
    input("Please press enter to quit!")
    sys.exit(0)

    
if __name__=='__main__':
    main()    

    
