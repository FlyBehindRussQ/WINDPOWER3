from statsmodels.tsa.seasonal import STL
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

######################################################################
# STL分解
plt.rc("figure", figsize=(10, 6))
 
df=pd.read_csv("10yuan_data.csv")
 
res = STL(df['power'], period=24*6*30).fit()  #period确定：10分钟一个数据，以天为周期就是24*6
res.plot()
 
df['trend']=res.trend
df['seasonal']=res.seasonal
df['resid']=res.resid

# 将分解后的数据保存为csv文件，并命名第一列为'Time'
df.to_csv('stl_decomposition.csv')

# plt.show()

trend_strength=max(0,1-df.resid.var()/df.seasonal.var())
seasonal_strength=max(0,1-df.resid.var()/df.trend.var())
print('trend_strength:',trend_strength)
print('seasonal_strength:',seasonal_strength)

print('residual mean:',df.resid.mean())
df.resid.hist()
