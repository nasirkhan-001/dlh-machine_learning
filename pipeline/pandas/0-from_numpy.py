#!/usr/bin/env python3
"""this module is about convering numpy array to dataframe"""
import pandas as pd


def from_numpy(array):
    """Convert a NumPy array to a Dataframe."""
    no_of_col = array.shape[1]
    if array.shape[1] > 26:
        raise ValueError("array can not exceed 26 columns.")
    else:
        heading = []
        for i in range(no_of_col):
            heading.append(chr(i + 65))
        return pd.DataFrame(array, columns=heading)
