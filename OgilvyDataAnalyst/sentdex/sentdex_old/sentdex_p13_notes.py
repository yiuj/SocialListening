#joining in new data: 30 year mortgage rate
#feed data into machine learning algorithm

import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = quandl.ApiConfig.api_key = 'thPwHsfxExE-sEDVhmPj'

#starts a little bit prior. so trim start
def mortgage_30yr():
    df = quandl.get("FMAC/MORTG",trim_start="1975-01-01", authtoken = api_key)
    df['Value'] = (df['Value'] - df['Value'][0])/ df['Value'][0]*100
#resample data so that it starts at end of monthself.
#resample to the month (M)
    df = df.resample('M').mean()
    df.columns
    return df

print(df)
#issue that table column = value
#issue that data is sampled at beginning of month
#all other data is sampled at end of month

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

        df[abv] = (df[abv] - df[abv][0])/ df[abv][0]*100

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    print(main_df.head())
    pickle_out = open('fiddy_states3.pickle','wb')
    pickle.dump(main_df, pickle_out )
    pickle_out.close()


def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df['Value'] = (df['Value'] - df['Value'][0])/ df['Value'][0]*100
    return df

m30 = mortgage_30yr()

HPI_data = pd.read_pickle('fiddy_states3.pickle')
#you see that data is collected at end of the month
HPI_bench = HPI_Benchmark()
