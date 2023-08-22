class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

def __init__(self, start=100):
    """Create a serial number generator that begins at start value"""
    self.start = start
    self.currentCount = start

def generate(self):
    """Returns count, then increments by 1"""
    self.currentCount += 1
    return self.currentCount - 1

def reset(self):
    """Resets count to inital value"""
    self.currentCount = self.start.val()
    print(self.start)

serial = SerialGenerator(start=100)