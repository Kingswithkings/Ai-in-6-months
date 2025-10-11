# Imports
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn import datasets
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
from scipy.stats import expon
import seaborn as sns

print('Libraries imported')

# Load dataset and split
iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print('Train size:', X_train.shape[0], 'Test size:', X_test.shape[0])

# Exercise 1: Enhanced RF GridSearch with max_features
pipe_rf = Pipeline([
    ('scaler', StandardScaler()),
    ('rf', RandomForestClassifier(random_state=42))
])

# Added max_features to the grid as requested in exercises
param_grid_rf = {
    'rf__n_estimators': [50, 100, 200],
    'rf__max_depth': [None, 5, 10],
    'rf__min_samples_split': [2, 5],
    'rf__max_features': ['sqrt', 'log2', None]  # Exercise completed: added max_features
}

# Exercise 2: Use StratifiedKFold (good practice even for balanced datasetsa)
cv_strategy = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)


# Exercise 3: Time the GridSearch
start_time = time.time()
gs_rf = GridSearchCV(pipe_rf, param_grid_rf, cv=cv_strategy, scoring='accuracy', n_jobs=-1)
gs_rf.fit(X_train, y_train)
grid_time = time.time() - start_time

print('Best RF params:', gs_rf.best_params_)
print('Best RF CV score:', gs_rf.best_score_)
print(f'GridSearch time: {grid_time:.2f} seconds')

# Evaluate RF on the test set
best_rf = gs_rf.best_estimator_
y_pred_rf = best_rf.predict(X_test)
print('Test Accuracy (RF):', accuracy_score(y_test, y_pred_rf))
print('\nClassification Report (RF):\n', classification_report(y_test, y_pred_rf, target_names=iris.target_names))

# Exercise Extension: SVM with RandomSearchCV

# SVM Pipeline
pipe_svm = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(random_state=42))
])

# Parameter distribution for RandomSearchCV
# Using expon (expontial distribution) for C and gamma as in your imports 
param_dist_svm = {
    'svm__C': expon(scale=10),          # Continious distribution: more samples near 0-20
    'svm__gamma': expon(scale=1),       # Same for gamma
    'svm__kernel': ['rbf', 'poly']
}

# Time RandonmizedSearchCV
start_time = time.time()
rs_svm = RandomizedSearchCV(
    pipe_svm,
    param_dist_svm, 
    n_iter=20, # Test 20 random combinations
    cv=cv_strategy,
    scoring='accuracy',
    n_jobs=-1,
    random_state=42
)

rs_svm.fit(X_train, y_train)
rand_time = time.time() - start_time

print('\n' + '='*50)
print('SVM with RandomizedSearchCV')
print('='*50)
print('Best SVM params:', rs_svm.best_params_)
print('Best SVM CV score', rs_svm.best_score_)
print(f'RandomizedSearch time: {rand_time:.2f} seconds')

# Evaluate SVM on test set
y_pred_svm = rs_svm.best_estimator_.predict(X_test)
print('Test Accuracy (SVM):', accuracy_score(y_test, y_pred_svm))
print('n\Classification Report (SVM):\n', classification_report(y_test, y_pred_svm, target_names=iris.target_names))


# Final comparison
print('\n' + '='*50)
print('FINAL COMPARISON')
print('='*50)
print(f"Random Forest Test Accuracy: {accuracy_score(y_test, y_pred_rf):.4f} (GridSearch: {grid_time:.2f}s)")
print(f"SVM Test Accuracy:           {accuracy_score(y_test, y_pred_svm):.4f} (RandomizedSearch: {rand_time:.2f}s)")