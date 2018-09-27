import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.stats import pearsonr
df = pd.read_csv('train.csv')
numerics = ['int16','int32','int64','float16','float32','float64']
df2 = df.select_dtypes(numerics)
df3 = df2.describe().T
df4 = df3.sort_values(by='std')
df4.index
x = df2.SalePrice
y1 = df2.LotArea
y2 = df2.GrLivArea
y3 = df2.MiscVal
y4 = df2.BsmtFinSF1
y5 = df2.BsmtUnfSF
y6 = df2.TotalBsmtSF
plt.scatter(x,y1)
scipy.stats.pearsonr(x,y1)
