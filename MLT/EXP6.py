# ============================================================
# EX.NO: 6 – Support Vector Machine (User Behavior)
# ============================================================

"""
AIM
To implement SVM to identify user behavior classes and plot the
confusion matrix using Seaborn.
"""

"""
PROCEDURE
1. Create dataset with Login_Frequency, Time_Spent, Pages_Visited,
   Actions_Performed and Behavior_Class (0=Casual,1=Regular,2=Power).
2. Split 75:25; train SVC with linear kernel.
3. Predict and evaluate; plot confusion matrix heatmap.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    "Login_Frequency":  [1,2,3,5,6,8,10,12,3,4,7,9],
    "Time_Spent":       [0.5,1,1.5,2,2.5,3,4,4.5,1.2,1.8,3.2,4],
    "Pages_Visited":    [5,8,10,15,18,25,30,35,12,14,22,28],
    "Actions_Performed":[2,3,4,6,7,10,12,15,5,6,9,11],
    "Behavior_Class":   [0,0,0,1,1,1,2,2,1,1,2,2]
}
df = pd.DataFrame(data)
X, y = df.drop("Behavior_Class", axis=1), df["Behavior_Class"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42)

svm = SVC(kernel="linear").fit(Xtr, ytr)
yp  = svm.predict(Xte)
print("SVM Accuracy:", accuracy_score(yte, yp))
print("\nClassification Report:\n", classification_report(yte, yp))

cm = confusion_matrix(yte, yp)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Casual","Regular","Power"],
            yticklabels=["Casual","Regular","Power"])
plt.xlabel("Predicted"); plt.ylabel("True")
plt.title("Confusion Matrix - SVM")
plt.show()

"""
OUTPUT
SVM Accuracy: 0.6666666666666666
Classification Report:
              precision  recall  f1-score  support
           0       1.00    1.00      1.00        1
           1       0.50    1.00      0.67        1
           2       0.00    0.00      0.00        1
    accuracy                         0.67        3
"""

"""
RESULT
SVM was successfully implemented to classify user behavior into
Casual, Regular, and Power user categories.
"""