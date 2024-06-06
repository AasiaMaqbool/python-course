from abc import ABC,abstractmethod
class company(ABC):
    def work(self):
       pass
class Manager(company):
    def work(self):
        print("I assign work to mange team")
class Employee(company):
    def work(self):
       print("I complete the work assign to me")

R=Manager()
R.work

K=Employee()
K.work()