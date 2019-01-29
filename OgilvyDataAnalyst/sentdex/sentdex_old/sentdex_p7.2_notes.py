#pickling
#save any python object. including list, dictionary, dataframe
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

    #pickle fiddy_states with the intention to write bytes
    pickle_out = open('fiddy_states.pickle','wb')
    #dump dataframe to pickle out file
    pickle.dump(main_df, pickle_out )
    #must close pickle because it was opened and written to
    pickle_out.close()

#grab_initial_state_data()
#pickling in. rb = reading bytes
pickle_in = open('fiddy_states.pickle','rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data)
#everything from pickleout is retained. Data comes in instantly.
#pandas as it's own pickle function
HPI_data.to_pickle('pickle.pickle')
HPI_data2 = pd.read_pickle('pickle.pickle')

print(HPI_data2)
