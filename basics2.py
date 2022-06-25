# ------------------------------
# File Name: basics2.py
# Description: Some of the basics of python operations.
#
# Created On: 21-June-2022
# Updated On: 21-June-2022
# ------------------------------

# One line comment
# print('Hello World') # Print example

'''
Multi-line comments
Same here
Thank you
'''

"""
Same
Same
"""
# print('Welcome')
print()

num = 21
#print('Hello', num, 'June', '-', 2022, type(num))

num = 'Hello'
#print(num, type(num))

num1 = 21
num = num1 + 4
num += 1 # num = num + 1
# + -* / %

# Integer Division
res = num // 5 # res = int(num / 5)

# Power Operator
res = 2 ** 8 # 2^8
#print(res, end= '\n')
#print('Testing...')

'''
if res == 255 :
    print('Correct')
    print('Done')
elif res == 256:
    print('Inside Else If')
else:
    print('Else')
'''

'''
if res == 255 :
    print('Correct')
    print('Done')

print('Exit')
'''

str1 = 'Name'
if str1 == 'Name':
    print('True')
else:
    print('False')



# While Loop

count = 0
num = 1
'''
while (count < 5) or (num < 3): # and or not
    print(count)
    count += 1
    num +=1
'''

'''
while (count < 5) : # and or not
    print(count)
    if count == 6:
        print('Found')
        break
    count += 1
else:
    print('Inside ELSE')

print('Done')
'''


# List

numbers = [21, 24, 27, 30]

#print(numbers[1])

'''
idx = 0
while idx < len(numbers):
    print(numbers[idx])
    idx += 1
'''

names = [ 'Sonu', 24, 'Celine', 'Vinayak', 24.12, 'Umer' ]

'''
print( type(names) )
idx = 0
while idx < len(names):
    print(names[idx])
    idx += 1
'''


# For Loop

'''
for name in names :
    print( name )
'''

'''
for idx,name in enumerate(names):
    print( idx, '->', name )
else:
    print('Inside Else')
'''

# Input from User
print()
#inputVar = input( 'Enter Name: ' )
'''
print(' Name: ', inputVar )

empID = int( input( 'Enter Employee ID: ') )
print( type(empID) )
empID += 1
print(' ID: ', empID )
'''

# Workout Question-1
# Create a list with multiple names. Ask a name from user to be searched in this list.
# Search the name in the list and print if found or not. If found, print index too.


# List methods




