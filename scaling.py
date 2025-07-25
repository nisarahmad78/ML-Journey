import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Load the dataset
df = pd.read_csv("cars2.csv")

# Select features and target variable
# Assumes 'Volume' is in cc and 'Weight' is in kg
X = df[['Weight', 'Volume']]
y = df['CO2']

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_scaled, y)

# New input for prediction
# Replace with appropriate values as per your data (e.g., 2300cc, 1300kg)
new_data = [[2300, 1300]]  # Volume in cc, Weight in kg
new_data_scaled = scaler.transform(new_data)

# Predict CO2 emission
predicted_CO2 = model.predict(new_data_scaled)
print(f"Predicted CO2 emission: {predicted_CO2[0]:.2f} g/km")
