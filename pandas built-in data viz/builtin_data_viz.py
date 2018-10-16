import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['patch.force_edgecolor'] = True

df1 = pd.read_csv('df1', index_col=0)  # index will be column 0
df2 = pd.read_csv('df2')

print df1.head()
print df2.head()

plt.style.use('ggplot')  # matplotlib style
'''
matplotlib style sheets: https://matplotlib.org/gallery.html#style_sheets
plt.style.use('bmh')
plt.style.use('dark_background')
plt.style.use('fivethirtyeight')
'''

df1['A'].hist()

df2.plot.area(alpha=0.4)

df2.plot.bar()
df2.plot.bar(stacked=True)

df1['A'].plot.hist(bins=50)

df1.plot.line(x=df1.index.name, y='B', figsize=(12,3), lw=1)

df1.plot.scatter(x='A', y='B')

#use c to color based off another column value.Use cmap to indicate colormap to use
df1.plot.scatter(x='A',y='B',c='C',cmap='coolwarm')

#use s to indicate size based off another column
# s parameter needs to be an array, not just the name of a column
df1.plot.scatter(x='A',y='B',s=df1['C']*200)


df2.plot.box() # Can also pass a by= argument for groupby


df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df.plot.hexbin(x='a',y='b',gridsize=25,cmap='Oranges')


df2['a'].plot.kde()
df2.plot.density()

plt.show()

