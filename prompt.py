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

visualisation_query = "Give me code only - Read train and test data from {0} and {1} and separate categorical and numeric columns. For categorical columns plot {2}. For numeric columns plot {3}.".format(data["specifications"]["data_source"], data["specifications"]["data_source"], data["specifications"]["visualisation"]["categorical"], data["specifications"]["visualisation"]["numeric"])
pdb.set_trace()

prompts = {
    "visualisation": (
        visualisation_query,
        project_dir + "/visualisation/visualisa.py",
    )
}
