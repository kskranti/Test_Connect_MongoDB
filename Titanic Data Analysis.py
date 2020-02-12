import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn as sns
#import sklearn.cross_validation

titanic_data = pd.read_csv(r'C:\Users\krasingh\Training\Data Science\titanic\train.csv')
pas_survive = titanic_data.Survived == True


#np.count_nonzero[pas_survive]

#print(titanic_data.count())

#print ("# of passengers in original data " + str(len(titanic_data)))

#print(titanic_data(["Survived"])==0).count()

##Aanalyzing data

#sns.countplot(x="Survived", data=titanic_data)
#plt.show()

#sns.countplot(x="Survived", hue="Sex",data=titanic_data)
#plt.show()

#sns.countplot(x="Survived", hue="Pclass",data=titanic_data)
#plt.show()

print(titanic_data.info())
titanic_data["Age"].plot.hist()
#titanic_data["Fare"].plot.hist(bin=20, figsize=(10,5))
plt.show()

print(titanic_data.isnull().sum())

sns.heatmap(titanic_data.isnull(),yticklabels=False)
plt.show()

sns.boxplot(x="Pclass", y="Age", data=titanic_data)
plt.show()
#survived_1 = titanic_data(["Survived"]=="1").values


titanic_data.drop(["Sex"], axis=1, inplace=True)
#titanic_data.count(titanic_data(["survived"] == 1))
