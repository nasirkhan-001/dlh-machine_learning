#!/usr/bin/env python3
"""Module that slice pandas DataFrame."""


def slice(df):
    """Function that do slicing over specific columns of pandas DataFrame."""
    df = df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]
    return df
