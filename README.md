# ESNcard-info-formatting
Repository with the Python code used for pre-processing raw ESNcard information, coming directly from the registration form.

## 1. Create the project directory

### 1.1. Create the root folder
Create a folder named `<project_name>`, at some path `~/<prefix_path>` <br>
<br>
**Command `[Command Prompt]`:**
```
mkdir "~/<prefix_path>/<project_name>"
```
**Result `[File directory]`:**
```
<prefix_path>/
        └── <project_name>/
```

### 1.2. Create (local) data folders
Create two folders named `Input_data` and `Output_data`, inside the root folder, `~/<prefix_path>/<project_name>` <br> 
<br>
**Command `[Command Prompt]`:**
```
mkdir "~/<prefix_path>/<project_name>/Input_data"
mkdir "~/<prefix_path>/<project_name>/Output_data"
```
**Result `[File directory]`:**
```
<prefix_path>/
        └── <project_name>/
                ├── Input_data/
                └── Output_data/
```
Make sure the raw ESNcard holders' information is stored inside folder `Input_data`. You can change the paths and names in the scripts, in order to make sure the names are compatible with the paths. The output, pre-processed, data will be stored inside folder `Output_data`.


### 1.2. Clone the GitHub repository
Clone this repository to a folder `Repo`, inside the root folder, `~/<prefix_path>/<project_name>` <br>
<br>
**Command `[Command Prompt]`:**
```
git clone "https://github.com/estebanhramirez/ESNcard-info-formatting.git" "~/<prefix_path>/<project_name>/Repo"
```
**Result `[File directory]`:**
```
<prefix_path>/
        └── <project_name>/
                    ├── Input_data/
                    ├── Output_data/
                    └── Repo/
                          ├── README.md
                          └── ...
```
<br>
<br>


## 2. Set-up the virtual environment

### 2.1. Create the virtual environment
Create a new folder name `venv` inside the repository folder, `~/<prefix_path>/<project_name>/Repo`, with an isolated and self-contained virtual environment <br>
<br>
**Command `[Command Prompt]`:**
```
python3.12 -m venv "~/<prefix_path>/<project_name>/Repo/venv"
```

### 2.2. Activate the virtual environment
**Command `[Command Prompt]`:**
```
source "~/<prefix_path>/<project_name>/Repo/venv/bin/activate"
```
or (in Windows)
```
~\<prefix_path>\<project_name>\Repo\venv\Scripts\activate.bat
```
We can deactivate the virtual environment using `deactivate.bat`.
<br>
<br>


## 3. Install the required libraries
**Command `[Command Prompt]`:**
```
pip install -r "~/<prefix_path>/<project_name>/Repo/requirements.txt"
```

