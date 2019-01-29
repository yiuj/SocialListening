#increase sampling or decrease sampling. increase or decrease granularity
#millisecond data resampled to 1 day
#^will take all the prices that day, all those milliseconds. add them together
#average them and give you the 1 day price based on those miliseconds
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


def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df['Value'] = (df['Value'] - df['Value'][0])/ df['Value'][0]*100
    return df


fig = plt.figure()

ax1 = plt.subplot2grid((1,1),(0,0))

HPI_data = pd.read_pickle('fiddy_states3.pickle')

#data is sampled once a month
#within resample. if you want to sample hourly, hit h. d = daily
#check pandas documentation 'timeseries offset aliases'

TX1yr = HPI_data['TX'].resample('A',how='mean')
print(TX1yr.head())
#A = resampling annually
#default for resample is to use the mean.

#plotting data with labels
HPI_data['TX'].plot(ax = ax1, label = 'Monthly TX HPI' )
TX1yr.plot(ax = ax1, label = 'Yearly TX HPI' )


plt.legend()
plt.show()
#looking at graph you see peaks at june and troughs during winter
#housing market = peak in june , cheapest in december 
#shows cycle especially when compared to annual data
