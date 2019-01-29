import quandl
import pandas as pd


api_key = quandl.ApiConfig.api_key = 'thPwHsfxExE-sEDVhmPj'

df = quandl.get('FMAC/HPI_TX',authtoken = api_key)
print(df.head())
#print(df)

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')


#this is a list
#print(fiddy_states)

#this is a dataframe
print(fiddy_states[0])

#this is a column
print(fiddy_states[0][1])

for abv in fiddy_states[0][1][1:]:
    print('FMAC/HPI_'+str(abv))
