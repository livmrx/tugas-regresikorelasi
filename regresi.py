#library-library yang dibutuhkan
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

#data untuk variable X untuk Kolom X dan Y untuk kolom Y
X = np.array([12,14,13,12,15,13,14,15,13,14])
Y = np.array([56,62,60,61,65,66,60,63,65,62])
X = X.reshape(-1, 1)
Y = Y.reshape(-1, 1)

#Create linear regression object
model_reg = LinearRegression()

#train the model using the training sets
model_reg.fit(X, Y)

print('Kholifah Nur Maliki / 152017065')

print('Panjang X = {}'.format(len(X)))
print('Panjang Y = {}'.format(len(Y)))

#regression coefficients
print('Koefisien = {}'.format(model_reg.coef_))
print('Konstanta ={} '.format(model_reg.intercept_))