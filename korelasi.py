import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

X = np.array([12,14,13,12,15,13,14,15,13,14])
Y = np.array([56,62,60,61,65,66,60,63,65,62])
corr = np.corrcoef(X, Y)

print('Kholifah Nur Maliki / 152017065')

print (corr)