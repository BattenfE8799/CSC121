#example via instructor


petNum = int(input("How many pets do you have? "))


pets = {}

for num in range(1, petNum+1): # always add 1 to userinput # to end there
    name = input("Enter name for pet "+str(num)+":") #input only takes one arguement and str(num) converts num into a string
    
    age = input("How old is "+name+":")
    print()
    
    petType = input("What is "+name+": ")

    
    pets.update({name: age})
print(pets)
    
print(f'{"Name":<10}{"Age"}{"Type"}')
print("---------------------------")
for k, v in pets.items():
    # was print(f'{k:<10}{v}')
    print(f'{k:<10}', end="") #seperates this and next print statement by nothing
    for item in v:
        print(f'{item:<10}', end="")
    print()
    

