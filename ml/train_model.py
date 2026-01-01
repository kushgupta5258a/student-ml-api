import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Dummy dataset
data = {
    "study_hours": [1,2,3,4,5,6,7,8],
    "attendance": [40,45,50,60,65,70,80,90],
    "result": [0,0,0,0,1,1,1,1]  # 0 = fail, 1 = pass
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance"]]
y = df["result"]

model = LogisticRegression()
model.fit(X, y)

os.makedirs("model", exist_ok=True)
pickle.dump(model, open("model/model.pkl", "wb"))

print("✅ Model trained & saved")
