import sys


def file_to_list(fname):
    """Read a file and return a list newlines stripped and casted to int.
    
    :param fname: name of the file to read"""
    with open(fname) as f:
        content = [int(x.strip('\n')) for x in f.readlines()]
    return content


def count_split_inversions(count_array):
    """Count the split inversions in an array/list."""
    return 2


if __name__ == '__main__':
    try:
        contents = file_to_list(sys.argv[1])
    except KeyError:
        print('This script requires one file to read as an argument.')
        sys.exit(1)
