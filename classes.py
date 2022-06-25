# Class

class adcBoard:
    def __init__(self, busCh, Addr):
        self.busCh = busCh
        self.Addr = Addr
        self.adcVal = 0
        self.TempVal = 0

    def readAdc( self ):
        # Reading ADC value from board
        self.adcVal = 0x12

    def calcTemp(self):
        # Calculations to convert ADC value to 'C
        self.TempVal = self.adcVal + 273


# Three Objects for class adcBoard

adc1 = adcBoard( busCh= 1, Addr= 0x21 ) # Constructor: Member function/Method with same name of the class
adc2 = adcBoard( busCh= 1, Addr= 0x25 )
adc3 = adcBoard( busCh= 2, Addr= 0x31 )


# Multi-threading Class
from threading import Thread, Event
from time import sleep

class threadClass(Thread):
    def __init__( self, threadID, delay ):
        Thread.__init__(self) # Calling Super class constructor
        self.threadID = threadID
        self._stopper = Event()
        self.delay = delay
        self.count = 0

    def run(self):
        while not self.stopped():
            print(self.threadID, ':', self.count)
            self.count += 1
            sleep(self.delay) # in seconds

    def stopped(self):
        return self._stopper.isSet()

    def stopThread(self):
        self._stopper.set()




if __name__ == '__main__':
        
    '''
    print( hex(adc1.Addr) )
    print( hex(adc2.Addr) )
    print( hex(adc3.Addr) )
    '''
    print('Before calling method:', adc1.adcVal)

    adc1.readAdc()
    adc1.calcTemp()
    print('After calling method:', hex(adc1.adcVal), '|', adc1.TempVal )

