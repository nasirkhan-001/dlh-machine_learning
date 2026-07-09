#!/usr/bin/env python3
"""Module that convert pandas DataFrame back to array."""
import pandas as pd


def array(df):
    """Function that return an numpy array from pandas DataFrame."""
    df = df[['High', 'Close']].tail(10).to_numpy()
    return df
