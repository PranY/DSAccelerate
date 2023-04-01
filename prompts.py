import os
from dotenv import load_dotenv

load_dotenv()
project_name = os.getenv("cookiecutter.project_name")

# use this dict to map the pregenerated files to the corresponding project files
pregenerated_files_dict = {
    f"{project_name}/requirements.txt": "pregenerated_files/requirements.txt",
    f"{project_name}/src/data/make_dataset.py": "pregenerated_files/make_dataset.py",
    f"{project_name}/src/features/build_features.py": "pregenerated_files/build_features.py",
    f"{project_name}/src/__init__.py": "pregenerated_files/main.py",
}

# use this prompt dictionary to populate the project file with chatgpt prompt responses
prompt_dict = {
    # model data splitting
    f"{project_name}/src/models/data_split.py": "Write a python code with imports to create a class with name `ModelDataSplitter` containing a function name `do_data_split` by taking X and train test split AS 30 percent and train validation split 20 percent. The class should also save the split dataset in csv format inside `data/interim` folder with file name train, validate and test.",
    # model training
    f"{project_name}/src/models/train_model.py": "Give me code with imports to create a class 'ModelTraining' which takes training data `training_data`, label name `label_name` and best model metric `best_model_metric` as input. The class constructor should set `model_save_location` to `models` directory which will be used to save all model created artifacts. This class should contain `train_models` function which will use pycaret library and train data on all `classification` algorithms and saved all the model iteratively at location `model_save_location`. This class should contain `evaluate_model` function which will read all the models trained and kept in `model_save_location` location by `train_models` function and compare them based on`best_model_metric` metric value and return the best model",
    # visualization
    f"{project_name}/src/visualization/visualize.py": "Give me code only with imports- Create a `Visualization` class which will take 3 dataset `train_data`, `test_data`, validate data, best model artifact `best_model` and target column name `label_name`. For categorical columns add code to plot [`bar graph`, `pie chart`, `heatmap`] in function `plot_categorical_features` with relevant Plot title for each column name. For numeric columns add code to plot [`histogram with 10 bins`, `box plot`, `density plot`, `scatter plot`, `heatmap`] in function `plot_numerical_features` with relevant Plot title for each column name. Using model `best_model` plot [`AUC`, `Confusion Matrix`, `Precision Recall Curve`] in function `plot_model_metrics` with associated metric as Plot title. Create a function `visualize` in class `Visualization` which call `plot_categorical_features`, `plot_numerical_features` and `plot_model_metrics`.",
}

pregenerated_file_prompt_dict = {
    # Make data - read csv file
    # "pregenerated_files/make_data_csv_file.py": "Write python code with documentation following the pep8 guidelines. Write a function that uses pandas library and is able to read a csv file, the function should take input of the csv file path.",
    # Make data - read csv url
    # "pregenerated_files/make_data_csv_url.py": "Write python code with documentation following the pep8 guidelines. Write a function that is able to read a csv file, the function should take input of a url path. Return a pandas dataframe is the csv reading is successful.",
    # Make data - read sql query
    # "pregenerated_files/make_data_sql_query.py": "Write python code with documentation following the pep8 guidelines. Write a function that reads data using a SQL query provided in string format in the function. Allow the user to additionally provide any SQL connector related parameters. If the connector parameters are provided, write a connecter internal to the method and execute the query, otherwise raise relevant errors.",
    # Make data - read redis data
    # "pregenerated_files/make_data_redis.py": "Write python code with documentation following the pep8 guidelines. Write a function that reads data from redis and loads it into pandas dataframe",
    # Feature engineering
    # "pregenerated_files/build_features.py": "Write python code with documentation following the pep8 guidelines. Write a class that has various methods to handle different kind of feature engineering steps. Keep one method for one idea. The class should be able to handle all types of feature engineering methods pertaining to regressions and classification problem statements in machine learning. Provide reasonable input options for methods that may require user input but keep it optional. Also ensure that the order of methods doesn't break the code. The constructor of the class should ask for a pandas dataframe and return a feature engineered dataframe in response. The constructor should also ask if the approach is classification or regression and according run relevant sequence of methods before returning the updated dataframe.",
}
