'''
# Creating Object of class from a module
from classes import adcBoard

adcObj = adcBoard( busCh= 2, Addr= 0x11 )

#adcObj.readAdc()
adcObj.calcTemp()
print('After calling method:', hex(adcObj.adcVal), '|', adcObj.TempVal )
'''

'''
from classes import adc1

adc1.readAdc()
adc1.calcTemp()
print('After calling method:', hex(adc1.adcVal), '|', adc1.TempVal )
'''

from classes import threadClass
from time import sleep

print('Creating Objects...')
th1 = threadClass( threadID= 101, delay= 0.5 )
th2 = threadClass( threadID= 102, delay= 1.5 )

print('Starting Threads...')
th1.start()
th2.start()

sleep(3)

th1.stopThread()
th2.stopThread()

print('Program Terminated!')
