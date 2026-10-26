# ESNcard-info-formatting
Repository with the Python code used for pre-processing raw ESNcard information, coming directly from the registration form.

## 1. Create the project directory

### 1.1. Create the root folder
Create a folder named `<project_name>`, at some path `<prefix_path>` <br>
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
Create two folders named `input_data` and `output_data`, at path `<prefix_path>/<project_name>` <br> 
<br>
**Command `[Command Prompt]`:**
```
mkdir "~/<prefix_path>/<project_name>/input_data"
mkdir "~/<prefix_path>/<project_name>/output_data"
```
**Result `[File directory]`:**
```
<prefix_path>/
        ├── input_data/
        ├── output_data/
        └── <project_name>/
```


### 1.2. Clone the GitHub repository
Clone this repository inside the root folder <br>
<br>
**Command `[Command Prompt]`:**
```
git clone "https://github.com/estebanhramirez/Local-OLLAMA-Chatbot.git" "~/<prefix_path>/<project_name>/Repo"
```
**Result `[File directory]`:**
```
<prefix_path>/
        └── <project_name>/
                    └── Repo/
                          ├── README.md
                          └── ...
```

## 2. Set-up the virtual environment

### 2.1. Create the virtual environment
Create a new folder name `venv` inside the root folder, `<project_name>`, with the isolated and self-contained virtual environment <br>
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

## 3. Install the required libraries
**Command `[Command Prompt]`:**
```
pip install -r "~/<prefix_path>/<project_name>/Repo/requirements.txt"
```
(After creating the LocalTunnel: test the public online link)
```
curl -X POST https://olive-donuts-add.loca.lt/generate -H "Authorization: Bearer <API_KEY>" -H "Content-Type: application/json" -H "bypass-tunnel-reminder: true" -d "{\"prompt\": \"What are you?\"}"
```

