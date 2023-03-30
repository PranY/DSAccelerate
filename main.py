from pathlib import Path
import subprocess
import openai
import os
from dotenv import load_dotenv

# Load the contents of the .env file into the environment variables
load_dotenv()

# Fetch the openai api key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set the path to the custom JSON file
cookiecutter_json_path = Path.cwd() / "project_config.json"

# Call the cookiecutter command-line tool with the custom JSON file
subprocess.call(
    [
        "cookiecutter",
        "https://github.com/drivendata/cookiecutter-data-science",
        "--no-input",
        "--config-file",
        str(cookiecutter_json_path),
        "-v",
    ]
)

prompt = """import train data from 'data/train.csv', test data from 'data/test.csv', with target column 'churn_value', load model from 'model/tree.pkl', predict 'churn_value' on train and test data and compute and print ['precision', 'recall', 'f1'] and save metrics in train_metrics.txt and test_metrics.txt"""

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=1000,
    top_p=0.1,
    presence_penalty=0,
    frequency_penalty=0,
)
print("openai response")
print(response)

with open("sample.py", "w") as file:
    file.write(response.choices[0].text)
