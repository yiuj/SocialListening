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
#convert dataframe into percentage change data
        df = df.pct_change()

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    print(main_df.head())
    pickle_out = open('fiddy_states.pickle','wb')
    pickle.dump(main_df, pickle_out )
    pickle_out.close()



HPI_data = pd.read_pickle('fiddy_states.pickle')
#plot data
HPI_data.plot()
#remove legend
#data should be on same scale so shouldn't have problem plotting dataframe
plt.legend().remove()
plt.show()
#showing all data points for housing prices over time
#notice all of the data started in 2000 so the points converge
#can plot percent change from beginning to end to get better depiction of data
