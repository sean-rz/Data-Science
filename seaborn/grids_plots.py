import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt 

mpl.rcParams['patch.force_edgecolor'] = True  # gridlines between bins

iris = sns.load_dataset('iris')
print iris.head()
print iris['species'].unique()  # number of species

##################################################################
#Grids: general types of plots that allow you to map plot types to 
#rows and columns of a grid

# Pairgrid: is a subplot grid for plotting pairwise relationships in a dataset
##################################################################

# Just the Grid
g = sns.PairGrid(iris)
# Then you map to the grid
g.map(plt.scatter)


# Map to upper,lower, and diagonal
g = sns.PairGrid(iris)
g.map_diag(plt.hist)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

##################################################################
# pairplot: pairplot is a simpler version of PairGrid
##################################################################
sns.pairplot(iris, hue='species', palette='rainbow', diag_kind='hist')

##################################################################
# Facet Grid: general way to create grids of plots based off of a feature
##################################################################
tips = sns.load_dataset('tips')
print tips.head()

g = sns.FacetGrid(tips, col="time", row="smoker") # Just the Grid
g = g.map(plt.hist, "total_bill")
# g = g.map(sns.distplot, 'total_bill')


g = sns.FacetGrid(tips, col="time",  row="smoker",hue='sex')
# Notice hwo the arguments come after plt.scatter call
g = g.map(plt.scatter, "total_bill", "tip").add_legend()

plt.show()