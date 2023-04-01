# DSAccelerate
Accelerating Analysts' Data Science Development

# Usage

1. Clone or download the DSAccelerate Project
2. Create a new environment using conda (preferred) or any other utility like venv for this project and run the command `make requirements` to setup the DSAccelerate Project.
3. You need to add your openai key to the project. Copy the `.env_sample` file and rename it to `.env`. Then, you need to paste your key against the OPENAI_API_KEY variable in the `.env` file.
4. Decide your project name and description, and run the command `make create <name> <description>` to create your project. In case you don't provide any arguments, a project with name `my_awesome_ds_project` will be created.
5. Go to the prompts.py file to inspect or edit the prompts, and run the command `make update`. This will update the project files in your project based on the prompts provided in the prompts.py file. You can repeat this step any number of times.
6. This will generate a DS project in a standardized template format. The number of tweaks needed to make the project runnable should be minimal, and depends on the quality of the ChatGPT prompt and model used.
7. You can run the `make help` or just `make` command to get the list of available commands.
8. In case you are working on multiple projects and wish to switch, you need to specify the project name (same as directory) in the `make update <name>` command.
9. A quickrun.py file has been provided for you to try out custom code if you need. This may help out during prompt engineering.
10. Once you are satisfied with the resulting project, you can start using it by creating a new environment for the project. This is different from the DSAccelerate environment which uses libraries like cookiecutter to generate projects, which will not be needed for your actual project.
11. You will need to setup the new environment by running the `make requirements` command inside the project.
12. After that you can run the project using the command `python __init__.py` which is where we are pushing the code that runs the project. In case you change this during project creation, you can run the standard `python <your file>` command to run it.
13. If you wish, you could also copy the prompts.py file into your DS Project for record keeping. It will act as an independent location for you to manage your custom prompts.

# Internals

## sample prompt
"import train data from 'data/train.csv', test data from 'data/test.csv', with target column 'churn_value', load model from 'model/tree.pkl', predict 'churn_value' on train and test data and compute and print ['precision', 'recall', 'f1'] and save metrics in train_metrics.txt and test_metrics.txt"

## sample response
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
