import os
import subprocess

# Specify the project parameters
project_name = "my_project"
repo_name = project_name
author_name = "Razorpay"
description = "A default description."
license = "3 - No license file"

# Check if the project directory already exists
if os.path.exists(project_name):
    print(f"Project directory '{project_name}' already exists.")
else:
    # Install Cookiecutter
    subprocess.run(["pip", "install", "cookiecutter"])

    # Create a new project using Cookiecutter
    cookiecutter_params = {
        "project_name": project_name,
        "repo_name": repo_name,
        "author_name": author_name,
        "description": description,
        "open_source_license": license,
        "aws_s3_bucket": "no",
        "python_interpreter": "python3"
    }
    subprocess.run(["cookiecutter", "https://github.com/drivendata/cookiecutter-data-science.git", "--no-input"], input=str(cookiecutter_params).encode())
    print(f"Created new project '{project_name}' using Cookiecutter.")
