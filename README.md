# AI Tutor for Corporate Training Assistant

A Streamlit-based portfolio prototype for workplace learning, course browsing, and training analytics.

## Features

- **Overview:** Illustrative training metrics and dashboard summaries.
- **Course Library:** A synthetic catalogue of training courses.
- **Training Management:** Sample training-management views.
- **About:** Project information.
- **Configuration utilities:** Reads optional local environment settings without displaying API key values.

## Technology stack

- Python 3.13
- Streamlit
- pandas and Plotly
- python-dotenv
- pytest

Additional packages are pinned in `requirements.txt`.

## Prerequisites

Install Python 3.13 and Git for Windows. Run the following commands from the project directory in PowerShell.

## Installation

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run the application

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open the local URL displayed by Streamlit, usually `http://localhost:8501`.

## Run tests

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

The initial configuration test suite contains five tests.

## API configuration and secrets

The current dashboard does not make an OpenAI API request. Optional settings are handled by `config.py`.

If local configuration is needed, copy `.env.example` to `.env` and edit the local file privately. Never commit `.env`, expose API keys in screenshots, or paste credentials into source control. A configured key does not establish that the key is valid, a model is available, or billing is enabled.

## Current scope and limitations

This is a development and portfolio prototype using synthetic data. The current implementation does not provide:

- Functional AI tutoring or live model integration
- Real employee accounts or authentication
- Enforced role-based access control
- Persistent, database-backed training records
- Production security, audit controls, or deployment hardening

Do not enter real employee information or confidential company data.

## Suggested future work

1. Add secure authentication and role-based permissions.
2. Implement persistent course and training records.
3. Integrate an AI tutor with appropriate privacy and cost controls.
4. Add validated progress tracking and reporting.
5. Expand automated tests and security reviews.
6. Prepare a production deployment process.

## Project status

Initial working prototype. Features described under future work are plans, not claims about the current implementation.
