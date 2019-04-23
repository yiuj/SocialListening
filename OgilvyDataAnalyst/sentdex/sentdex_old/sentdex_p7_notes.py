import quandl
import pandas as pd

api_key = quandl.ApiConfig.api_key = 'thPwHsfxExE-sEDVhmPj'


#how do I implement my api key??

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

main_df = pd.DataFrame()

for abv in fiddy_states[0][1][1:]:
    query = 'FMAC/HPI_'+str(abv)
    df = quandl.get(query, authtoken=api_key)
    df.rename(columns={'Value':str(abv)}, inplace=True)

    if main_df.empty:
        main_df = df
    else:
        main_df = main_df.join(df)
print(main_df)




#going to join dataframes because shared index
