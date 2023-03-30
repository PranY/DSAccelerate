import json
import pdb 

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

# ------THESE THREE VARIABLES, WE NEED TO DISCUSS WITH ADITI-------
hard_traintest_data_path = "data_path"
hard_train_save_path = "train.txt"
hard_test_save_path = "test.txt"
metrics_query_to_gpt = "give me code only - import train data from '{0}', test data from '{1}', with target column '{2}', load model from '{3}', predict '{2}' on train and test data and compute and print {4} and save metrics in {5} and {6}".format(hard_traintest_data_path, hard_traintest_data_path, data["specifications"]["target_column"], data["specifications"]["training"]["save_model"], data["specifications"]["metrics"], hard_train_save_path, hard_test_save_path)
pdb.set_trace()

prompts = {
    "matrics": (
        metrics_query_to_gpt,
    )
}
