#rolling correlation
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

#figure
fig = plt.figure()
#sublots / axes
ax1 = plt.subplot2grid((2,1),(0,0))
#create a new axes for STD
ax2 = plt.subplot2grid((2,1),(1,0), sharex=ax1)
#2 x 1. 2 tall 1 wide. next axes starting at 1,0
#share x axis of axis 1

HPI_data = pd.read_pickle('fiddy_states3.pickle')

#measure correlation between texas and alaska
#calculate correlation
TX_AK_12corr = HPI_data['TX'].rolling(window=12).corr(HPI_data['AK'])

#plotting Texas and Alaska HPI on graph axis = 1
HPI_data['TX'].plot(ax=ax1,label='TX HPI')
HPI_data['AK'].plot(ax=ax1,label='AK HPI')
ax1.legend()
#plotting correlation on graph axis = 2
TX_AK_12corr.plot(ax = ax2, label='TX_AK_12corr')
#HPI_data['TX12MA']=HPI_data['TX'].rolling(12).mean()

plt.legend()
plt.show()
