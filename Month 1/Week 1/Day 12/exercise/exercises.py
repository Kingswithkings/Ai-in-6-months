
### ✅ Solution:
### ✅ Fixed Code (without `seaborn`):

### ✅ Workaround Strategy:
# File: iris_comparison.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Load data
iris = datasets.load_iris()
X_full = iris.data
X_2d = X_full[:, :2]
y = iris.target

# Split consistently
X_train_full, X_test_full, y_train, y_test = train_test_split(
    X_full, y, test_size=0.25, random_state=42, stratify=y
)
X_train_2d, X_test_2d, _, _ = train_test_split(
    X_2d, y, test_size=0.25, random_state=42, stratify=y
)

# 1. Test k values (2D)
print("=== k-NN with different k (2 features) ===")
k_vals = [1, 3, 5, 7, 9]
for k in k_vals:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_2d, y_train)
    acc = accuracy_score(y_test, knn.predict(X_test_2d))
    print(f"k={k}: {acc:.4f}")

# 2. Full features (no scaling)
print("\n=== Full features (no scaling) ===")
lr = LogisticRegression(max_iter=200).fit(X_train_full, y_train)
knn5 = KNeighborsClassifier(n_neighbors=5).fit(X_train_full, y_train)
print(f"Logistic Regression: {accuracy_score(y_test, lr.predict(X_test_full)):.4f}")
print(f"k-NN (k=5):          {accuracy_score(y_test, knn5.predict(X_test_full)):.4f}")

# 3. With scaling
print("\n=== With StandardScaler ===")
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train_full)
X_test_s = scaler.transform(X_test_full)

lr_s = LogisticRegression(max_iter=200).fit(X_train_s, y_train)
knn_s = KNeighborsClassifier(n_neighbors=5).fit(X_train_s, y_train)
print(f"Logistic Regression (scaled): {accuracy_score(y_test, lr_s.predict(X_test_s)):.4f}")
print(f"k-NN (k=5, scaled):          {accuracy_score(y_test, knn_s.predict(X_test_s)):.4f}")

# Find best k
best_k, best_acc = 1, 0
for k in range(1, 21):
    knn_t = KNeighborsClassifier(n_neighbors=k).fit(X_train_s, y_train)
    acc = knn_t.score(X_test_s, y_test)
    if acc > best_acc:
        best_acc, best_k = acc, k
print(f"\nBest k-NN: k={best_k}, accuracy={best_acc:.4f}")

