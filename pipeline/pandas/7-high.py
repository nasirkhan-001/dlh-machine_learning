#!/usr/bin/env python3
"""Module that sorting values in DataFrame."""


def high(df):
    """Function that sort values in particular column of DataFrame."""
        # no panda import needed as df is defined already
    # sort_index will work on row modification
    # sort_value will work on values modification
    # df = df['High'].sort_values(descending=True)
    # this sort values only in cloumn high but task need whole
    # DF to be sorted based on values in high column
    # descending does not exist as parameter so use only ascending
    # column can be selected using by='High' or ['High']
    df = df.sort_values(['High'], ascending=False)
    return df
