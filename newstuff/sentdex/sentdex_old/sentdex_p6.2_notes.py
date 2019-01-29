import pandas as pd

#df 5 skips year 2002 and adds 2005
df1 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df3 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})

#df 1 = left, df 2 = right. how means which df data you are merging on
#merge on left
merged = pd.merge(df1,df3, on='Year',how='left')
merged.set_index('Year', inplace = True)
print(merged)

df1 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df3 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})
#merge on right
merged = pd.merge(df1,df3, on='Year',how='right')
merged.set_index('Year', inplace = True)
print(merged)

df1 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df3 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})

#outer and inner
#outer joins on union of keys
merged = pd.merge(df1,df3, on='Year',how='outer')
merged.set_index('Year', inplace = True)
print(merged)


df1 = pd.DataFrame({
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55],
                    'Year':[2001, 2002, 2003, 2004]
                    })

df3 = pd.DataFrame({
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53],
                    'Year':[2001, 2003, 2004, 2005]})

#inner is where keys intersect
merged = pd.merge(df1,df3, on='Year',how='inner')
merged.set_index('Year', inplace = True)
print(merged)
#probably want to merge on sharing a column. merge when index doesn't matter
#use join to merge on sharing an index. join when index does matter  
