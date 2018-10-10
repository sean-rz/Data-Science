import pandas as pd

ecom = pd.read_csv('Ecommerce Purchases')
print ecom.head()

#How many rows and columns are there
num_rows = len(ecom.index)
num_cols = len(ecom.columns)
print num_rows
print num_cols
print ecom.info()

#What is the average Purchase Price
print ecom['Purchase Price'].mean()

#What were the highest and lowest purchase prices
print ecom['Purchase Price'].max()
print ecom['Purchase Price'].min()

#How many people have English 'en' as their Language of choice
print sum(ecom['Language'] == 'en')
print ecom[ecom['Language'] == 'en'].count()

#How many people have the job title of "Lawyer"
print ecom[ecom['Job'] == 'Lawyer'].count()

#How many people made the purchase during the AM and how many people made the purchase during PM
print ecom['AM or PM'].value_counts()

#What are the 5 most common Job Titles
print ecom['Job'].value_counts().head(5)

#Someone made a purchase that came from Lot: "90 WT" 
#what was the Purchase Price for this transaction
print ecom[ecom['Lot'] == '90 WT']['Purchase Price'] 

#What is the email of the person with the following Credit Card Number: 4926535242672853 
print ecom[ecom["Credit Card"] == 4926535242672853]['Email'] 

#How many people have American Express as their Credit Card Provider 
#and made a purchase above $95
print ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()

#How many people have a credit card that expires in 2025
print sum(ecom['CC Exp Date'].apply(lambda exp: exp[3:] == '25'))

#What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) 
print ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5)


