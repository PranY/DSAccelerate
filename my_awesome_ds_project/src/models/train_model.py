import pandas as pd
import pycaret
from pycaret.classification import *
import pickle

class ModelTraining:
    def __init__(self, training_data, label_name, best_model_metric, model_save_location, model_algorithm_name=None):
        self.training_data = training_data
        self.label_name = label_name
        self.best_model_metric = best_model_metric
        self.model_save_location = model_save_location
        self.model_algorithm_name = model_algorithm_name

    def train_models(self):
        try:
            if self.model_algorithm_name is not None:
                model = setup(data=self.training_data, target=self.label_name, model_name=self.model_algorithm_name)
            else:
                model = setup(data=self.training_data, target=self.label_name)
            best_model = compare_models(sort=self.best_model_metric)
            save_model(best_model, model_name='best_model')
        except Exception as e:
            print(" error" ,e)

    def evaluate_model(self):
        try:
            best_model = load_model(model_name='best_model')
            return best_model
        except Exception as e:
            print(e)