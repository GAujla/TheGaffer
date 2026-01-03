# TheGaffer

**TheGaffer** is an aspirational AI-powered assistant designed for **Fantasy Premier League (FPL)**. By leveraging Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG), it aims to provide data-driven insights to help managers optimize their squads and win their mini-leagues.

---

## Project Architecture

The project follows a decoupled architecture, separating the AI processing logic from the user interface.

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/) – A high-performance web framework that serves as the API layer hosting the Large Language Model.
* **Frontend:** [Streamlit](https://streamlit.io/) – An interactive web interface for a seamless chat experience.
* **Package Manager:** [uv](https://docs.astral.sh/uv/) – An extremely fast Python package manager used for dependency management and environment isolation.



---

## Getting Started

### Prerequisites
Ensure you have `uv` installed. If you need to install a specific Python version or the tool itself, refer to the [official uv installation guide](https://docs.astral.sh/uv/guides/install-python/#installing-a-specific-version).

### Running the Application
To run the full stack, you must start the backend server before the frontend client. Follow these steps in order:

#### 1. Start the Backend (API)
Open a terminal window and execute:
```bash
uv run uvicorn main:app --reload
```


#### 2. Start the Frontend
Open a terminal window and execute:
```bash
uv run streamlit run client.py
```
