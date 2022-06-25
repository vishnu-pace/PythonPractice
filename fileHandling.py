
# File Handling
print('Beginning...')

# CSV Files : Comma separated Values

'''
# logFile = open( './logs/sample1.txt', 'w' ) # 'w', 'r', 'a'
logFile = open( './logs/sample1.txt', 'a' )
logFile.write( 'Hello. \n Thank you' )
#logFile.write( 'PACELAB 2022' )
logFile.close()
'''

'''
logFile = open( './logs/sample1.txt', 'r' )

for lines in logFile.readlines():
    print(lines)

logFile.close()
'''

'''
with open( './logs/sample1.txt', 'r' ) as logFile:
    for lines in logFile.readlines():
        print(lines)
'''

with open( './logs/data.csv', 'r' ) as logFile:
    for line in logFile.readlines():
        eachData = line.split(',')
        eachData[-1] = eachData[-1].split('\n')[0] # Cleaning last element data
        for data in eachData:
            print(data, end= '\t|\t')
        print()


print('Program Over')



