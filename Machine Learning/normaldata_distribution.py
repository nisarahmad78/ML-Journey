#Normal Data Dist: In numpy probability thoery this kind of data 
# dist is known as normal data dist or Gaussian Distribution, where the value 
# are concentrated around a give value.
# a Example of noraml data dist:
import numpy as np
import matplotlib.pyplot as plt
shared = np.random.normal(5.0,1.0,100000)
plt.hist(shared,100)
plt.show()



