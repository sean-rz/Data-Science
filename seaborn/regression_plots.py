import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt 

mpl.rcParams['patch.force_edgecolor'] = True  # gridlines between bins

tips = sns.load_dataset('tips')
print tips.head()

#######################################################################
'''
lmplot allows you to display linear models, but it also conveniently 
allows you to split up those plots based off of features, as well as 
coloring the hue based off of features.
'''
#######################################################################

sns.lmplot(x='total_bill', y='tip', data=tips)
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm')


# http://matplotlib.org/api/markers_api.html
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='coolwarm',
           markers=['o','v'], scatter_kws={'s':100})  # marker size of 100

#######################################################################
'''
We can add more variable separation through columns and rows with the 
use of a grid. Just indicate this with the col or row arguments
'''
#######################################################################
sns.lmplot(x='total_bill',y='tip',data=tips,col='sex') # 1 row 2 cols
sns.lmplot(x="total_bill", y="tip", row="sex", col="time",data=tips)
sns.lmplot(x='total_bill', y='tip', data=tips, col='day', hue='sex', palette='coolwarm')

# adjust size and aspect ratio
sns.lmplot(x='total_bill', y='tip',data=tips, col='day', hue='sex', palette='coolwarm', aspect=0.6, size=8)


plt.show()

