from abc import ABC, abstractmethod


class Records(ABC):
    @abstractmethod
    def saveRecords(self):  # Save records of any type depends upon which class is implementing this
        pass
