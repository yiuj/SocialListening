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

#with % change
#generate data
fig = plt.figure()
#creating a grid. grid will be 1 x 1, starting at 0,0. grid of subplots
ax1 = plt.subplot2grid((1,1),(0,0))

HPI_data = pd.read_pickle('fiddy_states3.pickle')
benchmark = HPI_Benchmark()

#plotting data. ploting ax1 data on axis 1
HPI_data.plot(ax = ax1 )
#color k = black . big benchmark linewidth
benchmark.plot(ax=ax1, color='k',linewidth = 10)
plt.legend().remove()
plt.show()
