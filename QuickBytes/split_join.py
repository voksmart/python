# Split text using split() function

str1='Good Morning! Welcome to New York'
print(str1.split()) # returns a list

str2='Apples,Oranges,Grapes,Mangoes'
# separates on comma
# default sep = ' ' 
print(str2.split(sep=','))

# maxsplit property
# defines total no. of split to occur
# default maxsplit = -1,as many as possible

print(str1.split(maxsplit=2)) # two splits
# total no. of elements = maxsplit+1

# join() method
# joins iterator elements with str separator
city=['T','e','x','a','s']
fruit = ["mango","grapes","apple"]

strsep1 = ""
strsep2 = "-"
print(strsep1.join(city))
print(strsep2.join(fruit))


