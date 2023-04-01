import openai
import os
import sys
import shutil
from dotenv import load_dotenv, set_key
import pkgutil
import inspect


from prompts import pregenerated_files_dict, prompt_dict

# Load the contents of the .env file into the environment variables
load_dotenv()

# Fetch the openai api key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

if len(sys.argv) >= 2 and os.path.exists(sys.argv[1]):
    project_name = sys.argv[1]
    set_key(".env", "cookiecutter.project_name", project_name)
    print(f'switched to project `{project_name}`')

project_name = os.getenv('cookiecutter.project_name')
print(f'updating project `{project_name}`')

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

def update_requirements_txt():

    # List of modules to ignore
    ignore_modules = ["builtins", "sys", "os", "math", "random"]

    # List of Python script files in the project directory
    python_files = [filename for filename in os.listdir(project_name) if filename.endswith(".py")]

    # Set of used modules
    used_modules = set()

    # Loop over Python script files
    for filename in python_files:
        # Get list of imported modules
        imported_modules = []
        module_name = os.path.splitext(filename)[0]
        module = __import__(module_name)
        for name, module in inspect.getmembers(module):
            if inspect.ismodule(module) and not name.startswith("_") and module.__name__ not in ignore_modules:
                imported_modules.append(module.__name__)

        # Get list of modules used by the script
        for module in imported_modules:
            used_modules.add(module)
            try:
                package = __import__(module)
                for importer, modname, ispkg in pkgutil.walk_packages(package.__path__):
                    used_modules.add(modname)
            except ImportError:
                pass

    # Write list of modules to requirements.txt
    with open(project_name+"/requirements.txt", "a") as f:
        for module in sorted(list(used_modules)):
            f.write(module + "\n")

# populate pregenerated files
for relative_file_location, pregenerated_file_location in pregenerated_files_dict.items():
    file_location = project_name + "/" + relative_file_location
    shutil.copy(pregenerated_file_location, file_location)

# update files using prompts
for relative_file_location, prompt in prompt_dict.items():
    file_location = project_name + "/" + relative_file_location
    response_text = invoke_completion_api(prompt)
    with open(file_location, "w") as file:
        file.write(response_text)
        file.close()

update_requirements_txt()
