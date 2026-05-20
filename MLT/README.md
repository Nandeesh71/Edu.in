# 24AMPW401 – Machine Learning Techniques with Laboratory

**Institution:** Sri Sai Ram Engineering College, Chennai  
**Department:** CSE (Artificial Intelligence & Machine Learning)  
**Year / Sem:** II Year / IV Semester | Batch: 2024–2028  
**Academic Year:** 2025–2026

---

## List of Experiments

| Ex No | Title | Dataset | File |
|-------|-------|---------|------|
| 01 | Data Preprocessing Techniques | Data_preprocessing.csv | `ex01_data_preprocessing/data_preprocessing.py` |
| 02 | Simple & Multiple Linear Regression | GHI_Report.csv | `ex02_linear_regression/linear_regression.py` |
| 03 | Polynomial Regression | GHI_Report.csv | `ex03_polynomial_regression/polynomial_regression.py` |
| 04 | Naive Bayes and KNN | GHI_Report.csv | `ex04_naive_bayes_knn/naive_bayes_knn.py` |
| 05 | Decision Tree Classifier | Toyota.csv | `ex05_decision_tree/decision_tree.py` |
| 06 | Support Vector Machine (SVM) | user_behavior_dataset.csv | `ex06_svm/svm.py` |
| 07 | Random Forest Algorithm | ev_charging_patterns.csv | `ex07_random_forest/random_forest.py` |
| 08 | AdaBoost Technique | credit_risk_dataset.csv | `ex08_adaboost/adaboost.py` |
| 09 | XGBoost and LightGBM | MBA.csv | `ex09_xgboost_lightgbm/xgboost_lightgbm.py` |
| 10 | K-Means and Hierarchical Clustering | credit_risk_dataset.csv | `ex10_kmeans_hierarchical/kmeans_hierarchical.py` |

---

## Setup on Mac

### Step 1 – Install Python
```bash
brew install python
python3 --version
```

### Step 2 – Create Virtual Environment
```bash
python3 -m venv mlt_env
source mlt_env/bin/activate
```

### Step 3 – Install Required Libraries
```bash
pip install numpy pandas matplotlib scikit-learn seaborn xgboost lightgbm scipy
```

### Step 4 – Run Any Experiment
```bash
# Place the required CSV dataset in the same folder as the .py file, then:
cd ex01_data_preprocessing
python3 data_preprocessing.py
```

---

## Datasets Required

| Dataset | Used In |
|---------|---------|
| Data_preprocessing.csv | Ex 01 |
| GHI_Report.csv | Ex 02, 03, 04 |
| Toyota.csv | Ex 05 |
| user_behavior_dataset.csv | Ex 06 |
| ev_charging_patterns.csv | Ex 07 |
| credit_risk_dataset.csv | Ex 08, 10 |
| MBA.csv | Ex 09 |

---

## Tech Stack
Python 3 · NumPy · Pandas · Scikit-learn · Matplotlib · Seaborn · XGBoost · LightGBM · SciPy
