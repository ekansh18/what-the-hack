# what-the-hack

Repository for the hackathon

# Basic commands for the FastAPI App

---

## Prerequisites

| Tool    | Version | Download                      |
| ------- | ------- | ----------------------------- |
| Python  | 3.11+   | https://python.org/downloads  |
| VS Code | any     | https://code.visualstudio.com |

---

## First-Time Setup

Do this once when you first clone the project.

### 1. Clone the repo

```bash
git clone https://github.com/ekansh18/what-the-hack.git
```

### 2. Create a virtual environment

```bash
python3 -m venv myenv
```

### 3. Activate the virtual environment

**Mac / Linux**

```bash
source myenv/bin/activate
```

**Windows (Command Prompt)**

```bash
.venv\Scripts\activate
```

**Windows (PowerShell)**

```bash
.venv\Scripts\Activate.ps1
```

You'll know it worked when you see `(.venv)` at the start of your terminal line.

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the App

Every time you work on the project, do this:

```bash
# Step 1 — activate the virtual environment (if not already active)
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate           # Windows

# Step 2 — start the server
uvicorn main:app --reload
```

The server runs at **http://localhost:8000**

| URL                          | What it is                                   |
| ---------------------------- | -------------------------------------------- |
| http://localhost:8000        | Your API                                     |
| http://localhost:8000/docs   | Interactive Swagger UI — test endpoints here |
| http://localhost:8000/health | Health check                                 |

To stop the server: `Ctrl+C`

---

## Adding a New Package

```bash
pip install <package-name>
pip freeze > requirements.txt    # save it so teammates get it too
```

---

## Project Structure

```
my-fastapi-app/
├── myenv/               ← virtual environment (do not commit)
├── .vscode/
│   └── launch.json      ← debugger config
├── main.py              ← FastAPI app
├── requirements.txt     ← Python dependencies
└── .gitignore
```

---

## Recommended VS Code Extensions

Install these from the Extensions panel (`Ctrl+Shift+X`):

- **Python** — Microsoft
- **Pylance** — type checking and autocomplete
- **Ruff** — linting and formatting
- **REST Client** — test API calls directly in VS Code from `test.http`

---

## Common Commands

| What                             | Command                                 |
| -------------------------------- | --------------------------------------- |
| Activate virtual env (Mac/Linux) | `source .venv/bin/activate`             |
| Activate virtual env (Windows)   | `.venv\Scripts\activate`                |
| Start server                     | `uvicorn main:app --reload`             |
| Start on a different port        | `uvicorn main:app --reload --port 8080` |
| Install a package                | `pip install <package>`                 |
| Save dependencies                | `pip freeze > requirements.txt`         |
| Install from requirements        | `pip install -r requirements.txt`       |
| Stop server                      | `Ctrl+C`                                |
| Deactivate virtual env           | `deactivate`                            |
