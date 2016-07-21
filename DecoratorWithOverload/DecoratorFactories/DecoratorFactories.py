from random import randint

# PythonDecorators/DecoratorFactories.py
class Factory():

    """
    Contructor overload will runs okay if __init__(self) never get call;
    however, will crack if get call
    """
    """
    If there are decorator arguments, the function
    to be decorated is not passed to the constructor!
    """
    def __init__(self):             
        print("No order")

    def __init__(self, aFac):
        self.__aFac = aFac
        #print("Get Order: ", self.__aFac)

    """
    If there are decorator arguments, __call__() is only called
    once, as part of the decoration process! You can only give
    it a single argument, which is the function object
    """
    def __call__(self):
        def doNothing(*args):
            print('delete order from database')
        return doNothing

    def __call__(self, f):
        def doSomething(*args):
            print(f.__name__, ': ', self.__aFac)
            if(f.__name__ == 'makeProducts'):
                f(*args)
        return doSomething



if __name__ == '__main__':

    itemOrder = ['noOrder', 'Satcom', 'CATV', 'Gyro']
    orderType = ['Itar', 'nonItar']

    item1 = itemOrder[randint(0, 3)]
    item2 = orderType[randint(0, 1)]

    if item1 == 'noOrder':
        # Python doesn't support overload function
        # contructor overload and operator overload will crack the whole program when call 
        @Factory()          
        def makeOrder():
            print('Customer has cancel or no order')
    else:        
        @Factory(item1)
        def makeOrder(aWorld):
            pass                        # never get call
            
        @Factory(item1)
        def makeProducts(isItar):
            if isItar == 'Itar' or item1 == 'Gyro':
                print('These products make in US')
            elif item1 == 'Satcom':
                print('These products make in ThaiLand')
            else:
                print('These products make in China')
                 
            
    makeFrom = ['USA', 'China', 'ThaiLand']
    makePro = makeFrom[randint(0, 2)]
    makeOrder(makePro)
    makeProducts(item2)
