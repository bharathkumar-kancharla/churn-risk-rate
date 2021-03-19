Step 1:

- Create a Folder for the Project
- Open CMD (command prompt) and navigate to Project Folder using cd (change directory) command
- Type `code .` to open the VSCode from the given folder

Step 2:

- Open the TERMINAL in VSCode and create a virtual enviornment for the project using command:

        conda create -n lose_a_customer python=3.7 -y

  **Note:** `lose_a_customer` enviorment is created using Python 3.7 version and `-y` is given to pass `YES` by default for the command

- Activate the enviornment created

        conda activate lose_a_customer

Step 3: (Optional)

- Created a folders and sub folders from the terminal/from vscode directly for storing the Supporting documents required for the project.

        mkdir Supporting\Images

  **Note:** Reference can be found [here](https://www.windows-commandline.com/create-directory-command-line/) for creating the folders using the terminal

Step 4:

- Create a requirement file either create manually or using `pip freeze` function

        pip freeze > requirements.txt

  - We can add the list of packages required for the project manually and run the requirements file to install all the required packages `or` install all the packages using `pip install <package 1> <package 2>` and run the freeze command to automatically save the installed packages information in requirements.file

  - If requirements are added manually then we need to install the packages using command

        pip install -r requirements.txt

    **Note:** `-r` option is provided to run the `pip install` command `recursively` to install all the packages in requirement file.

Step 5:

- Create a file named `template.py` by clicking on the New file icon next to project name

  - This file will help us to create all the required directories and files for the project manually
  - This action can also done automatically using cookiecutter package. Follow the steps [here](https://drivendata.github.io/cookiecutter-data-science/) to create the project folder structure automatically

  **Information on directories and files to be added**

  - Directories
    - `data/raw` - To store the raw data of the project
    - `data/processed` - To store processed data of the project
    - `notebooks` - To perform EDA and Experimentation on the data
    - `saved_models` - To save all the models of the project
    - `src` - To Store all the required codes to run the project
  - Files
    - `dvc.yaml` - All the stages (i.e., Data Gathering, Data Processing, Training, Evualtion) we are going to implement
    - `params.yaml` - All the configuration and Parameters are added in this file.

  **Note:**

  1. `params.yaml` is created manually to have centralized commands. This is created because, If we have hard coded some elements of code some stage it is hard to find the location to make some changes if project is big. So we maintain centralized location for all the parameters using `params.yaml` file. So that changes will reflect automatically without affecting the code.
  2. `dvc.yaml` can be created manually(preferred) or automatically using command line commands.

     > `yaml` - yet another markup language

     > There are other markup languages like `xml`, `html`, `yml`

- After creating the file run the following command in terminal to create the directories and files

        python templates.py
