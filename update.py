import openai
import os
import sys
import shutil
from dotenv import load_dotenv, set_key
from copy import deepcopy

from prompts import pregenerated_files_dict, prompt_dict, pregenerated_file_prompt_dict
from main_requirement_file import create_requirement_file

# Load the contents of the .env file into the environment variables
load_dotenv()

# Fetch the openai api key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

if len(sys.argv) >= 2 and os.path.exists(sys.argv[1]):
    project_name = sys.argv[1]
    set_key(".env", "cookiecutter.project_name", project_name)
    print(f"switched to project `{project_name}`")

project_name = os.getenv("cookiecutter.project_name")
print(f"updating project `{project_name}`")


def invoke_completion_api(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=2000,
        top_p=0.1,
        presence_penalty=0,
        frequency_penalty=0,
    )
    print(
        {
            "openai_prompt": prompt,
            "openai_response": response,
        }
    )
    response_text = response.choices[0].text
    return response_text


combined_prompt_dict = deepcopy(prompt_dict)
combined_prompt_dict.update(pregenerated_file_prompt_dict)

# update files using prompts
for relative_file_location, prompt in combined_prompt_dict.items():
    response_text = invoke_completion_api(prompt)
    with open(relative_file_location, "w") as file:
        file.write(response_text)
        file.close()

# populate pregenerated files
for (
    relative_file_location,
    pregenerated_file_location,
) in pregenerated_files_dict.items():
    shutil.copy(pregenerated_file_location, relative_file_location)

create_requirement_file(project_name)
