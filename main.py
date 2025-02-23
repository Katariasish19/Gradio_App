import numpy as np
import pandas as pd

#dict1 = {
  #  "name":['harry','rohan','skillf','shubham'],
  #  "marks":[92,34,24,67],
  #  "city":['rampur','kolkata','bareilly','artarctica']
#}

#df = pd.DataFrame(dict1)
#print(df)

#df.to_csv('friends.csv',index = False)



#data = [['bellingham',20],['haland',24],['grevanche',21]]

#df1 = pd.DataFrame(data, columns=['Name','Age'])
#print(df1)


#df2 = pd.read_csv('test.csv')
#print(df2.head(4))
#print(df2.tail(4))
#df2_xlsx = pd.read_excel('test.xlsx')('test.text',delimiter = '\t')
#print(df2_xlsx)


#df3 = pd.read_csv('Pokemon.csv')
#print(df3)
#print(df3.columns)

#print(df.iloc[1:4]) 



dates_list = ['2023-10-01','2023-11-01','2023-12-01','2023-10-01']

date_series = pd.to_datetime(dates_list)

df = pd.DataFrame({ 'datetime_column': date_series})

df['year'] = df['datetime_column'].apply(lambda x: x.year)
df['month'] = df['datetime_column'].apply(lambda x: x.month)
df['day'] = df['datetime_column'].apply(lambda x: x.day)

print(df)
print(df.dtypes)


new_dates ={'date': ['2023-10-01','2023-11-01','2023-12-01','2023-10-01']}

df1 = pd.DataFrame(new_dates)

df1['year'] = df1['date'].str[:4]
df1['month'] = df1['date'].str[5:7]
df1['day'] = df1['date'].str[8:]

print(df1[['year','month','day']])
print(df1.dtypes)