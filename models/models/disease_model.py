import pandas as pd
import numpy as np
import pickle

from sklearn.ensemble import RandomForestClassifier

np.random.seed(42)

data = pd.DataFrame({

    "Age":np.random.randint(18,80,1000),
    "BP":np.random.randint(90,180,1000),
    "Sugar":np.random.randint(70,300,1000),
    "Cholesterol":np.random.randint(120,300,1000),
    "Disease":np.random.randint(0,2,1000)

})

X = data[
[
"Age",
"BP",
"Sugar",
"Cholesterol"
]
]

y = data["Disease"]

model = RandomForestClassifier()

model.fit(X,y)

pickle.dump(
    model,
    open(
        "models/disease_model.pkl",
        "wb"
    )
)

print("Model Saved")