# use this dict to map the pregenerated files to the corresponding project files
pregenerated_files_dict = {
    "/requirements.txt": "pregenerated_files/requirements.txt",
    "/src/data/make_dataset.py": "pregenerated_files/make_dataset.py",
    "/src/features/build_features.py": "pregenerated_files/build_features.py",
    "/src/__init__.py": "pregenerated_files/main.py",
}

# use this prompt dictionary to populate the project file with chatgpt prompt responses
prompt_dict = {
    # model data splitting
    "/src/models/data_split.py": "Write a python code with imports to create a class with name `ModelDataSplitter` containing a function name `do_data_split` by taking X and train test split AS 30 percent and train validation split 20 percent. The class should also save the split dataset in csv format inside `data/interim` folder with file name train, validate and test.",
    # model training
    "/src/models/train_model.py": "Give me code with imports to create a class 'ModelTraining' which takes training data `training_data`, label name `label_name` and best model metric `best_model_metric` as input. The class constructor should set `model_save_location` to `models` directory which will be used to save all model created artifacts. This class should contain `train_models` function which will use pycaret library and train data on all `classification` algorithms and saved all the model iteratively at location `model_save_location`. This class should contain `evaluate_model` function which will read all the models trained and kept in `model_save_location` location by `train_models` function and compare them based on`best_model_metric` metric value and return the best model",
    # visualization
    "/src/visualization/visualize.py": "Give me code only with imports- Create a `Visualization` class which will take 3 dataset `train_data`, `test_data`, validate data, best model artifact `best_model` and target column name `label_name`. For categorical columns add code to plot [`bar graph`, `pie chart`, `heatmap`] in function `plot_categorical_features` with relevant Plot title for each column name. For numeric columns add code to plot [`histogram with 10 bins`, `box plot`, `density plot`, `scatter plot`, `heatmap`] in function `plot_numerical_features` with relevant Plot title for each column name. Using model `best_model` plot [`AUC`, `Confusion Matrix`, `Precision Recall Curve`] in function `plot_model_metrics` with associated metric as Plot title. Create a function `visualize` in class `Visualization` which call `plot_categorical_features`, `plot_numerical_features` and `plot_model_metrics`.",
}
