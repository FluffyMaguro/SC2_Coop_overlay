"""Utility functions to read text files to Python data structures."""

import csv


def csv_to_dictitems(filename, header=1):
    """Read a CSV and return a dictionary of {column1: column2} pairs
    
    `header` defaults to 1, for human readable CSV's, and is ignored.
    """
    with open(filename, newline='') as fh:
        # reader = csv.DictReader(fh)
        # print(dict(row.values() for row in reader))
        reader = csv.reader(fh)
        for _ in range(header):
            next(reader)
        return {row[0]: row[1] for row in reader if row}

def txt_to_iter(filename, header=0, factory=set):
    """Read a single-column text file to an appropriate iterable.
    
    Assumes no header (iterable as a column)
    `factory` defaults to `set` based on the original data.
    """
    with open(filename, newline='') as fh:
        reader = csv.reader(fh)
        for _ in range(header):
            next(reader)
        return factory(row[0] for row in reader if row)

def csv_to_comastery_dict(filename, header=1):
    """Read a CSV of CO and Six masteries as {key: [list]} pairs
    
    `header` defaults to 1, for human readable CSV's, and is ignored.
    output: {column1: [column2, ..., column7], ...}
    """
    with open(filename, newline='') as fh:
        reader = csv.reader(fh)
        for _ in range(header):
            next(reader)
        return {row[0]: row[1:] for row in reader if row}
