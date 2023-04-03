
import pandas as pd
from sklearn.model_selection import train_test_split

class ModelDataSplitter:
    def __init__(self, X):
        self.X = X
    
    def do_data_split(self):
        X_train, X_test = train_test_split(self.X, test_size=0.3, random_state=42)
        X_train, X_val = train_test_split(X_train, test_size=0.2, random_state=42)
        
        X_train.to_csv('data/interim/train.csv', index=False)
        X_val.to_csv('data/interim/validate.csv', index=False)
        X_test.to_csv('data/interim/test.csv', index=False)