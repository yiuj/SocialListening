import pandas as pd

df = pd.read_csv('ZILLOW-C25709_ZRISFRR.csv')
print(df.head())

df.set_index('Date',inplace = True)
print(df.head())

#dataframe to new csv

df.to_csv('newcsv2.csv')
df = pd.read_csv('newcsv2.csv',index_col=0)

print(df.head())

#rename column. so far we have one column called 'Value'. Index = date (not a column)
df.columns = ['Houston_HPI']
print(df.head())

#save to csv files
df.to_csv('newcsv3.csv')
#want to remove headers in new csv file
df.to_csv('newcsv4.csv', header = False)
#want to add columns back to csv file. names = column names. set index to date
df = pd.read_csv('newcsv4.csv', names=['Date','Houston_HPI'],index_col=0)
print(df)

#convert to html
df.to_html('example.html')

#rename columns
df.rename(columns={'Houston_HPI':'8787'},inplace=True)
print(df.head())
