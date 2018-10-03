import numpy as np
import pandas as pd


# pip install sqlalchemy
# pip install lxml
# pip install html5lib
# pip install BeautifulSoup4
# pip install xlrd
# pip install openpyxl

# CSV files
df = pd.read_csv('example')
print df

df.to_csv('example2.csv',index=False)

# Excel files
df = pd.read_excel('Excel_Sample.xlsx',sheetname='Sheet1')
print df

df.to_excel('Excel_Sample2.xlsx',sheet_name='Sheet1')

# HTML Input
data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
print data[0]

# SQL
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
df.to_sql('my_table',engine)  # Write records stored in a DataFrame to a SQL database
sql_df = pd.read_sql('my_table',con=engine)  # Read SQL query or database table into a DataFrame
print sql_df