import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import codecs

with codecs.open('DayAve.csv','r','shift-jis','ignore') as f:
    df=pd.read_csv(f,sep=',', skiprows=4)


#print(df)

df.sort_index()
print(df)

df.dropna(how='any', inplace=True)
df.drop(['品質情報','均質番号','品質情報.1','均質番号.1',
'品質情報.2','均質番号.2'],
axis=1, inplace=True)

print(df)
all_list=[]
date=[]
temp=[]
pres=[]
humi=[]
count=0


for i in df:
    all_list=df.values.flatten()

    date.append(i)
    temp.append(i)
    humi.append(i)
    #weat.append(i)
    pres.append(i)


#slice SAIKO!
date=all_list[::4]
temp=all_list[1::4]
humi=all_list[2::4]
pres=all_list[3::4]
#humi=all_list[4::5]

print(all_list)
print(date)
print(temp)


temp_date=[]
#temp_date=temp
#temp_date.append(date)
#temp_date=np.vstack([temp.T,date])

NUM=30
plt.plot(range(NUM),temp[0:NUM])
plt.ylabel("temp")
plt.xticks(range(NUM),date[0:NUM])
plt.show()