# table of squares and cubes using for loops and f-sting
# 2/3/2021
# CSC 121 M1HW1-- Debugging
# Elizabeth Battenfield


#header row
print(f'{"Number":>6} {"Square":>6} {"Cube":>4}')
#for loop for numbers 0-5
for num in range (6):
    
    print(f'{num:>6} {num**2:>6} {num**3:>4}')


#Pseudocode
#comment block top
#header row with f-string right aligned
#for loop for numbers 0-5 with f-string right aligned