#create a correlation table
import quandl
import pandas as pd
import pickle


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

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    print(main_df.head())
    pickle_out = open('fiddy_states.pickle','wb')
    pickle.dump(main_df, pickle_out )
    pickle_out.close()

HPI_data = pd.read_pickle('pickle.pickle')

#change column or add column TX2. also multiply data in column by 2
HPI_data['TX2']=HPI_data['TX']*2
print(HPI_data[['TX','TX2']])
