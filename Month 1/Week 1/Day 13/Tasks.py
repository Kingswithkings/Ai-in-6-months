# Imports
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score

print('Libraries imported')


# Load dataset and split
# Load iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print('Train size', X_train.shape[0], 'Test size:', X_test.shape[0])


# Pipeline + GridSearch for RandomForest
pipe_rf = Pipeline([
    ('scaler', StandardScaler()),
    ('rf', RandomForestClassifier(random_state=42))
])

param_grid_rf = {
    'rf__n_estimators': [50, 100, 200],
    'rf__max_depth': [None, 5, 10],
    'rf__min_samples_split': [2, 5]
}

gs_rf = GridSearchCV(pipe_rf, param_grid_rf, cv=5, scoring='accuracy', n_jobs=-1)
gs_rf.fit(X_train, y_train)

print('Best RF params:', gs_rf.best_params_)
print('Best RF CV score:', gs_rf.best_score_)


# Evaluate on test set
best_rf = gs_rf.best_estimator_
y_pred_rf = best_rf.predict(X_test)
print('Test Accuracy (RF):', accuracy_score(y_test, y_pred_rf))
print('n\Classification Report (RF):\n', classification_report(y_test, y_pred_rf, target_names=iris.target_names))

# 3. RandomizedSearchCV - SVC (example for larger search space)
# Pipeline + RandomSearch for SVC
pipe_svc = Pipeline([
    ('scaler', StandardScaler()),
    ('svc', SVC(random_state=42))
])

from scipy.stats import expon, randint

param_dist_svc = {
    'svc__C': expon(scale=1.0), # continious distribution
    'svc__gamma': expon(scale=0.1),
    'svc__kernel': ['rbf', 'poly']
}

rs_svc = RandomizedSearchCV(pipe_svc, param_dist_svc, n_iter=20, cv=5, scoring='accuracy', n_jobs=-1, random_state=42)
rs_svc .fit(X_train, y_train)

print('Best RF params:', gs_rf.best_params_)
print('Best RF CV score:', gs_rf.best_score_)

# Evaluate on test set
best_rf = gs_rf.best_estimator_
y_pred_rf = best_rf.predict(X_test)
print('Test Accuracy (RF):', accuracy_score(y_test, y_pred_rf))
print('\nClassification Report (RF):\n', classification_report(y_test, y_pred_rf, target_names=iris.target_names))

# 4. Inspect and Evaluate

# Convert_results_ to DataFrame and show top rows
cv_rf = pd.DataFrame(gs_rf.cv_results_)
cols = ['params', 'mean_test_score', 'std_test_score', 'rank_test_score']
print(cv_rf[cols].sort_values('rank_test_score').head(10))

# 5. Visualise GridSearch results - heatmap for n_estimators vs max_depth
# Create pivot table for heatmap
pv = cv_rf.copy()
pv['n_estimators'] = pv['params'].apply(lambda p: p['rf__n_estimators'])
pv['max_depth'] = pv['params'].apply(lambda p: -1 if p['rf__max_depth'] is None else p['rf__max_depth'])

heat = pv.pivot_table(values='mean_test_score', index='n_estimators', columns='max_depth')

plt.figure(figsize=(6,4))
import seaborn as sns
sns.heatmap(heat, annot=True, fmt='.3f', cmap='viridis')
plt.title('GridSearch RF mean_test_score')
plt.show()