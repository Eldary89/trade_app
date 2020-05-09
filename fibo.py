import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import math

data=pd.read_csv('eurgbp_d.csv')
data['date'] = pd.to_datetime(data['date'])
print(data.head(30))

levels = pd.DataFrame()
levels['date'] = data['date']
levels['h-l'] = data['high'] - data['low']

# Entry level buy orders
levels['lev1b']= data['high']- levels['h-l']*0.236
levels['lev2b']= data['high']- levels['h-l']*0.382
levels['lev3b']= data['high']- levels['h-l']*0.50
levels['lev4b']= data['high']- levels['h-l']*0.618
levels['lev5b']= data['high']- levels['h-l']*0.7647

#Entry level sell order
levels['lev1s']= data['low']+ levels['h-l']*0.236
levels['lev2s']= data['low']+ levels['h-l']*0.382
levels['lev3s']= data['low']+ levels['h-l']*0.50
levels['lev4s']= data['low']+ levels['h-l']*0.618
levels['lev5s']= data['low']+ levels['h-l']*0.7647

print(levels.head(30))

open_trade = pd.DataFrame()
open_trade['date'] = data['date'].loc[lambda s: levels['h-l'] > data['atr']]
dates = data['date'].isin(open_trade['date'])
dates_lev = levels['date'].isin(open_trade['date'])

open_trade['buy_or_sell'] = np.where(
    data['open'].loc[dates] < data['close'].loc[dates],
    'buy', 'sell'
)

open_trade['lev1btp'] = data['high'].loc[dates] + levels['h-l'].loc[dates] * 1.236
open_trade['lev2btp'] = data['high'].loc[dates] + levels['h-l'].loc[dates] * 1.382
open_trade['lev3btp'] = data['high'].loc[dates] + levels['h-l'].loc[dates] * 1.5
open_trade['lev4btp'] = data['high'].loc[dates] + levels['h-l'].loc[dates] * 1.618
open_trade['lev5btp'] = data['high'].loc[dates] + levels['h-l'].loc[dates] * 1.7647

open_trade['lev1stp'] = levels['lev1s'].loc[dates_lev] - levels['h-l'].loc[dates_lev]
open_trade['lev2stp'] = levels['lev2s'].loc[dates_lev] - levels['h-l'].loc[dates_lev]
open_trade['lev3stp'] = levels['lev3s'].loc[dates_lev] - levels['h-l'].loc[dates_lev]
open_trade['lev4stp'] = levels['lev4s'].loc[dates_lev] - levels['h-l'].loc[dates_lev]
open_trade['lev5stp'] = levels['lev5s'].loc[dates_lev] - levels['h-l'].loc[dates_lev]

print(open_trade.head(30))

close_trade = pd.DataFrame()

def find_date(x):
    return data['date'].loc[data['date'] > x & ]

close_trade['date'] = open_trade['date'].apply(find_date)
print(close_trade)