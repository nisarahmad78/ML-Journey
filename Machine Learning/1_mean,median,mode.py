import numpy as np
from scipy import stats
speed = [59,20,30,40,50,20,30,55,77,88,10,91,19,80,99,98]
mean_result =np.mean(speed)
median_result = np.median(speed)
mode_result = stats.mode(speed)
print(f'Mean: {mean_result},Median: {median_result}, Mode: {mode_result[0]}')

