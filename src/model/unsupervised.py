import numpy as np
import pandas as pd
import joblib
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity


def build_model (features) :
    '''
    model : Centroid Based Anomaly Detection
    '''
    
    # feature scaling
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # mean_vector
    model = np.mean(features_scaled, axis = 0)
    
    # save
    joblib.dump(model, "model.pkl")
    joblib.dump(scaler, "scaler.pkl")

    return ;


def predict (data) :

    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")

    scaled = scaler.transform(data)
    similarity = cosine_similarity(scaled, model.reshape(1, -1))[0, 0]

    # -1 <= similarity <= 1
    # min-max normalization
    result = (similarity + 1) / 2
    # for percent
    # significant : 2
    result = round(result * 100, 2)

    return result
    

if (__name__ == "__main__") :
    
    build_model(features)
