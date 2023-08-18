import pickle
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Obtener la ruta completa del archivo .py
script_dir = os.path.dirname(os.path.abspath(__file__))

# Cambiar el directorio de trabajo al directorio del archivo .py
os.chdir(script_dir)


df_test = pd.read_csv("data/df_test.csv", sep=",")

X_test = df_test.drop(["HeartDisease"], axis=1)
y_test = df_test["HeartDisease"]

pickled_model = pickle.load(open("model/production/model_230818122335.pkl", "rb"))
prediction = pickled_model.predict(X_test)

np.savetxt("data/prediction.csv", prediction, delimiter=",")
