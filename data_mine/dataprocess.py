from data_mine.processing import processing
import pandas as pd
import numpy as np
from sklearn import model_selection


process=processing()
df=process.read_data_txt('../resources/data_set/kddcup.txt')
df=process.dropduplicates(df)
df.dropna(inplace=True)
df=process.cat_to_num(df)
df.reset_index(inplace=True)

X = np.array(df.drop(['type'],1))
Y=np.array(df['type'])

prin_comp=process.scale_and_pca(X)

middf=pd.DataFrame(data=prin_comp,columns=['p1','p2','p3','p4','p5','p6'])
newdf=pd.concat([middf, df[['type']]], axis = 1)
print(newdf)
