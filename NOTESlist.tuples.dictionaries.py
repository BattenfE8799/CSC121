# module 4 -Notes  
#dictionaries sets



def listsNotes():
    # are mutable-changeable
    # multiple values
    # are zerod index. index start at 0
    # slice
    #can have duplicates
    #to remove all duplicates from list, turn it into a set
    students = ["Marceia", "Chantelle"]
        #marceia has index position 0
    
    
    
    
def tuplesNotes():
    # are not mutable
    # you cannot add to or change tupples
    #can have duplicates
    studentsTuple = ("Marceia", "Chantelle")
        #marceia has index position 0, chantelle 1
    
    
def dictionariesNotes():
    # are mutable
    # words point to definitions
    # words cannot be duplicated in dictionary
    # unique pointer is key, value is like definition
    # key:value   word:definition
    # (key:value) = element    
    
    # methods
    #clear()      removes all the elements from dictionary
    #copy()       returns a copy of the dictionary
    #fromkeys()   returns a dict with specified keys and value
    #get()        returns the value of speficied key
    #items()      returns list containing tuple for each key value pair
    #keys()       returns list containing the dict's keys
    #pop()        removes the element with specified key
    #popitem()    removes the last inserted key-value pair
    #setdefault() returns the value of speficied key. if the key doesn't exist: 
                    #insert the key , with the specified value
    #update()     updates the dict with specified key-value pairs
    #values()     returns a list of all the values in the dict
    
    # ADD TO DICTIONARY (element)
    nameOfDict.update({"Jerry":5})
    nameOfDict["Carson"] = 88    
    
    # CREATES DICTIONARY w/elements
    nameOfDict = {"Tom" : 85, "Bob" : 88} 
    
    # CREATES DICTIONARY empty
    grades1 = {}
    
    grades2 = dict()

    # DELETE DICTIONARY (ENTIRE)
    del nameOfDict
    
    # DELETE DICTIONARY (specific key-value pair)
    nameOfDict.pop("Jerry")
    del nameOfDict["Tom"]
    
    # DISPLAYS DICTIONARY entire
    nameOfDict
    
    # DISPLAYING DICTIOANRY KEYS (think slicing)
    nameOfDict ["Tom"]     #put the index/unique pointer/key in brakets to find value
                    # same as using pet[1] to find the second element in a list
    nameOfDict.get(["Tom"])
    nameOfDict.keys(["Tom"])
    
    # DISPLAY DICTIONARY MORE THAN ONE KEY
    for item in nameOfDict:
        print(item)       
    nameOfDict.keys()
        
    # DISPLAY DICTIONARY VALUES ONLY
    for item in nameOfDict.values():
        print(item)
    
    nameOfDict.values()
    
    # DISPLAY DICTIONARY KEYS AND VALUES
    for k,v in nameOfDict.items():
        print(k,v)
    
    nameOfDict.items()
    
    # DISPLAY DICTIONARY KEYS AND VALUES IN TABULAR FORMAT
    print(f'{"Name":<10}{"Age}')
    print("------------------")
    for k, v in nameOfDict.items():
        print(f'{k:,10}{v}')
       
    
    # SEARCH FOR SPECIFIC KEYS/VALUES (think slicing)
        #SEE DISPLAY DICTIONARY
        
    # UPDATE DICTIONARY
    nameOfDict.update({"Jerry":5})
    nameOfDict["Carson"] = 88  #updates the value for Carson
    

def setsNotes():
    #not a zero index
    #no custome index
    #used for comparisons
    #used to see if something is a member in the set
    #example: to see if someone is in both of the classes
    #example cont: so you compare both sets to see if they are in it. 
    # does not allow duplicates
    # if you convert list to set you remove all duplicates
    # can not use slicing in sets, as there is no index
    
    
    #METHODS
    #add()          Adds an element to the set
    #clear()        Removes all the elements from a set
    #
    
    
    
    # CREATE SET empty
    # CONVERT LIST INTO SET
    listName = [90, 88, 88]
    
    setName = set(listName)
    #DO NOT USE setName = {} TO CREATE SET. IT CREATES DICTIONARY
    
    
    