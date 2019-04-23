import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])
#df 1 & df 2 share same columns but have different indexes
concat = pd.concat([df1,df2])

print(concat)

#adding df3. df3 has an extra column 'low_tier_hpi' and no 'us_gdp_thousands'
#also have two 2001's
concat = pd.concat([df1,df2,df3])

print(concat)

#try append
df4 = df1.append(df2)
print(df4)
#but pandas is meant for pure data manipulation
