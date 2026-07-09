#!/usr/bin/env python3
"""Module that filpping a DataFrame."""


def flip_switch(df):
    """Function that do sorting and transpose a DataFrame."""
    # no panda import needed as df is defined already
    # sort_index will work on row modification
    # sort_value will work on values modification
    # transpose will flip column and row of DF
    # index sort will result in last row will appear first
    df = df.sort_index(ascending=False).T
    return df
