import os
import ast


def get_imported_libraries(file_path):
    with open(file_path, "r") as f:
        node = ast.parse(f.read())
    imported_libraries = []
    for n in node.body:
        if isinstance(n, ast.Import):
            for alias in n.names:
                imported_libraries.append(alias.name)
        elif isinstance(n, ast.ImportFrom):
            for alias in n.names:
                imported_libraries.append(f"{n.module}.{alias.name}")
        elif isinstance(n, ast.FunctionDef):
            for subnode in n.body:
                if isinstance(subnode, ast.Import):
                    for alias in subnode.names:
                        imported_libraries.append(alias.name)
                elif isinstance(subnode, ast.ImportFrom):
                    for alias in subnode.names:
                        imported_libraries.append(f"{subnode.module}.{alias.name}")
    return imported_libraries


def create_requirement_file(folder_path):
    with open(folder_path + "/requirements.txt", "r") as f:
        existing_libraries = f.read().splitlines()
    existing_libraries.extend(
        [
            "os",
            "ast",
            "sys",
            "datetime",
            "math",
            "random",
            "csv",
            "json",
            "urllib",
            "itertools",
            "collections",
        ]
    )
    imported_libraries_set = set()
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(subdir, file)
                imported_libraries = get_imported_libraries(file_path)
                imported_libraries_set.update(
                    [
                        library.split(".")[0]
                        for library in imported_libraries
                        if library.split(".")[0] not in existing_libraries
                    ]
                )
    with open(folder_path + "/requirements.txt", "a") as file:
        for package in sorted(imported_libraries_set):
            file.write(package + "\n")
