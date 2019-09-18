# Keep a count of iterations
# method -1 (Un-optimized)
str1 = "Hello Jack"
i=0
findLetter="J"
for letter in str1:
    if letter == findLetter:
        print(f'{findLetter} occurs at index : {i:d}')
        break
    i+=1
    
# method -2 (Un-optimized)
color = ["red","blue","green","yellow"]
i=0
findColor = "green"
for mycolor in color:
    if mycolor == findColor :
        print(f'{findColor} occurs at index : {i:d}')
        break
    i+=1

# Method 3 : Enumerate
# enumerate start index @ 0
for cindex,mycolor in enumerate(color):
    if mycolor == findColor :
        print(f'{findColor} occurs at index : {cindex:d}')
        break
    
# Forcing enumerate to start index @ 1
for cindex,mycolor in enumerate(color,1):
    if mycolor == findColor :
        print(f'{findColor} occurs at index : {cindex:d}')
        break

