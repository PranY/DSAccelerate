# DSAccelerate
Accelerating Data Science Development using ChatGPT.


# Instructions

1. Setup DSAccelerate
    1. Download the repository zip file or clone it using the git clone command.
    2. (Recommended) Create a new python environment using conda, venv or any other service.
    3. Run the `make download` command to set it up.
2. Create your new project
    1. Provide your specifications in the `project_config.json` file.
    2. Run the `make run` command to generate your project.
3. Setup your new project
    1. (Recommended) Create a new python environment using conda, venv or any other service for your project.
    2. Get into your project directory and run the `make requirements` command to setup your environments.
    3. Tweak the generated files as per your requirements and resolve any errors if they occur.
    4. Finally, run your project using the command `python src/__init__.py`


# Available ML Algorithms
`model_algorithm_name` support in PyCaret:

- Logistic Regression ('lr')
- K Neighbors Classifier ('knn')
- Naive Bayes ('nb')
- Decision Tree Classifier ('dt')
- Random Forest Classifier ('rf')
- Extra Trees Classifier ('et')
- Gradient Boosting Classifier ('gbc')
- Extreme Gradient Boosting Classifier ('xgboost')
- Light Gradient Boosting Machine ('lightgbm')
- CatBoost Classifier ('catboost')
- AdaBoost Classifier ('ada')
- Linear Discriminant Analysis ('lda')
- Quadratic Discriminant Analysis ('qda')
- Ridge Classifier ('ridge')
- Ridge Classifier CV ('ridgecv')
- Passive Aggressive Classifier ('pac')
- Perceptron ('perceptron')
- Voting Classifier ('voting')
- Stacking Classifier ('stacking')
