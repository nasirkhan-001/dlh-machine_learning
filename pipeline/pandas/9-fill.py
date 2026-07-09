#!/usr/bin/env python3
"""Module that fill missing values in pandas DataFrame."""


def fill(df):
    """Function that fill empty cells in row and column of DF."""
    # remove weighted price col at all and 1 represent col index
    df = df.drop(['Weighted_Price'], axis=1)

    # doing forward fill for close column
    df['Close'] = df['Close'].ffill()

    # it was not possible to fill each column with close value in 
    # one go like, see below 
    # df[['High', 'Low', 'Open']] = df[['High', 'Low', 'Open']].fillna(df['Close'])
    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])

    # its possible to fill multiple column with empty cell 
    # with 0 in one go, see below 
    df[['Volume_(BTC)', 'Volume_(Currency)']] = df[[
        'Volume_(BTC)', 'Volume_(Currency)']].fillna(0)
    return df
