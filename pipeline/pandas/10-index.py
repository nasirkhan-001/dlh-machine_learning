#!/usr/bin/env python3
"""Module that set index of DataFrame."""


def index(df):
    """Function that enables timestamp column as  index for DF."""
    df = df.set_index('Timestamp')
    return df
