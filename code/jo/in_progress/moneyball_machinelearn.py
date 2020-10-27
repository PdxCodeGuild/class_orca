import pandas as pd
import numpy as np
from sklearn import linear_model

data = pd.read_csv('moneyballs_players_csv.csv')
# defines what data we look at
x = data[['AVG','HR','RBI','R','SB']]
y = data['Team W-L%']

# splits data to use 80% as training data and %20 as test data
training_data = data[:(int((len(data)*0.8)))]
test_data = data[(int((len(data)*0.8))):]

regr= linear_model.LinearRegression()

# sets some variable to to work in the regression model
train_x = np.array(data[['AVG', 'HR', 'RBI', 'R', 'SB']])
train_y = np.array(data['Team W-L%'])

test_x = np.array(data[['AVG', 'HR', 'RBI', 'R', 'SB']])
test_y = np.array(data['Team W-L%'])

regr.fit(train_x,train_y)

# prints the coefficient data with pandas:
coeff_data = pd.DataFrame(regr.coef_ , x.columns , columns=['coefficients'])
print(coeff_data)

# predicts data
y_pred = regr.predict(test_x)

# checks accuracy
from sklearn.metrics import r2_score
r = r2_score(test_y , y_pred)
print('r2 :',r)