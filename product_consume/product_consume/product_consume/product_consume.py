from threading import Thread, Condition, Event
from heapq import heappush, heappop
import sys
import time
from random import randint


class CustomerOrder(Thread):
    __satcomProduct = ['L-Band Tx', 'L-Band Rx', 'NMS', '1x1 RSU', '1x4 RSU']
    __cbtvProduct = ['Tx', 'Rx']
    __proLen = len(__satcomProduct)-1

    def __init__(self, cvCusOrd):
        Thread.__init__(self)
        self.__queue = []
        self.__cvCusOrd = cvCusOrd

    def push(self, item, priority):
        heappush(self.__queue, (priority, item))

    #def pop(self):
    #    return heappop(self.__queue)

    def get_product(self) -> object:
        try:
            return heappop(self.__queue)
        except IndexError:
            print('No more item')
            return 0

    def run(self):
        #with self.__cvCusOrd:
        while True:
            self.__cvCusOrd.acquire()
            pro_name = self.__satcomProduct[randint(0, self.__proLen)]
            quantity = randint(1, 1000)
            #         (product name, quantity)   priority
            self.push( (pro_name, quantity), randint(1,5))
            print('Customer order ', quantity, 'of "', pro_name, '"')
            self.__cvCusOrd.notify()
            self.__cvCusOrd.release()
            time.sleep(10)


class ShippingDepartment(Thread):

    def __init__(self, cvShpDp):
        Thread.__init__(self)
        self.__cvShpDp = cvShpDp

    def run(self):
        #with self.__cvShpDp:
        while True:
            self.__cvShpDp.acquire()
            self.__cvShpDp.wait()
            self.theProduct = CustomerOrder.get_product()
            print('Products have shipped ', self.theProduct)
            self.__cvShpDp.release()


if __name__ == '__main__':

    print('Start program here')
    condition = Condition()
    cusOrder = CustomerOrder(condition)
    shpDep = ShippingDepartment(condition)
    cusOrder.start()
    shpDep.start()
    cusOrder.join()
    shpDep.join()
