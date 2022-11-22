import os
import numpy as np 
import pandas as pd
from joblib import load


class Serving:    
    def __init__(self):
        self.clf = load('infra/mlruns/clf_cat.pkl')
    
    def classifier(self, income: float, age: float, loan: float):
        x = np.array([income, age, loan]).reshape(1,3)
        return self.clf.predict(x)
    
    
