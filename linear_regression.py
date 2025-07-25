import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
X = [6,8,10,12,14,18,20]
Y = [300,700,1200,1600,2200,2700,3500]
Slope, intercept , r, p , std_error = stats.linregress(X,Y)
# def slopes(x):
#     return Slope*x +intercept
# model = list(map(slopes,X ))
# plt.scatter(X,Y)
# plt.plot(X,model)
# plt.show()
print(r)