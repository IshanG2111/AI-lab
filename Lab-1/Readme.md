# AI-LAB — Lab 1

Short repository README for the Lab-1 exercises and supporting files.

## Project Overview

This workspace contains materials for the AI Lab (Lab-1). It includes small Python scripts, a Jupyter notebook, and markdown notes describing the lab and tasks.

## Repository Structure

```
.
├─ Lab-1/
   └─lab.md               # Lab overview / notes
   └─task.md              # Assignment / task description
│  └─ lab1.ipynb        # Jupyter notebook for Lab-1
```

## Requirements

- Python 3.8 or newer
- Optional: `virtualenv` / `venv` for an isolated environment

There is no `requirements.txt` in the repository. If your lab code requires third-party packages, create a `requirements.txt` and run `pip install -r requirements.txt`.

## Setup (PowerShell)

Create and activate a virtual environment (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
```

If you add dependencies, install them with:

```powershell
pip install -r requirements.txt
```

## Running the code

- Run a single script (example):

```powershell
python .\Lab-1\1.py
```

- Run the Jupyter notebook (recommended for interactive work):

```powershell
pip install jupyter
jupyter notebook .\Lab-1\lab1.ipynb
```

