import os

# Creating a list of directories which are required for the project
dirs = [
    # As windows use / to join the directories and linux based OS uses \ to join
    # To avoid issues it is recommended to specify the directories using os.path.join
    "data_given",
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src",
]

for dir_ in dirs:
    # exist_ok is set True, to avoid errors even if folder already exists
    os.makedirs(dir_, exist_ok=True)
    # To add a .gitkeep file in each created folder
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass

# Create a required files (i.e., )
files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    # __init__.py will convert the src folder into package
    os.path.join("src", "__init__.py"),
    # "README",
]

for file_ in files:
    # Simply open the files and saving it
    with open(file_, "w") as f:
        pass