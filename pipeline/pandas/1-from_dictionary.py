#!/usr/bin/env python3
"""Module that use function to convert Dictionary to pandas DataFrame."""
import pandas as pd

df = pd.DataFrame({
    'First': [0.0, 0.5, 1.0, 1.5],
    'Second': ['one', 'two', 'three', 'four']
    }, index=['a', 'b', 'c', 'd'])
