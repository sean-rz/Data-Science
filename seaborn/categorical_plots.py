# x-axis is a categorical data

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['patch.force_edgecolor'] = True  # gridlines between bins
#%matplotlib inline

tips = sns.load_dataset('tips')
print tips.head()

##############################################################
# barplot: allows you to aggregate the categorical data based 
# off some function, by default the mean
##############################################################
sns.barplot(x='sex', y='total_bill', data=tips)
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)

##############################################################
# countplot: essentially the same as barplot except the 
# estimator is explicitly counting the number of occurrences
##############################################################
sns.countplot(x='sex', data=tips)

####################################################################
# boxplot: shows the distribution of quantitative data across 
# levels of a categorical variable 
# https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51
# https://www.youtube.com/watch?v=CoVf1jLxgj4
####################################################################
sns.boxplot(x='day', y='total_bill', data=tips, palette='rainbow')

# Can do entire dataframe with orient='h'
sns.boxplot(data=tips,palette='rainbow',orient='h')

sns.boxplot(x="day", y="total_bill", hue="smoker",data=tips, palette="coolwarm")

####################################################################
# violinplot: plays a similar role as a box and whisker plot. 
# It shows the distribution of quantitative data across several  
# levels of one (or more) categorical variables such that those 
# distributions can be compared. The violin plot features a kernel 
# density estimation of the underlying distribution
####################################################################
sns.violinplot(x="day", y="total_bill", data=tips,palette='rainbow')
sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',palette='Set1')
sns.violinplot(x="day", y="total_bill", data=tips,hue='sex',split=True,palette='Set1')

####################################################################
# stripplot: draw a scatterplot where one variable is categorical 
####################################################################
sns.stripplot(x="day", y="total_bill", data=tips)
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True)
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1')
sns.stripplot(x="day", y="total_bill", data=tips,jitter=True,hue='sex',palette='Set1',split=True)

####################################################################
# swarmplot: is similar to stripplot, but the points are adjusted 
# only along the categorical axis so that they don't overlap
# it does not scale as well to large numbers of observations
####################################################################
sns.swarmplot(x="day", y="total_bill", data=tips)
sns.swarmplot(x="day", y="total_bill", hue='sex', data=tips, palette="Set1", split=True)

####################################################################
# factorplot: is the most general form of a categorical plot. 
# It can take in a kind parameter to adjust the plot type
####################################################################
sns.factorplot(x='sex', y='total_bill', data=tips, kind='bar')

# Combining Categorical Plots
sns.violinplot(x='tip', y='day', data=tips, palette='rainbow')
sns.swarmplot(x='tip', y='day', data=tips, color='black', size=3)

plt.show()

