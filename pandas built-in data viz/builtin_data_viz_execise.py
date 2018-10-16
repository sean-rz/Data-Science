import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['patch.force_edgecolor'] = True

df3 = pd.read_csv('df3')
print df3.head()

# scatter plot of b vs a
df3.plot.scatter(x='a', y='b', c='red', s=50, figsize=(12,3)) # s for size

plt.style.use('ggplot')
df3['a'].plot.hist(alpha=0.5,bins=25) # alpha for transparency

# boxplot comparing the a and b columns
df3[['a','b']].plot.box()


df3['d'].plot.kde()
df3['d'].plot.density(lw=5,ls='--') # dashed linestyle


# just for rows up to 30
df3.ix[0:30].plot.area(alpha=0.4)


# display the legend outside of the plot
f = plt.figure()
df3.ix[0:30].plot.area(alpha=0.4,ax=f.gca())
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))

plt.show()
