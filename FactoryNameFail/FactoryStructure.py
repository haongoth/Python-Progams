from abc import ABCMeta, abstractmethod

#class Factory(metaclass=ABCMeta):
   # @abstractmethod
    #def make_product(self):
    #    raise NotImplementedError()

class US_Factory(metaclass=ABCMeta):
    @abstractmethod
    def make_product(self):
        print("These products make in USA")

class SatCom(US_Factory):
    def make_product(self):
        print("These make by SatCom group in USA")

class CATV(US_Factory):

    def make_product(self):
        print("These make by CATV group in USA")

class Gyro(US_Factory):
    def make_product(self):
        print("These make by Gyro group in USA")

class NonUS_Factory(metaclass=ABCMeta):
    @abstractmethod
    def make_product(self):
        print("These products make in China")

class SatCom(NonUS_Factory):
     def make_product(self):
        print("These make by SatCom group in Thailand")

class CATV(NonUS_Factory):
    def make_product(self):
        print("These make by CATV group in China")

if __name__ == '__main__':
  
    aFactoryNonUS = CATV()
    aFactoryUS = CATV()
    aFactoryNonUS.make_product()
    aFactoryUS.make_product()

