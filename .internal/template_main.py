from src.data.make_dataset import read_csv_file
from src.models.data_split import ModelDataSplitter
from src.models.train_model import ModelTraining
from src.visualization.visualize import Visualization
import os

import constant as const

data = read_csv_file("~/Downloads/archive/Iris.csv")
ModelDataSplitter(data).do_data_split()
path = os.path.join("data", "interim")
X_train = read_csv_file(os.path.join(path, "train.csv"))
X_val = read_csv_file(os.path.join(path, "validate.csv"))
X_test = read_csv_file(os.path.join(path, "test.csv"))
model = ModelTraining(X_train, const.label, const.evaluation)
model.train_models()
best_model = model.evaluate_model()
Visualization(X_train, X_test, X_val, best_model, const.label).visualize()
