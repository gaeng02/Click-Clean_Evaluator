import numpy as np 
import joblib 
from sklearn.preprocessing import StandardScaler 
from sklearn.linear_model import LogisticRegression 


def build_model (features, labels) : 
    ''' 
    model : Logistic Regression 
    ''' 
     
    # feature scaling 
    scaler = StandardScaler() 
    features_scaled = scaler.fit_transform(features) 

    # logistic regression 
    model = LogisticRegression() 
    model.fit(features_scaled, labels) 

    # save 
    joblib.dump(model, "model.pkl") 
    joblib.dump(scaler, "scaler.pkl") 

    return ; 


def predict (data) : 
     
    model = joblib.load("model.pkl") 
    scaler = joblib.load("scaler.pkl") 
 
    scaled = scaler.transform(data) 
    prediction = model.predict_proba(scaled) 

    result = round(prediction[0][1] * 100, 2)

    return result


if (__name__ == "__main__") :

    build_model(features, labels)
