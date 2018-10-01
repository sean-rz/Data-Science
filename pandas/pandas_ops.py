import pandas as pd

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print df.head()

print df['col2'].unique()   # list of unique values
print df['col2'].nunique()  # number of unique values
print df['col2'].value_counts()
print type(df['col2'].value_counts()) # <class 'pandas.core.series.Series'>
print df['col2'].value_counts()[444]  # 2


#Select from DataFrame using criteria from multiple columns
newdf = df[(df['col1'] > 2) & (df['col2'] ==444)] 
print newdf


# Applying Functions
def times2(x):
    return x*2

print df['col1'].apply(times2) # broadcast function to values
print df['col3'].apply(len)
print df['col2'].apply(lambda x: x*2)
print df['col1'].sum()


print df.drop('col1', axis=1)
del df['col1']  # Permanently Removing a Column
print df


# Get column and index names
print df.columns  # Index(['col2', 'col3'], dtype='object')
print df.index  # RangeIndex(start=0, stop=4, step=1)


# Sorting and Ordering a DataFrame
print df.sort_values(by='col2')   #inplace=False by default

# Find Null Values or Check for Null Values
print df.isnull()

# pivot table
data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]}
df = pd.DataFrame(data)
print df

print df.pivot_table(values='D', index=['A','B'], columns=['C'])