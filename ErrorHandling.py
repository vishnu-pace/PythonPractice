
try:
    num = int(input( 'Enter a number: ' ))
    res = 20/num
    print(res)


except ZeroDivisionError:
    print('[ERROR] Zero Cannot be provided.')
#except ValueError:
#    print('[ERROR] Please provide a integer number.')
except:
    pass
    #print('[ERROR] Please re-enter.')


print('Thank you.')