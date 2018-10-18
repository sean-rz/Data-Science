import pandas as pd
import numpy as np 
import datetime
import pickle
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt 
import plotly
import cufflinks as cf

cf.go_offline()
sns.set_style('whitegrid')
mpl.rcParams['patch.force_edgecolor'] = True # gridlines between bins


df = pd.read_pickle('all_banks')
print(df.head())

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
df.columns.names = ['Bank Ticker','Stock Info']

print(df.xs(key='Close', axis=1, level='Stock Info').max())

returns = pd.DataFrame()

for tick in tickers:
    returns[tick + ' Return'] = df[tick]['Close'].pct_change()
print(returns.head())

sns.pairplot(returns[1:])

min_return_date = returns.idxmin()
max_return_date = returns.idxmax()

riskiest_stock = returns.std().idxmax()
riskiest_stock_2015 = returns.loc['2015-01-01':'2016-12-31'].std()

sns.distplot(returns.loc['2015-01-01':'2016-12-31']['MS Return'], color='green', bins=100)
sns.distplot(returns.loc['2008-01-01':'2008-12-31']['C Return'], color='red', bins=100)

# Close price for each bank for the entire index of time
df.xs(key='Close', axis=1, level='Stock Info').plot()

df.xs(key='Close', axis=1, level='Stock Info').iplot()

for tick in tickers:
    df[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()

# Moving averages for 30 days
plt.figure(figsize=(12,6))
df['BAC']['Close'].loc['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg')
df['BAC']['Close'].loc['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE')
plt.legend()

# heatmap of the correlation between the stocks Close Price
sns.heatmap(df.xs(key='Close', axis=1, level='Stock Info').corr(), annot=True)
sns.clustermap(df.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)

close_corr = df.xs(key='Close', axis=1, level='Stock Info').corr()
close_corr.iplot(kind='heatmap',colorscale='rdylbu')

# plt.show()


# Ref: https://www.udemy.com/python-for-data-science-and-machine-learning-bootcamp
