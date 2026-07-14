#!/usr/bin/env python3
"""Module that use hierarchical indexing for two DataFrame."""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Task that apply hierarchical indexing over DataFrames."""
    df1 = index(df1)
    df2 = index(df2)
    df1 = df1.loc[1417411980:1417417980]
    df2 = df2.loc[1417411980:1417417980]
    df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
    # now df is multiindex, like outer level or grouping is by
    # bitstamp and coinbase while secondly index by timestamp
    # column values and syntax for df.swaplevel(exchange, timestamp)
    # df.swaplevel(col_name_with_index_to_change, new_index_col_name)
    # 0 is outer index, 1 is inner, and if 2, it will more inner
    # swap will simply move timestamp col as first index while
    # bitstamp and coinbase column as secind index
    df = df.swaplevel(0, 1)
    df = df.sort_index()
    return df
