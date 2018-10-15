import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt 

mpl.rcParams['patch.force_edgecolor'] = True  # gridlines between bins

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

print tips.head()
print flights.head()

#####################################################################
# heatmap: data should already be in a matrix form
#####################################################################

# Matrix form for correlation data
tips_corr = tips.corr()
print tips_corr

pvflights = flights.pivot_table(values='passengers', index='month', columns='year')
print pvflights

sns.heatmap(tips_corr)
sns.heatmap(tips_corr,cmap='coolwarm',annot=True)

sns.heatmap(pvflights)
sns.heatmap(pvflights,cmap='magma',linecolor='white',linewidths=1)

#####################################################################
# clustermap: uses hierarchal clustering to produce a clustered version 
# of the heatmap
#####################################################################

sns.clustermap(pvflights)
# years and months are no longer in order, instead they are grouped by similarity in value (passenger count). 

# More options to get the information a little clearer like normalization
sns.clustermap(pvflights, cmap='coolwarm', standard_scale=1)

plt.show()