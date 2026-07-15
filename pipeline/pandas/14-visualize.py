#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df = df.drop(columns="Weighted_Price")
df = df.rename(columns={"Timestamp": "Date"})
df['Date'] = pd.to_datetime(df["Date"], unit="s")
df = df.set_index("Date")
df["Close"] = df["Close"].ffill()
df["High"] = df["High"].fillna(["Close"])
df["Low"] = df["Low"].fillna(["Close"])
df["Open"] = df["Open"].fillna(["Close"])
df[["Volume_(BTC)", "Volume_(Currency)"]] = df[[
    "Volume_(BTC)", "Volume_(Currency)"]].fillna(0)
df = df.loc[2017:]
df = df.resample("D").agg({
    "High": "max"
    "Low": "min"
    "Open": "mean"
    "Close": "mean"
    "Volume_(BTC): "sum"
    "Volume_(Currency): "sum"
    })
df.plot()
df.show()
