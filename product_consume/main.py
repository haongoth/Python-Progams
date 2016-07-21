import threading
import customerOrder
import production

if __name__ == '__main__':

    print('Start program with 4 threads running.')
    condition = threading.Condition()
    eventDriven = threading.Event()
    #condition = threading.Semaphore()
    dataItems = customerOrder.productInfo()
    shipDep = customerOrder.ShippingDepartment(eventDriven, dataItems)
    cusOrder = customerOrder.CustomerOrder(condition, dataItems)
    usFac = production.US_factory(condition, eventDriven, dataItems)
    nonUsFac = production.nonUS_factory(condition, eventDriven, dataItems)
    shipDep.start()
    usFac.start()
    nonUsFac.start()
    cusOrder.start()
    shipDep.join()
