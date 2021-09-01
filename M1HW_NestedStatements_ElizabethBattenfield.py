# Using a loop to find the two largest values of 10 numbers entered
# 2/3/2021
# CSC 121 M1HW2 --Nested Statements
# Elizabeth Battenfield

# initilized variables
num_1 = 0
num_2 = 0
timethru = 1
second = "st"

# processing with a for loop
for num in range(10):
    
# get number
    number = int(input(f'{"Enter your"} {timethru:<0}{second:<0} {"number: "}'))

# check for larger numbers
    if number > num_1:
        num_2 = num_1
        num_1 = number   
    else:
        num_2 =num_2
        
#add to timethru
    timethru += 1
# check for times through
    if timethru == 2:
        second = "nd"
    elif timethru == 3:
        second = "rd"
    else:
        second = "th"

#print largest and second largest numbers
print()
print(f'{"Your largest number is:"} {num_1}')
print()
print(f'{"Your second largest number is:"} {num_2}')


# Pseudocode
# top comment block
# initialize variables
# ask for number
# if new number is larger save as largest and old largest as second largest
# not sure what to do with else, so put as same = same
# bonus to self if can ask each time using 1st 2nd etc.
# state the largest and second largest numbers