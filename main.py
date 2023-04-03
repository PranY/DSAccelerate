from pathlib import Path
import subprocess
import os
import json
import shutil

from openai_wrapper import invoke_completion_api
from prompt import prompts

from main_requirement_file import create_requirement_file
from model.data_split import do_data_split_processing
from model.model_training import create_model_training_code

# Set the path to the custom JSON file

cookiecutter_json_path = Path.cwd() / "project_config.json"


def write_content_to_project(prompt_details):
    prompt, file_location = prompt_details
    response_text = invoke_completion_api(prompt)
    with open(file_location, "w") as file:
        file.write(response_text)

def create_constant_file(request_config):
    my_const_dict = {}
    my_const_dict["label"] = f"""{request_config["specifications"]["label"]}"""
    my_const_dict["evaluation"] = request_config["specifications"]["training"]["evaluation"]
    with open('.internal/constant.py', 'w') as f:
        # Loop over the dictionary keys and write variables to the file
        for key in my_const_dict:
            # Use exec() to create a variable with the key name and the dictionary value
            exec(f"""{key} = "{my_const_dict[key]}" """, globals())
            # Write the variable to the file
            f.write(f"""{key} = "{my_const_dict[key]}"\n""")


if __name__ == "__main__":
    # Call the cookiecutter command-line tool with the custom JSON file
    # Open the file containing the JSON data
    with open(cookiecutter_json_path, "r") as f:
        # Load the JSON data from the file
        request_config = json.load(f)
    project_dir = request_config["default_context"]["project_name"].lower()
    if not os.path.exists(project_dir):
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
    shutil.copy(".internal/make_dataset.py", project_dir + "/src/data/make_dataset.py")
    write_content_to_project(
        do_data_split_processing(
            prompts["model_data_splitting"], request_config, project_dir
        )
    )
    write_content_to_project(
        create_model_training_code(
            prompts["model_training"], request_config, project_dir
        )
    )
    write_content_to_project(prompts["visualisation"])
    create_requirement_file(project_dir)
    shutil.copy(".internal/template_main.py", project_dir + "/src/__init__.py")
    create_constant_file(request_config)
    shutil.copy(".internal/constant.py", project_dir + "/src/constant.py")
