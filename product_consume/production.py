from threading import Thread, Event
import time
from random import randint


class US_factory(Thread):

    __quantity = 0

    def __init__(self, cvFactory, evtFactory, items):
        Thread.__init__(self)
        self.__cvFactory = cvFactory
        self.__evtFactory = evtFactory
        self.__items = items

    def run(self):
        # with self.__cvShpDp:
        self.__cvFactory.acquire()
        while True:
            self.__cvFactory.wait()
            totalProBuilt = 0
            #theProduct = self.__items.get_product()
            priority, (productName, __quantity) = self.__items.get_product() #theProduct
            self.__cvFactory.release()
            while(__quantity > 0):
                numProdone = randint(1, 100)
                if(__quantity > numProdone):
                    __quantity -= numProdone
                else:
                    __quantity = 0
            #assert isinstance(self.quantity, object)
            #print('Products have done ', self.priodity, ' ', self.prodName,' ',self.quantity)
                totalProBuilt += numProdone
                print(numProdone, ' ', productName, ' have done this week in US')
                time.sleep(1)
            print('Total ', productName, 'have built in US: ',totalProBuilt)
            self.__cvFactory.acquire()
            print('US factory sends ', totalProBuilt, 'of ', productName, ' to shipping department')
            self.__evtFactory.set()


class nonUS_factory(Thread):

    __quantity = 0

    def __init__(self, cvFactory, evtFactory, items):
        Thread.__init__(self)
        self.__cvFactory = cvFactory
        self.__evtFactory = evtFactory
        self.__items = items

    def run(self):
        # with self.__cvShpDp:
        self.__cvFactory.acquire()
        while True:
            self.__cvFactory.wait()
            totalProBuilt = 0
            #theProduct = self.__items.get_product()
            priority, (productName, __quantity) = self.__items.get_product() #theProduct
            self.__cvFactory.release()
            while(__quantity > 0):
                numProdone = randint(1, 100)
                if(__quantity > numProdone):
                    __quantity -= numProdone
                else:
                    __quantity = 0
            #assert isinstance(self.quantity, object)
            #print('Products have done ', self.priodity, ' ', self.prodName,' ',self.quantity)
                totalProBuilt += numProdone
                print(numProdone, ' ', productName, ' have done this week in China')
                time.sleep(1)
            print('Total ', productName, 'have been built in China: ',totalProBuilt)
            self.__cvFactory.acquire()
            print('China factory sends ', totalProBuilt, 'of ', productName, ' to shipping department')
            self.__evtFactory.set()
