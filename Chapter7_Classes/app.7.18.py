# to create an abstract class we need to import the ABC class from abc labrary (abstract class)
from abc import ABC, abstractmethod

# 18 - Abstract Base Clase


class InvalidOperationError(Exception):
    pass


class Stream(ABC):  # making an abstract class by inheriting from ABC
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod  # define abstract method tht is mandatory to be instantiated
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):

    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):

    def read(self):
        print("Reading data from a memory")


# TypeError: Can't instantiate abstract class MemoryStream with abstract method read

# stream = FileStream()
# stream.open()

# stream = Stream() #TypeError: Can't instantiate abstract class Stream with abstract method read

stream = MemoryStream()
stream.open()  # should be opened a stream without defining the type file stream or network stream
stream.read()
stream.close()

stream1 = FileStream()
stream1.open()
# stream1.open()
stream1.read()
stream1.close()
# stream1.close()
