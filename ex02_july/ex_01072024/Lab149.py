from abc import ABC, abstractmethod

class ATB(ABC):

    def enrolled(self):
        print("Enrolled")

    @abstractmethod
    def perform_task1(self):
        pass

    @abstractmethod
    def perform_task2(self):
        pass


class Amit(ATB):
    def perform_task1(self):
        return "Done1"

    def perform_task2(self):
        return "Done2"


amit= Amit()
print(amit.perform_task2())
print(amit.perform_task1())