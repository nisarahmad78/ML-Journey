import pandas as pd
from sklearn import linear_model

df = pd.read_csv('cars.csv')
car_valume = df[['Volume','Weight']]
car_co2 = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(car_valume,car_co2)

predict = regr.predict([[2300,1300]])
print(f"Preditct: {predict[0]}")
