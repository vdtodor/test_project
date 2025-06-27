# Test Project Python Setup

This repository now contains a minimal Python project.
See the files in the `docs/` directory for the project plan, task checklist, and setup instructions.

## Requirements

- [pyenv](https://github.com/pyenv/pyenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

## Setup

1. Install `pyenv` and `pyenv-virtualenv`.
2. Run `pyenv install $(cat .python-version)` to install the required Python version.
3. Create a virtual environment:

   ```bash
   pyenv virtualenv $(cat .python-version) test_project-env
   pyenv local test_project-env
   ```
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the example script:

```bash
python src/main.py
```

To compare two CSV files using Polars:

```bash
python src/csv_compare.py sample_data/file1.csv sample_data/file2.csv comparison_results.csv
```

To run a quick performance check on large, randomly generated datasets:

```bash
python src/performance_check.py --rows 1000000 --threads 8
```
