# ============================================================
# EX.NO: 4 – Naïve Bayes & KNN (Level of Experience)
# ============================================================

"""
AIM
To apply Naïve Bayes and KNN supervised learning algorithms to
identify the Level of Experience of a user.
"""

"""
PROCEDURE
1. Create dataset with Age, Education_Level, Years_of_Experience,
   Skill_Score and Experience_Level (0=Junior,1=Mid,2=Senior).
2. Split 70:30.
3. Train GaussianNB and KNeighborsClassifier (k=3).
4. Predict and evaluate Accuracy, Precision, Recall, F1.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

data = {
    "Age":                 [22,25,28,35,40,45,23,27,32,38],
    "Education_Level":     [1,2,2,3,3,3,1,2,2,3],
    "Years_of_Experience": [0,2,4,8,12,20,1,3,6,10],
    "Skill_Score":         [3,5,6,8,9,9,4,6,7,8],
    "Experience_Level":    [0,0,1,1,2,2,0,1,1,2]
}
df = pd.DataFrame(data)
X = df.drop("Experience_Level", axis=1)
y = df["Experience_Level"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42)

nb = GaussianNB().fit(Xtr, ytr)
knn = KNeighborsClassifier(n_neighbors=3).fit(Xtr, ytr)

print("Naive Bayes Accuracy:", accuracy_score(yte, nb.predict(Xte)))
print("KNN Accuracy:",         accuracy_score(yte, knn.predict(Xte)))
print("\nNaive Bayes Report:\n", classification_report(yte, nb.predict(Xte)))
print("\nKNN Report:\n",         classification_report(yte, knn.predict(Xte)))

"""
OUTPUT
Naive Bayes Accuracy: 0.3333333333333333
KNN Accuracy:         0.6666666666666666

Naive Bayes Report:
              precision  recall  f1-score  support
           0       0.00    0.00      0.00        1
           1       0.33    1.00      0.50        1
           2       0.00    0.00      0.00        1
    accuracy                         0.33        3

KNN Report:
              precision  recall  f1-score  support
           0       0.00    0.00      0.00        1
           1       0.50    1.00      0.67        1
           2       1.00    1.00      1.00        1
    accuracy                         0.67        3
"""

"""
RESULT
Naïve Bayes and KNN were successfully implemented to classify the
level of experience.
"""