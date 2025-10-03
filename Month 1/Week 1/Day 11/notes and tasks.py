# Day 11 — Introduction to scikit-learn
# Today you'll learn basic supervised learning with scikit-learn: creating a synthetic regression dataset, train/test split, training a Linear Regression model, evaluation metrics, cross-validation, and a simple pipeline.

# Run each cell (select + Shift+Enter).

# Objectives
# Create a synthetic regression dataset with make_regression
# Split into train/test sets
# Train a LinearRegression model
# Evaluate using MAE, MSE, RMSE, and R²
# Use Pipeline with StandardScaler and LinearRegression
# Run cross-validation and inspect 

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print('Libraries imported')



# Create dataset
X, y = make_regression(n_samples=200, n_features=3, noise=10.0, random_state=42)
print('X shape:', X.shape)
print('y shape:', y.shape)

# Quick scatter of first feature vs target
plt.figure()
plt.scatter
plt.title('Feature 0 vs Target')
plt.xlabel('Feature 0')
plt.ylabel('Target')
plt.show()


# Train / Train
# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print('Train size:', X_train.shape[0])
print('Test size:', X_test.shape[0])

# Train Linear Regression (no scalling)
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'MAE: {mae:.3f}')
print(f'MSE: {mse:.3f}')
print(f'RMSE: {rmse:.3f}')
print(f'R2: {r2:.3f}')


# Scatter actual vs Predicted
plt.figure()
plt.scatter(y_test, y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()])
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.show()


# Pipeline with StandardScaler + LinearRegression
# pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('lr', LinearRegression())
])

pipe.fit(X_train, y_train)

y_pred_pipe = pipe.predict(X_test)

mae_p = mean_absolute_error(y_test, y_pred_pipe)
mse_p = mean_squared_error(y_test, y_pred)
rmse_p = np.sqrt(mse_p)
r2_p = r2_score(y_test, y_pred_pipe)

print(f'pipeline MAE: {mae_p:.3f}')
print(f'Pipeline RMSE: {rmse_p:.3f}')
print(f'Pipeline R2: {r2_p:.3f}')


# Cross-validation (negative MSE is returned by scikit-learn for scoring='neg_mean_squared_error')
cv_scores = cross_val_score(pipe, X, y, cv=5, scoring='neg_mean_squared_error')
cv_mse = -cv_scores
cv_rmse = np.sqrt(cv_mse)
print('CV MSE:', np.round(cv_mse, 3))
print('CV RMSE:', np.round(cv_rmse, 3))
print('Mean CV RMSE:', np.round(np.mean(cv_rmse), 3))

# Inspect model coefficients
# Fit linear model on full training set (with scaler) and inspect coefficients
pipe.fit(X_train, y_train)
coefs = pipe.named_steps['lr'].coef_
intercept = pipe.named_steps['lr'].intercept_
print('Intercept:', intercept)
print('Coefficients:', coefs)
