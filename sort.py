import pandas as pd
import numpy as np


data = pd.read_table('input.txt',sep='\s+', engine='python')
data.head()


s = data['animal'].value_counts()
data = data.sort_values(by=['animal'])
data.head()
n = 0
notPrint = True
for i in range (0, len(s)):
    male = False
    female = False
    for j in range (0, s[i]):
        if(data.iloc[n]['gender'] == "male"):
            male = True
        if(data.iloc[n]['gender'] == "female"):
            female = True
        n += 1
    if(male and female):
        print(data.iloc[n-1]['animal'])
        notPrint = False
    
if(notPrint):
    print(0)
    


    n = 0
for i in range (0,len(s)):
    print(data.iloc[n]['animal'] , " - ", s[i])
    n += s[i]


    calls = pd.read_table('the_calls.txt',sep='\s+', engine='python')

calls.head()

calls = calls.sort_values(by=['person', 'sec'], ascending = [True, False] )
calls.head()


np.savetxt(r'calls.txt', calls.values, fmt='%s')