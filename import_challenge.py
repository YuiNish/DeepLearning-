import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import codecs

#csvファイル内に文字が含まれるとエラーが発生→'utf-8' codec can't decode byte 0x95 in position 0: invalid start byte
#codecsを使ってエラー回避
with codecs.open('DayAve.csv','r','shift-jis','ignore') as f:
    df=pd.read_csv(f,sep=',', skiprows=4)


#print(df)

df.sort_index()
print(df)

df.dropna(how='any', inplace=True)
df.drop(['品質情報','均質番号','品質情報.1','均質番号.1',
'品質情報.2','均質番号.2'],
axis=1, inplace=True)
#axis=0:列方向、axis=1:行方向
#ここでは行方向に一致する要素(ラベル)を指定することでそこの部分の列を落とす

print(df)
