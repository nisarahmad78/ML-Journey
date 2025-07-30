from sklearn import datasets
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()
x = iris['data']
y = iris['target']

logic = LogisticRegression(max_iter=1000)
C = [0.25,0.50,0.75,1,1.25,1.50,1.75,2]
scores = []
for choice in C:
    logic.set_params(C = choice)
    logic.fit(x,y)
    scores.append(logic.score(x,y))
print(scores)
