import tensorflow as tf
import joblib
import numpy as np
heart_model=tf.keras.models.load_model("heart_model.h5")
diabetes_model=tf.keras.models.load_model("diabetes_model.h5")
scalar_model=joblib.load("heart_scalar.pkl")
def predict_heart_disease(features:list):
    data=np.array([features])
    data_scaled=scalar_model.transform(data)
    pred=heart_model.predict(data_scaled)
    return float(pred[0][0])
scalar_model=joblib.load("diabetes_scalar.pkl")
def predict_diabetes_disease(features:list):
    data=np.array([features])
    data_scaled=scalar_model.transform(data)
    pred=diabetes_model.predict(data_scaled)
    return float(pred[0][0])