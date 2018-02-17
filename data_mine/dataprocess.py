from data_mine.preprocessing import preprocessing
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import model_selection
from sklearn.preprocessing import StandardScaler
z_scaler = StandardScaler()

process=preprocessing()
df=process.read_data_txt('kddcup.txt')
df=process.dropduplicates(df)
df.dropna(inplace=True)
df=process.cat_to_num(df)
df.reset_index(inplace=True)
X = np.array(df.drop(['type'],1))
Y=np.array(df['type'])
z_data = z_scaler.fit_transform(X)
prin_comp=PCA(n_components=6).fit_transform(z_data)
middf=pd.DataFrame(data=prin_comp,columns=['p1','p2','p3','p4','p5','p6'])
newdf=pd.concat([middf, df[['type']]], axis = 1)
print(newdf)
