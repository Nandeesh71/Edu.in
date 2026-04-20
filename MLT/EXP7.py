# ============================================================
# EX.NO: 7 – Random Forest (Driving Habits Classification)
# ============================================================

"""
AIM
To apply Random Forest to classify users based on driving habits and
plot the confusion matrix using Seaborn.
"""

"""
PROCEDURE
1. Create dataset with Avg_Daily_Distance, Driving_Hours,
   Speed_Variation, Trips_Per_Week and Driving_Class.
2. Split 75:25; train RandomForestClassifier (100 trees).
3. Predict and evaluate; plot confusion matrix heatmap.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = {
    "Avg_Daily_Distance": [10,15,20,40,60,80,5,8,25,45,70,90],
    "Driving_Hours":      [1,1.5,2,3,4,5,0.5,1,2.5,3.5,4.5,5.5],
    "Speed_Variation":    [2,3,3,5,6,7,1,2,4,5,6,7],
    "Trips_Per_Week":     [5,6,7,8,9,10,3,4,7,8,9,10],
    "Driving_Class":      [0,0,0,1,1,1,2,2,0,1,1,1]
}
df = pd.DataFrame(data)
X, y = df.drop("Driving_Class", axis=1), df["Driving_Class"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42)

rf = RandomForestClassifier(n_estimators=100, random_state=42).fit(Xtr, ytr)
yp = rf.predict(Xte)
print("Random Forest Accuracy:", accuracy_score(yte, yp))
print("\nClassification Report:\n", classification_report(yte, yp))

cm = confusion_matrix(yte, yp)
sns.heatmap(cm, annot=True, fmt="d", cmap="Greens",
            xticklabels=["Commuter","Long-Distance","Occasional"],
            yticklabels=["Commuter","Long-Distance","Occasional"])
plt.xlabel("Predicted"); plt.ylabel("True")
plt.title("Confusion Matrix - Random Forest")
plt.show()

"""
OUTPUT
Random Forest Accuracy: 0.6666666666666666
Classification Report:
              precision  recall  f1-score  support
           0       0.00    0.00      0.00        1
           1       1.00    1.00      1.00        2
           2       0.00    0.00      0.00        0
    accuracy                         0.67        3
"""

"""
RESULT
Random Forest was successfully implemented to classify users based
on driving habits.
"""