import json

# Open the JSON file
with open("project_config.json", "r") as f:
    # Load the JSON data into a Python dictionary
    data = json.load(f)

# Create a dictionary of dictionaries
result = {}

# Iterate over the items in the original dictionary
for key, value in data.items():
    # If the value is a dictionary, add it to the result dictionary
    if isinstance(value, dict):
        result[key] = value

# Get project directory from config
project_dir = result["default_context"]["project_name"].lower()

# Prompt Structure
# {
#     task: (
#         prompt,
#         file_path
#     )
# }

# visualisation_query = "Give me code only - Read train and test data from {0} and {1} and separate categorical and numeric columns. For categorical columns plot {2}. For numeric columns plot {3}.".format(
#     data["specifications"]["data_source"],
#     data["specifications"]["data_source"],
#     data["specifications"]["visualisation"]["categorical"],
#     data["specifications"]["visualisation"]["numeric"],
# )

visualisation_query = """Give me code only with imports- Create a `Visualization` class which will take 3 dataset `train_data`, `test_data`, validate data, best model artifact `best_model` and target column name `label_name`.
    For categorical columns add code to plot {0} in function `plot_categorical_features` with relevant Plot title for each column name.
    For numeric columns add code to plot {1} in function `plot_numerical_features` with relevant Plot title for each column name.
    Using model `best_model` plot {2} in function `plot_model_metrics` with associated metric as Plot title.
    Create a function `visualize` in class `Visualization` which call `plot_categorical_features`, `plot_numerical_features` and `plot_model_metrics`.
    """.format(
    data["specifications"]["visualisation"]["categorical"],
    data["specifications"]["visualisation"]["numeric"],
    data["specifications"]["visualisation"]["model"],
)

prompts = {
    "visualisation": (
        visualisation_query,
        project_dir + "/src/visualization/visualize.py",
    ),
    "model_data_splitting": (
        """Write a python code with imports to create a class with name 'ModelDataSplitter' containing a function name `do_data_split` by taking X and train test split AS {train_test_split_percentage} and train validation split {test_val_split_percentage}.
        The class should also save the split dataset in csv format inside {location} folder with file name train, validate and test.
        """,
        "/src/models/data_split.py",
    ),
    "model_training": (
        """Give me code with imports to create a class 'ModelTraining' which takes training data `training_data`, label name `label_name` and best model metric`best_model_metric` as input. 
        The class constructor should set `model_save_location` to {location} which will be used to save all model created artifacts and also take `model_algorithm_name` which could be null.
        This class should contain `train_models` function which will use pycaret library and train data on {model_algorithm_name} if not null or all {model_type} algorithms and saved all the model iteratively at location `model_save_location` inside try and except to handle exception. 
        This class should contain `evaluate_model` function which will read all the models trained and kept in `model_save_location` location by `train_models` function and compare them based on`best_model_metric` metric value and return the best model
        """,
        "/src/models/train_model.py",
    ),
}
