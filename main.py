from pathlib import Path
import subprocess

from openai_wrapper import get_response
from prompt import prompts

# Set the path to the custom JSON file
cookiecutter_json_path = Path.cwd() / "project_config.json"


def write_content_to_project():
    for file_location, prompt in prompts.items():
        response_text = get_response(prompt)
        with open(file_location, "w") as file:
            file.write(response_text)


if __name__ == "__main__":
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
    write_content_to_project()
