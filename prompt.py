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

# Print the contents of the result dictionary
print(result)

project_dir = result["default_context"]["project_name"].lower()


prompts = {
    project_dir
    + "/sample.py": "import train data from 'data/train.csv', test data from 'data/test.csv', with target column 'churn_value', load model from 'model/tree.pkl', predict 'churn_value' on train and test data and compute and print ['precision', 'recall', 'f1'] and save metrics in train_metrics.txt and test_metrics.txt"
}
