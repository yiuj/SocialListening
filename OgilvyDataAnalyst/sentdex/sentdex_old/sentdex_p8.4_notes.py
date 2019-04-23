#correlate all data with each other
#create a correlation table
import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = quandl.ApiConfig.api_key = 'thPwHsfxExE-sEDVhmPj'

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][1][1:]

def grab_initial_state_data():

    states = state_list()

    main_df = pd.DataFrame()

    for abv in states:
        query = 'FMAC/HPI_'+str(abv)
        df = quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value':str(abv)}, inplace=True)
#convert dataframe into percentage change data starting at starting value
        df[abv] = (df[abv] - df[abv][0])/ df[abv][0]*100
        #every dataframe has a column for a state's dataframe
        #calculate percent change: new - old / old

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    print(main_df.head())
    pickle_out = open('fiddy_states3.pickle','wb')
    pickle.dump(main_df, pickle_out )
    pickle_out.close()

#going to figure out aggregate of U.S. housing index
def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df['Value'] = (df['Value'] - df['Value'][0])/ df['Value'][0]*100
    return df

HPI_data = pd.read_pickle('fiddy_states3.pickle')

#correlate all data with each other
#create a correlation table
HPI_State_Correlation = HPI_data.corr()
#generating a correlation table for all columns
print(HPI_State_Correlation)
#more information. for every column how many rows, avg, std, lowest, 25th quartile
#min is very important. shows the least correlated row with each state 
print(HPI_State_Correlation.describe())
