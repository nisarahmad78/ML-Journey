import numpy as np
import matplotlib.pylab as plt
from scipy.cluster.hierarchy import linkage,dendrogram
x = [4,5,10,4,3,11,14,6,10,12]
y = [21,19,24,17,16,25,24,22,21,21]

data = list(zip(x,y))
linked_data = linkage(data,method='ward',metric='euclidean')
dendrogram(linked_data)
plt.show()


## same this we can do using the scikit-learn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
data = list(zip(x,y))
print(data)
hierarchy_clustering =AgglomerativeClustering(n_clusters=2,linkage='ward')
label = hierarchy_clustering.fit_predict(data)
plt.scatter(x,y,c=label,cmap='viridis')
plt.show()















