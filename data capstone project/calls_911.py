import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
sns.set_style('whitegrid')

df = pd.read_csv('911.csv')

print df.info()
print df.head(3)

# What are the top 5 zipcodes for 911 calls
print df['zip'].value_counts().head(5)

# What are the top 5 townships (twp) for 911 calls
print df['twp'].value_counts().head(5)

# how many unique title codes are there
print df['title'].nunique()

# Creating new features
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])

# What is the most common Reason for a 911 call
print df['Reason'].value_counts().head(3)

# create a countplot of 911 calls by Reason
sns.countplot(x='Reason',data=df,palette='viridis')

# convert the column from strings to DateTime objects
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# 3 new columns called Hour, Month, and Day of Week
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

# map the actual string names to the day of the week
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)

# countplot of the Day of Week column with the hue based off of the Reason column
sns.countplot(x='Day of Week',data=df,hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.) # To relocate the legend

# the same for Month
sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#group the DataFrame by the month column and use the count() method for aggregation
byMonth = df.groupby('Month').count()

#plot off of the dataframe indicating the count of calls per month
# Could be any column
byMonth['twp'].plot()

#create a linear fit on the number of calls per month
# you need to reset the index to a column
sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())

# groupby the Date column with the count() aggregate and create a plot of counts of 911 calls
df['Date'] = df['timeStamp'].apply(lambda t: t.date())

#https://scentellegher.github.io/programming/2017/05/24/pandas-bar-plot-with-formatted-dates.html
df.groupby('Date').count()['twp'].plot()
plt.tight_layout()

# create 3 separate plots with each plot representing a Reason for the 911 call
df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()

df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()

df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()


# Heatmap: restructure the dataframe so that columns become the Hours (x-axis) and the Index becomes the Day of the Week (y-axis)

dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()

plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')

sns.clustermap(dayHour,cmap='viridis')

# DataFrame that shows the Month as the column
dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()

plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')

sns.clustermap(dayMonth,cmap='viridis')
