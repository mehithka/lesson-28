from abc import ABC, abstractmethod

class absclass(ABC):
    def print(self,x):
        print('passed value: ', x)

    @abstractmethod
    def task(self):
        print('inside abs class task')

#create sub class
class test_class(absclass):
    def task(self):
        print('we are inside test class task')

#object of test class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)  