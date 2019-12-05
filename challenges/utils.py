"""Utils to help with various challenges."""


def read_input_file(filename):
    """Read and return the input file."""
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    input_file.close()
    return lines


def file_to_numbers(lines):
    """Turn a file's lines list into integers list"""
    return list(map(int, lines))
