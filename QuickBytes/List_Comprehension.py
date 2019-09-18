# List comphrenshion

numList=[1,2,3,4,5]

# Simple List Comprehension
# print square of numbers is numlist

square=[x**2 for x in numList]

# List Comphrehension with 'if' statement
square=[x**2 for x in numList if x%2==0]

# List Comphrehension with nested lists
skipList=[2,5,7]
square=[x**2 for x in numList if x not in skipList]

# List Comphrehension with nested 'for' 
# & nested 'lists'
skipList=[2,5,7]
square=[x**2 for y in numList for x in skipList]
