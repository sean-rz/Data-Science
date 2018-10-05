# The groupby method allows you to group rows of data together and call aggregate functions

import pandas as pd

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
print df

# groupby() method to group rows together based off of a column name
print df.groupby('Company').mean()
print df.groupby('Company').std()
print df.groupby('Company').min()
print df.groupby('Company').max()
print df.groupby('Company').count()

print df.groupby('Company').describe()
print df.groupby('Company').describe().transpose()
print df.groupby('Company').describe().transpose()['GOOG']