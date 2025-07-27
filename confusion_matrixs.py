# import numpy as np
# from sklearn.metrics import ConfusionMatrixDisplay
# from sklearn.metrics import confusion_matrix
# import matplotlib.pyplot as plt
# actual_data = np.random.binomial(3,.9,1000)
# prediction = np.random.binomial(3,.9,1000)
# model = confusion_matrix(actual_data,prediction)
# display_prediction = ConfusionMatrixDisplay(confusion_matrix=model, display_labels=[False,True])
# display_prediction.plot()
# plt.show()

import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt

# Generate binary data: values will be either 0 (False) or 1 (True)
actual_data = np.random.binomial(1, .9, 1000)       # 90% True (1), 10% False (0)
prediction = np.random.binomial(1, .9, 1000)

# Compute confusion matrix with binary labels
cm = confusion_matrix(actual_data, prediction, labels=[0, 1])

# Display the confusion matrix using True/False labels
display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[False, True])
display.plot()
plt.title("Confusion Matrix (True/False)")
plt.show()





import matplotlib.pyplot as plt
from sklearn import metrics
actual_data = np.random.binomial(1, .9, size=1000)       # 90% True (1), 10% False (0)
prediction = np.random.binomial(1, .9, size=1000)
cm = metrics.confusion_matrix(actual_data, prediction)
display = metrics.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[False, True])
display.plot()
plt.title("Confusion Matrix (True/False)")
plt.show()


