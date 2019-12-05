"""
First challenge of AoC.
https://adventofcode.com/2019/day/1
"""
from functools import reduce
from math import floor
from .utils import file_to_numbers, read_input_file


def sum_fuel(a, b):
    """Use to reduce a list of module masses to fuel sum."""
    return a + calculate_module_fuel(b)


def calculate_module_fuel(module_mass):
    """"Use to calculate fuel for a module including fuel for fuel."""
    fuel = calculate_fuel(module_mass)
    additional_fuel = calculate_fuel(fuel)
    while additional_fuel > 0:
        fuel += additional_fuel
        additional_fuel = calculate_fuel(additional_fuel)
    return fuel


def calculate_fuel(mass):
    """Use to calculate fuel for any individual mass."""
    return max([floor(mass / 3) - 2, 0])


def main():
    """Solve and print day 1's challenge."""
    masses = file_to_numbers(
        read_input_file('day-1-input.txt'))
    masses.insert(0, 0)
    fuel = reduce(sum_fuel, masses)

    print("Fuel: {}".format(fuel))


if __name__ == "__main__":
    main()
