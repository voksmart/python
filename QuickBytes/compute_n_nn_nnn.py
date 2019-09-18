# Objective
# input a number from user say 'n'
# find the sum of n + nn + nnn

# for e.g user input = 5
# find the sum of 5 + 555 + 555

num = input('Enter a number :')
sum=0

for i in range(1,4):
    sum+=int(num*i)
    
print(sum)


# find the sum of n + nn + nnn +....+n(mtimes)
# for e.g user input = 5
# number of times = 4
# find the sum of 5 + 555 + 555 +5555

num = input('Enter a number :')

mtimes = int(input('No of times:'))
sum=0

for i in range(1,mtimes+1):
    sum+=int(num*i)
    
print(sum)

