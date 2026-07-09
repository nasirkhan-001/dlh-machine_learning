#!/usr/bin/env python3
"""Module that sorting values in DataFrame."""


def high(df):
    """Function that sort values in particular column of DataFrame."""
    # no panda import needed as df is defined already
    # sort_index will work on row modification
    # sort_value will work on values modification
    df = df['High'].sort_values(descending=True)
    return df
