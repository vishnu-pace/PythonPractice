# Workout Question - 2
# Pattern using while loop
# 5 4 3 2 1 
# 4 3 2 1
# 3 2 1
# 2 1
# 1

'''
Workout Question - 3
Pattern using while loop
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* * 
*
'''

print()
# Range Function
#print( range(5) ) # 0 1 2 3 4 

'''
for val in range(-10, 20, 5):
    print(val)
'''
'''
for val in range(20, -11, -5):
    print(val)
'''

# Workout Question - 4
# Fibonacci Series with user-specified limit
# 0 1 1 2 3 5 8 13 21...
# Example-1:
# Enter limit: 10
# 0 1 1 2 3 5 8
# Example-2:
# Enter limit: 5
# 0 1 1 2 3 5


# List methods
names = [ 'Sonu', 'Celine', 'Vinayak', 'Umer' ]


#print(names)
'''
#name = input('Enter name to be appended: ')
names.append('Sreeja')
print(names)
names.pop(0)
names.pop()
print(names)
'''

#print(names[-1]) # -1 is the last index of list
names[0] = 'Sreeja'
#print(names)


# Tuple
coord= ( 2, 'Hi', 3.14)
#print(coord)

#coord[1] = 'Umer'
#print(coord)

res = coord[0] + 2
#print(res)


# Set
numSet = { 'Hello', 24, 1.23, 'op', 12, 24, 'op', 24 }

#print(numSet)

# List without Repetation
numList = [ 'Hello', 24, 1.23, 'op', 12, 24, 'op', 24 ]
#print(numList)
numList = list( set( numList ) )
#print(numList)



# Dictionary
phonebook = { 
    'Key': 'Value', 
    'Name':'Vishnu', 
    'EmpId': 22, 
    'Rating': 22.11, 
    2: 'Val'  }

for key in phonebook:
    #print(key)
    #print(phonebook[key])
    pass

#print(phonebook['Name'])
# print(phonebook[0]) # KeyError because no key as 0
'''
for key,val in phonebook.items():
    #print(key, '->', val)
    if key == 'Name':
        print(val)
'''


# List of tuples

coordList = [ (0,1), (1,2), (4,5) ]
#print(coordList[1])

# List of Dictionaries

phonebook = [ 
    { 'Name': 'Sonu', 'EmpId' : 22 },
    { 'Name': 'Sreeja', 'EmpId': 21 },
    { 'Name': 'Umer', 'EmpId': 99 }
 ]
'''
for each in phonebook:
    if each['EmpId'] == 99:
        print( each['Name']  )
'''

# Workout Question - 5
'''
List of Dictionaries
Keys -> Name, EmpId, Username, Password
Enter Username:
Enter Password:
'''



# Functions

'''
def sampleFunc( str1 ):
    print(str1, type(str1))


sampleFunc('Hello') # Function call
sampleFunc(24)
sampleFunc( ['Ok', 'HI', 24] )
'''

def simpleFunc( str1, var2= 10 ):
    print(str1)
    var2 += 5
    print(var2)
    temp = [var2, str1]
    return var2, str1, temp

'''
simpleFunc( var2= 20, str1= 'Hello')
#simpleFunc(str1= 'Welcome')
res = simpleFunc(str1= 'OK')
print(res)
res1, res2, res3 = simpleFunc(str1= 'OK')
print(res1, '<-->', res2, '<-->', res3)
'''

# MODULES

'''
import modules1
int1 = int(input( 'Enter 1st number: ' ))
int2 = int(input( 'Enter 2nd number: ' ))
resAdd = modules1.add(int1, int2)
resSub = modules1.sub(int1, int2)
print(resAdd, 'and', resSub)
'''

'''
import modules1 as m1
int1 = int(input( 'Enter 1st number: ' ))
int2 = int(input( 'Enter 2nd number: ' ))
resAdd = m1.add(int1, int2)
resSub = m1.sub(int1, int2)
print(resAdd, 'and', resSub)
'''

from modules1 import add,sub
int1 = int(input( 'Enter 1st number: ' ))
int2 = int(input( 'Enter 2nd number: ' ))
resAdd = add(int1, int2)
resSub = sub(int1, int2)
print(resAdd, 'and', resSub)







