from threading import Thread, Condition, Event, Semaphore
from heapq import heappush, heappop
import time
from random import randint


class productInfo():
    __queue = []

    def set_product(self, item, priority):
        heappush(self.__queue, (priority, item))

    def get_product(self):
        try:
            return heappop(self.__queue)
        except IndexError:
            print('No more item')
            return 0


class CustomerOrder(Thread):
    __orderType = ['Itar, nonItar']
    __satcomProduct = ['L-Band Tx', 'L-Band Rx', 'NMS', '1x1 RSU', '1x4 RSU']
    __cbtvProduct = ['Tx', 'Rx']
    __proLen = len(__satcomProduct) - 1

    def __init__(self, cvUSFact, items):
        Thread.__init__(self)
        self.__cvUSFact = cvUSFact
        self.__productInfo = items

    def run(self):
        # with self.__cvCusOrd:
        while True:
            self.__cvUSFact.acquire()
            pro_name = self.__satcomProduct[randint(0, self.__proLen)]
            quantity = randint(1, 1000)
            #           product name, quantity)        priority
            self.__productInfo.set_product((pro_name, quantity), randint(1, 5))
            print('Customer order ', quantity, 'of "', pro_name, '"')
            self.__cvUSFact.notify()
            self.__cvUSFact.release()
            time.sleep(randint(5, 50))


class ShippingDepartment(Thread):

    def __init__(self, evtShpDp, items):
        Thread.__init__(self)
        self.__evtShpDp = evtShpDp
        self.__productInfo = items

    def run(self):
        # with self.__cvShpDp:
        while True:
            self.__evtShpDp.wait()
            print('Products have shipped ')
            self.__evtShpDp.clear()
            #self.__cvShpDp.release()
