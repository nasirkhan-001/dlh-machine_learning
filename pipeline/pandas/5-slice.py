#!/usr/bin/env python3
"""Module that slice a DataFrame using iloc function"""


def slice(df):
    """Function that do slicing at specific location in DataFrame."""
    df = df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]
    return df
