# find() method

txt = 'Hello John'
# returns lowest index of sub string 
# if found else returns -1 

print(txt.find('John'))

# replace method 
# replace 'John' with 'Jane'
print(txt.replace('John','Jane'))

# Practical Demo
sample="Its a cloudy day"
retIndex=sample.find("cloudy")

if retIndex!=0:
    sample=sample.replace("cloudy","sunny")
    print(sample)
else:
    print("No match found!")
    
