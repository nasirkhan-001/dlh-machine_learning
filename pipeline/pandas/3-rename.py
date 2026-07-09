#!/usr/bin/env python3
"""Module that use function to rename pandas DataFrame."""
import pandas as pd


def rename(df):
    """Function that modify pandas DataFrame."""
    df = df.rename(columns={'Timestamp': 'Datetime'})
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
    df = df[['Datetime', 'Close']]
    return df
