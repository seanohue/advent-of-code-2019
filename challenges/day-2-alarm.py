"""See https://adventofcode.com/2019/day/2"""
from functools import reduce
from utils import read_csv_file_as_numbers


class IntComputer:
    """
    An IntComputer implementation.
    """

    def __init__(self, program):
        """Init an IntComputer with a program."""
        self.program = program
        self.position = 0

    def get(self, position=None):
        """Get the value at a position in the program."""
        return self.program[
            position if position is not None else self.position]

    def step(self):
        """Read & execute the opcode at the current position."""
        return self.execute_op(self.get())

    def read(self, n=1):
        """Advance the program's position and return the value thereof."""
        return self.get(
            self.advance(n))

    def read_list(self, n=1):
        """
        Get and return the values at the next n positions."""
        return self.get_list(
            self.collect(n))

    def advance(self, n=1):
        """Advance the program's position and return it."""
        self.position += n
        return self.position

    def insert(self, position, value):
        """Insert a value at that position destructively."""
        self.program[position] = value
        print('Inserted value {} into pos <{}>.'.format(
            value, position))
        return True

    def execute_op(self, opcode):
        """Do as the opcode says."""
        switch = {
            1: 'add_op',
            2: 'multiply_op',
            99: 'end',
        }

        return getattr(self, switch[opcode], 'error')()

    def add_op(self, n=2):
        """Perform the add opcode."""
        value = self.add(n)
        position = self.read()
        self.advance()
        return self.insert(position, value)

    def multiply_op(self, n=2):
        """Perform the multiply opcode."""
        value = self.multiply(n)
        position = self.read()
        self.advance()
        return self.insert(position, value)

    def end(self):
        """Return false to end the program's execution."""
        return False

    def error(self):
        """Raise an exception due to invalid opcode."""
        raise Exception(
            'Invalid opcode: <{}>: {}'.format(
                self.position, self.read()))

    def add(self, n=2):
        """Add the next n values."""
        return sum(
            self.read_list(n))

    def multiply(self, n=2):
        """Multiply the next n values."""
        return reduce(
            (lambda x, y: x * y),
            self.read_list(n))

    def get_list(self, iterable):
        """Given a list of positions, return a list of values."""
        return list(map(self.get, iterable))

    def collect(self, n=0):
        """Collect values from the next n positions, advancing the program."""
        collection = []
        for _ in range(n):
            collection.append(
                self.get(
                    self.advance()))

        return collection

    def execute_program(self):
        executing = True
        while executing:
            print('<{}>: {}'.format(
                self.position, self.get()))
            executing = self.step()
        print('Done!')



def main():
    """Solve and print day 2's challenge."""
    print('Basic test:')
    basic_computer = IntComputer([1, 0, 0, 0, 99])
    basic_computer.execute_program()
    print(basic_computer.get(0) == 2)

    print('Full test:')
    program = read_csv_file_as_numbers('day-2-input.txt')
    computer = IntComputer(program)

    # Set up 1202 alarm state...
    computer.insert(1, 12)
    computer.insert(2, 2)
    computer.execute_program()
    print(computer.get(0))


if __name__ == "__main__":
    main()
