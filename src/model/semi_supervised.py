import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.semi_supervised import LabelPropagation


def build_model (features, labels) :
    '''
    model : Label Propagation
    '''
    
    # feature scaling
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # label propagation
    model = LabelPropagation()
    model.fit(features_scaled, labels)

    # save
    joblib.dump(model, "model.pkl")
    joblib.dump(scaler, "scaler.pkl")

    return ;


def predict (data) :
    
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")

    scaled = scaler.transform(data)
    prediction = model.predict(scaled)

    result = round(prediction[0][1] * 100, 2)

    return result


if (__name__ == "__main__") :

    build_model(features, labels)

    # labels
    # true : 1
    # false : 0
    # none : -1

