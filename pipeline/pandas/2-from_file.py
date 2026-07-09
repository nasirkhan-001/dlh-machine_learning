#!/usr/bin/env python3
"""Module that use function to convert file to pandas DataFrame."""
import pandas as pd


def from_file(filename, delimiter):
    """Function that reads a CSV file and returns a pandas DataFrame."""
    data = pd.read_csv(filename, delimiter=delimiter)
    return data
