import os
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Ruta completa del archivo .py
script_dir = os.path.dirname(os.path.abspath(__file__))

# Cambio del directorio de trabajo al directorio del archivo .py
os.chdir(script_dir)

df = pd.read_csv("data/df.csv", sep=",")
X = df.drop(["HeartDisease"], axis=1)
y = df["HeartDisease"]
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(
    class_weight="balanced", max_depth=3, random_state=42, min_samples_split=2
)
model.fit(X_train, y_train)

# Guardar el modelo
model_filename = "model/production/model_230818122335.pkl"
model_path = os.path.join(script_dir, model_filename)
pickle.dump(model, open(model_path, "wb"))
