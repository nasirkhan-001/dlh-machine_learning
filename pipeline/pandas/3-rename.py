#!/usr/bin/env python3
"""Module that use function to rename pandas DataFrame."""
import pandas as pd


def rename(df):
    """Function that modify pandas DataFrame."""
    # syntax for renaming function are around 10 and most common used are:
    # index, columns, inplace, level, errors, copy, axis, mapper, & others.
    # index to play with rows lables while columns is around headers
    # inplace is to make changes in original DF, by default its false
    # which means dont modify orignal DF and return new DF with changes
    # level is to rename the index of a MultiIndex DataFrame
    # errors is to handle raise them or ignore them upon changes in
    # in DF, and by default it ignores errors
    df = df.rename(columns={'Timestamp': 'Datetime'})
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')
    df = df[['Datetime', 'Close']]
    return df
