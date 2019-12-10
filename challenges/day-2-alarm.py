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
        self.pointer = 0

    def get(self, address=None):
        """Get the value at a address in the program."""
        return self.program[
            address if address is not None else self.pointer]

    def step(self):
        """Read & execute the opcode at the current position."""
        return self.execute_op(self.get())

    def read(self, n=1):
        """Advance the program's position and return the value thereof."""
        return self.get(
            self.advance(n))

    def read_parameters(self, n=1):
        """
        Get and return the values at the next n positions."""
        return self.get_list(
            self.collect(n))

    def advance(self, n=1):
        """Advance the program's position and return it."""
        self.pointer += n
        return self.pointer

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
                self.pointer, self.read()))

    def add(self, n=2):
        """Add the next n values."""
        return sum(
            self.read_parameters(n))

    def multiply(self, n=2):
        """Multiply the next n values."""
        return reduce(
            (lambda x, y: x * y),
            self.read_parameters(n))

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
                self.pointer, self.get()))
            executing = self.step()
        print('Done!')



def main():
    """Solve and print day 2's challenge."""
    print('Basic test:')
    basic_computer = IntComputer([1, 0, 0, 0, 99])
    basic_computer.execute_program()
    print(basic_computer.get(0) == 2)

    noun = -1
    verb = 0
    result = None
    target = 19690720
    error = None
    initial_memory = read_csv_file_as_numbers('./day-2-input.txt')
    while result != target and not error:
        try:
            noun += 1
            # 160 is when the program maxes out
            if noun == 160:
                noun = 1
                verb += 1
            computer = IntComputer(list(initial_memory))
            computer.insert(1, noun)
            computer.insert(2, verb)
            computer.execute_program()
            result = computer.get(0)
        except Exception as e:
            error = e
            print(e)
            print('Failed at noun {} and verb {}'.format(noun, verb))

    code = (100 * noun) + verb
    print('program code is {}'.format(code))



if __name__ == "__main__":
    main()
