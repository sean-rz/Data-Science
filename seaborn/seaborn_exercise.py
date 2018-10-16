import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['patch.force_edgecolor'] = True  # gridlines between bins


sns.set_style('whitegrid')

titanic = sns.load_dataset('titanic')
print titanic.head()


sns.jointplot(x='fare', y='age', data=titanic)

sns.distplot(titanic['fare'], bins=30, kde=False, color='red')

sns.boxplot(x='class', y='age', data=titanic, palette='rainbow')

sns.swarmplot(x='class', y='age', data=titanic, palette='Set2')

sns.countplot(x='sex',data=titanic)


sns.heatmap(titanic.corr(), cmap='coolwarm')
plt.title('titanic.corr()')


g = sns.FacetGrid(data=titanic, col='sex')
g.map(plt.hist, 'age')

plt.show()
