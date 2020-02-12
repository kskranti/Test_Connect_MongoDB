import statistics as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(st.mean([10,12,24,17,18]))
print(st.median([10,12,24,17,18]))
print(st.mode([10,12,24,12,17,18]))
plt.rcParams['figure.figsize'] = (20.0, 10.0)

data = pd.read_csv(r"C:\Users\krasingh\Downloads\headbrain\headbrain.csv")
print(data.shape)
print(data.head())

#collecting X & Y

X=data['Head Size(cm^3)'].values
Y=data['Brain Weight(grams)'].values


#Now calculate y = mx + c Or coefficient b1 & b0(c & m)
#Mean of X & Y

#Mean_x = st.mean(x)
#Mean_y = st.mean(y)

mean_x =np.mean(X)
mean_y = np.mean(Y)

#Total number of values

m = len(X)

#using the formula to calculate b1 & b2
numer = 0
denom = 0
#Calculate b1(c)

for i in range(m):
    numer +=(X[i] - mean_x) * (Y[i] - mean_y)

print(numer)


#Calculate denom

for i in range(m):
    denom += (X[i] - mean_x) **2

print(denom)

#print coefficient b1(c)

b1 = numer/denom

print(b1)


#print coefficient b0(c)

b0 = mean_y - (b1 * mean_x)
print (b0)

#henc we can say that value of m is .26 & value of c is 325.57

#plotting values & regression line y = mx + c

max_x = np.max(X) + 100
min_x = np.min(X) -100

#calculating line values x & y

#calculating line values x & y
x= np.linspace(min_x,max_x,1000)
y = b0 + b1*x

#Plotting line

plt.plot(x,y, color = 'red', label = 'regression line')


#plotting scatter points
plt.scatter(X,Y, color='green', label='scatter plot')

plt.xlabel('head size in cm3')
plt.ylabel('Brain weight in gms')

plt.legend()
plt.show()

