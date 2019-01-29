#handling missing data NAN
#can ignore missing data
#can delete missing data
#can fill in missing data. take previous or future data point and fill
#can replace NAN with a static number

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


fig = plt.figure()

ax1 = plt.subplot2grid((1,1),(0,0))

HPI_data = pd.read_pickle('fiddy_states3.pickle')

#adding to dataframe

HPI_data['TX1yr'] = HPI_data['TX'].resample('A',how='mean')
#TX1yr is not showing any data (NAN) bc not enough data points
#want to delete this data
#drop NAN
#must use inplace = True
HPI_data.dropna(inplace=True)
print(HPI_data[['TX','TX1yr']].head())
# if you want to drop a row with all NAN:
HPI_data.dropna(how='all',inplace=True)

#option to fill NAN
#method can be forward fill(ffill) or backward fill
#forward fill = sweeping forward. taking previous values and filling in forward

HPI_data.fillna(method='ffill'inplace=True)
#can also fill NA with a value
#can also set a limit to how much you want to fill
HPI_data.fillna(value=-99999,inplace=True,limit=100)

HPI_data[['TX','TX1yr']].plot(ax = ax1)

plt.legend()
plt.show()
#now TX1yr shows data by dropping NAN
