import os
import sys
import json
import subprocess
from dotenv import set_key

name = str(sys.argv[1]).lower() if len(sys.argv) >= 2 else "my_awesome_ds_project"
description = sys.argv[2] if len(sys.argv) >= 3 else "My Awesome DS Project"

if name in ["-h", "--help", "help"]:
    print(f"Usage: {sys.argv[0]} [optional_name] [optional_description]")
    sys.exit(0)

if os.path.exists(name):
    print(f"directory {name} already exists")
    sys.exit(1)

project_name = name
cookiecutter_config = {
    "default_context": {
        "project_name": project_name,
        "repo_name": "{{ cookiecutter.project_name.lower().replace(' ', '_') }}",
        "author_name": "Razorpay",
        "description": description,
        "open_source_license": "No license file",
        "s3_bucket": "No",
        "aws_profile": "default",
        "python_interpreter": "python3",
    }
}

print(cookiecutter_config)
with open("cookiecutter.json", "w") as f:
    # Write the config into JSON file
    f.write(json.dumps(cookiecutter_config))

subprocess.call(
    [
        "cookiecutter",
        "https://github.com/drivendata/cookiecutter-data-science",
        "--no-input",
        "--config-file",
        "cookiecutter.json",
        "-v",
    ]
)

set_key(".env", "cookiecutter.project_name", project_name)
