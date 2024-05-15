import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the csv file
nyc = pd.read_csv(r'C:\Users\Valeria\Documents\Advanced Pyhton\Homework 10\ave_yearly_temp_nyc_1895-2017.csv')

# Rename the value column to Temperature
nyc.columns = ['Date', 'Temperature', 'Anomaly']

nyc.Date = nyc.Date.floordiv(100)
print(nyc.head(3))

# Splitting the data for training and testing
X_train, X_test, y_train, y_test = train_test_split(nyc.Date.values.reshape(-1,1), nyc.Temperature.values, random_state=11)

print(X_train.shape)
print(X_test.shape)

# Training the model
linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)

linear_regression.coef_
linear_regression.intercept_

# Testing the model
predicted = linear_regression.predict(X_test)
expected = y_test

for p, e in zip(predicted[::5], expected[::5]):
    print(f'predicted: {p:.2f}, expected: {e:.2f}')

# Predicting future temperatures and estimating past temperatures
predict = (lambda x: linear_regression.coef_ * x + linear_regression.intercept_)
predict(2019)
predict(1890)

# Visializing the dataset with the regression line
axes = sns.scatterplot(data=nyc, x = 'Date', y = 'Temperature', hue = 'Temperature', palette = 'winter', legend = False)

axes.set_ylim(10, 70)

x = np.array([min(nyc.Date.values), max(nyc.Date.values)])
y = predict(x)

line = plt.plot(x,y)
plt.show()
