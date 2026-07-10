#!/usr/bin/env python3
"""Module that show stats of DataFrame."""


def analyze(df):
    """Function that show descriptive state of DataFrames."""
    df = df.drop(columns='Timestamp').describe()
    return df
