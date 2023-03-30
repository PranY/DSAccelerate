from pathlib import Path
import subprocess

# Install Cookiecutter
subprocess.run(["pip", "install", "cookiecutter"])

# Set the path to the custom JSON file
cookiecutter_json_path = Path.cwd()/'project_config.json'
# Call the cookiecutter command-line tool with the custom JSON file
subprocess.call(["cookiecutter", "https://github.com/drivendata/cookiecutter-data-science","--no-input","--config-file", str(cookiecutter_json_path), "-v", ])

def insert_metrices_code(project_json):
  """
  takes in config
  generates query for chat gpt 
  
  TODO : pass it to API and parse the response and mkdir/touch and insert the code
  """
  query_to_gpt = "import train data from '{0}', test data from '{1}', with target column '{2}', load model from '{3}', predict '{2}' on train and test data and compute and print {4} and save metrics in train_metrics.txt and test_metrics.txt".format("data/train.csv", "data/test.csv", project_json["target_column"], "model/tree.pkl", project_json["metrics"])
