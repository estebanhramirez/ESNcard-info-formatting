# Local-OLLAMA-Chatbot
Local code for a OLLAMA Chatbot

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

## 4. Set-up Ollama API

### 4.1. Install Ollama
Install Ollama in your local laptop<br>
<br>
**Command `[PowerShell]`:**
```
irm https://ollama.com/install.ps1 | iex
```

### 4.2. Pull Ollama models
Download the model `llama2`<br>
<br>
**Command `[Command Prompt | PowerShell]`:**
```
ollama pull llama2
```
Check that the model was downloaded<br>
<br>
**Command `[Command Prompt | PowerShell]`:**
```
ollama list
```

### 4.3. Start the Ollama HTTP Server/API
**Command `[Command Prompt | PowerShell]`:**
```
ollama serve
```

## 5. Set-up LocalTunnel
Once Node.js installed, LocalTunnel lets us create a public link instantly with a single command

### 5.1. Install Node.js®
Install Node.js®'s prebuilt from the official website: [Node.js®](https://nodejs.org/en/download).

### 5.2. Install LocalTunnel
Once Node.js installed, install LocalTunnel
**Command `[Command Prompt]`:**
```
npm install -g localtunnel
```

### 5.3. Run the Python server
Run the FastAPI app to handle prompts and communicate with the local LLM<br>
<br>
**Command `[Command Prompt]`:**
```
python "~/<prefix_path>/<project_name>/Repo/app.py"
```

### 5.4. Launch LocalTunnel
Open a second terminal window and direct LocalTunnel to point to your FastAPI port (8080)<br>
<br>
**Command `[Command Prompt]`:**
```
lt --port 8080
```
LocalTunnel will output a public HTTPS URL.

## 6. Test the end-to-end pipeline
(Before creating the LocalTunnel: test the localhost)
```
curl -X POST http://127.0.0.1:8080/generate -H "Authorization: Bearer <API_KEY>" -H "Content-Type: application/json" -d "{\"prompt\": \""What are you?\"}"
```
(After creating the LocalTunnel: test the public online link)
```
curl -X POST https://olive-donuts-add.loca.lt/generate -H "Authorization: Bearer <API_KEY>" -H "Content-Type: application/json" -H "bypass-tunnel-reminder: true" -d "{\"prompt\": \"What are you?\"}"
```

