import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

web_stats = {'Day': [1,2,3,4,5,6],
            'Visitors': [43,53,43,56,67,90],
            'Bounce_Rate': [65,56,34,45,67,78]}
df = pd.DataFrame(web_stats)
#set index to day
#df.set_index('Day')
#but this is just a copy. doesn't really change df
#df = df.set_index('Day')
#works but sloppy
df.set_index('Day', inplace = True)

print(df.head(2))
#print just column Visitors
print(df['Visitors'])
#Also object oriented. Visitors as attribute
print(df.Visitors)

#print two columns. list inside a reference
print(df[['Visitors','Bounce_Rate']])

#convert to visitors list
print(df.Visitors.tolist())
#convert visitors and bounce rate to array. must use numpy to convert to array
print(np.array(df[['Visitors','Bounce_Rate']]))
#print above array as a pandas dataframe

df2 = pd.DataFrame(np.array(df[['Visitors','Bounce_Rate']]))
print(df2)
