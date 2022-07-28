from abc import ABC, abstractmethod


class AbstractReader(ABC): 
    """
    it's abstract class for future Reader class
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def read(self):
        """
        it's method for read file
        """
        pass
    
    @abstractmethod
    def write(self):
        """
        it's method for write file
        """

