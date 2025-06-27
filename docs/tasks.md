# Implementation Tasks

This document lists concise tasks for building the CSV comparison tool.

## 1. Environment Setup
- [x] Install `pyenv` and `pyenv-virtualenv`.
- [x] Install Python using `.python-version`.
- [x] Create and activate a virtual environment.
- [x] Install requirements from `requirements.txt` including `polars`.

## 2. Input Validation
- [x] Read CSV headers and ensure both files share identical column names.
- [x] Exit with a clear error if headers differ in name or count.

## 3. Data Loading
- [x] Load both CSV files lazily using Polars `scan_csv`.
- [x] Reorder columns consistently before comparison.

## 4. Comparison
- [x] Join DataFrames on `hash_id`.
- [x] Identify rows that exist only in one file.
- [x] For matching rows, log columns whose values differ along with old and new values.

## 5. Logging and Output
- [x] Write mismatched and missing rows to a result file.
- [x] Log errors to standard output without interrupting processing unless a fatal error occurs.

## 6. Testing
- [x] Create small sample datasets to validate the tool.
- [x] Verify performance on large files using multiple cores.
