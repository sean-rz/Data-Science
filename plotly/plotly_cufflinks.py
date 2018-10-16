import cufflinks as cf
import plotly as py
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[5,4,3,2,1]})

# Scatter
fig = df.iplot(kind='scatter', x='A', y='B', mode='markers', size=10, asFigure=True)

#Bar Plots
fig = df2.iplot(kind='bar', x='Category', y='Values', asFigure=True)
fig = df.iplot(kind='bar', barmode='stack', asFigure=True)
fig = df.sum().iplot(kind='bar', asFigure=True)

# Boxplots
fig = df.iplot(kind='box', asFigure=True)

# 3d Surface
fig = df3.iplot(kind='surface', colorscale='rdylbu', asFigure=True)

# Spread
fig = df[['A','B']].iplot(kind='spread', asFigure=True)

# histogram
fig = df['A'].iplot(kind='hist', bins=25, asFigure=True)

fig = df.iplot(kind='bubble', x='A', y='B', size='C', asFigure=True)

# scatter_matrix() is similar to sns.pairplot()
fig = df.scatter_matrix(asFigure=True)

py.offline.plot(fig)
