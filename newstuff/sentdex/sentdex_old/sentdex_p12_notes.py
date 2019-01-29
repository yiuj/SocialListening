#applying comparison operators to dataframe
#operators to redefine dataframe or generate a new one
#operators = >,<,=,extracts
#can also handle erroneous data. 100% certain it is erroneous
#example if stock price was $0
import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}
#6212 data point is clearly bad data

#how do you automatically detect erroneous data
# use Standard Deviation
df = pd.DataFrame(bridge_height)
#calculate standard deviation
df['STD']= df['meters'].rolling(2).std()
print(df)
#can see visually STD is too big. Want to decide beforehand.
#if STD >x, get rid of that point x
#want to describe meters and STD
df_std = df.describe()['meters']['std']
print(df_std)
#so average standard devation for entire data set = 2000, 1/3 of max std
#exact value for meters and std is 2067

#now can redefine the dataframe
#where the df is less than df_std. df_std = 2067
#this selects only columns that meet certain criteria
df = df[ (df['STD'] < df_std) ]
print(df)

df['STD'].plot()
df.plot()
plt.show()
