# Qttp
Qttp search engine 
# Qttp Search Engine

## Overview
Qttp, developed by Karlfiner-Robotiken, is a quantum web search engine that integrates data from multiple existing search engines to provide optimized search results.

## Features
- Integrates results from Google, Bing, and DuckDuckGo.
- Uses Flask for the web interface.
- Provides a simple and clean user interface.
- Optimizes search results using quantum algorithms.

## Setup

### Prerequisites
- Python 3.6+
- Pip (Python package manager)

### Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/Karlfiner-Robotiken/qttp.git
    cd qttp
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    python app.py
    ```

### Directory Structure
- `app.py`: Main application file.
- `search_engine.py`: Contains the logic for integrating search engines.
- `templates/`: Directory for HTML templates.
    - `index.html`: Home page template.
    - `results.html`: Results page template.
- `requirements.txt`: List of dependencies.

## Usage

### Running Locally
To run the application locally, navigate to the project directory and execute:
```bash
python app.py
