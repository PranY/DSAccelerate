from pathlib import Path
import subprocess

# Install Cookiecutter
subprocess.run(["pip", "install", "cookiecutter"])

# Set the path to the custom JSON file
cookiecutter_json_path = Path.cwd()/'cookiecutter.json'
# Call the cookiecutter command-line tool with the custom JSON file
subprocess.call(["cookiecutter", "https://github.com/drivendata/cookiecutter-data-science","--no-input","--config-file", str(cookiecutter_json_path), "-v", ])
