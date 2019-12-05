"""Utils to help with various challenges."""


def read_input_file_lines(filename):
    """Read and return the input file."""
    input_file = open(filename, 'r')
    lines = input_file.readlines()
    input_file.close()
    return lines


def list_to_int(values):
    """Turn a file's list of values into integers list"""
    return list(map(int, values))


def read_file_lines_as_numbers(filename):
    return list_to_int(
        read_input_file_lines(filename))


def read_csv_file_as_numbers(filename):
    input_file = open(filename, 'r')
    file_str = str(input_file.read())
    input_file.close()
    values = file_str.split(',')
    return list_to_int(values)
