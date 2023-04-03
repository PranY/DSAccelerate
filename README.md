# DSAccelerate
Accelerating Analysts' Data Science Development


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


# ML Algorithms available
model_algorithm_name support in PyCaret:

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


# ChatGPT API Details


## sample prompt
```
"import train data from 'data/train.csv', test data from 'data/test.csv', with target column 'churn_value', load model from 'model/tree.pkl', predict 'churn_value' on train and test data and compute and print ['precision', 'recall', 'f1'] and save metrics in train_metrics.txt and test_metrics.txt"
```

## sample response
```
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": "\n\n# Importing necessary libraries\nimport pandas as pd\nimport numpy as np\nfrom sklearn.tree import DecisionTreeClassifier\nfrom sklearn.metrics import precision_recall_fscore_support\nfrom sklearn.externals import joblib\n\n# Loading train and test data\ntrain_data = pd.read_csv('data/train.csv')\ntest_data = pd.read_csv('data/test.csv')\n\n# Loading model\nmodel = joblib.load('model/tree.pkl')\n\n# Predicting on train and test data\ntrain_pred = model.predict(train_data.drop('churn_value', axis=1))\ntest_pred = model.predict(test_data.drop('churn_value', axis=1))\n\n# Computing precision, recall and f1\ntrain_metrics = precision_recall_fscore_support(train_data['churn_value'], train_pred, average='binary')\ntest_metrics = precision_recall_fscore_support(test_data['churn_value'], test_pred, average='binary')\n\n# Printing metrics\nprint('Train Metrics: Precision: {}, Recall: {}, F1: {}'.format(train_metrics[0], train_metrics[1], train_metrics[2]))\nprint('Test Metrics: Precision: {}, Recall: {}, F1: {}'.format(test_metrics[0], test_metrics[1], test_metrics[2]))\n\n# Saving metrics\nnp.savetxt('train_metrics.txt', train_metrics, delimiter=',')\nnp.savetxt('test_metrics.txt', test_metrics, delimiter=',')"
    }
  ],
  "created": 1680170256,
  "id": "cmpl-6zjKCKENY9Bj2wrlDUVLV7ye3wKSh",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 405,
    "prompt_tokens": 86,
    "total_tokens": 491
  }
}
```
