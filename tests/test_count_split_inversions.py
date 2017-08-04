"""Tests for stanford_algorithms.count_split_inversions."""
from os.path import join
from os import getcwd
from stanford_algorithms import count_split_inversions


def test_file_to_list():
    contents = count_split_inversions.file_to_list(
        join(getcwd(), 'sample_data/integer_array.txt'))
    assert len(contents) == 100000


def test_count_split_inversions():
    """Test for the info function."""
    contents = count_split_inversions.file_to_list(
        join(getcwd(), 'sample_data/integer_array.txt'))
    assert count_split_inversions.count_split_inversions(contents) == 1
