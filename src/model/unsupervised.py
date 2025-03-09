import numpy as np
import pandas as pd
import joblib
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity


def build_model (features, eps = 0.5, min_samples = 2) :
    
    '''
    model : DBSCAN 
    '''
    
    # feature scaling
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # clustering 
    dbscan = DBSCAN(eps = eps, min_samples = min_samples, metric = "euclidean")
    clusters = dbscan.fit_predict(features_scaled)

    # save
    joblib.dump(dbscan, "model.pkl")
    joblib.dump(scaler, "scaler.pkl")
    
    return clusters


def predict (data) :
    


if (__name__ == "__main__") :
    
    ;
