# Reference: http://seaborn.pydata.org/tutorial/aesthetics.html

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['patch.force_edgecolor'] = True  # gridlines between bins


tips = sns.load_dataset('tips')

sns.set_style('darkgrid')
sns.countplot(x='sex', data=tips, palette='deep')
sns.despine() # Spine Removal
# sns.despine(left=True)

'''
matplotlib plt.figure(figsize=(width,height) * to change the size of 
most seaborn plots.
You can control the size and aspect ratio of most seaborn grid plots 
by passing in parameters: size, and aspect
'''
# Non Grid Plot
plt.figure(figsize=(12,3))
sns.countplot(x='sex',data=tips)

# Grid Type Plot
sns.lmplot(x='total_bill',y='tip',size=2,aspect=4,data=tips)

# The set_context allows to override default parameters
sns.set_context('poster',font_scale=4) # or notebook
sns.countplot(x='sex',data=tips,palette='coolwarm')

plt.show()