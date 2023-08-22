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
        self.next_number = start

    def __repr__(self):
        """Returns info about generated instance"""
        return f'start ={self.start} and nextNumber= {self.next_number}'

    def generate(self):
        """Returns count, then increments by 1"""
        self.start += 1
        return self.next_number - 1

    def reset(self):
        """Resets count to inital value"""
        self.currentCount = self.start


