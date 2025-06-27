# Implementation Tasks

This document lists concise tasks for building the CSV comparison tool.

## 1. Environment Setup
- [ ] Install `pyenv` and `pyenv-virtualenv`.
- [ ] Install Python using `.python-version`.
- [ ] Create and activate a virtual environment.
- [ ] Install requirements from `requirements.txt` including `polars`.

## 2. Input Validation
- [ ] Read CSV headers and ensure both files share identical column names.
- [ ] Exit with a clear error if headers differ in name or count.

## 3. Data Loading
- [ ] Load both CSV files lazily using Polars `scan_csv`.
- [ ] Reorder columns consistently before comparison.

## 4. Comparison
- [ ] Join DataFrames on `hash_id`.
- [ ] Identify rows that exist only in one file.
- [ ] For matching rows, log columns whose values differ along with old and new values.

## 5. Logging and Output
- [ ] Write mismatched and missing rows to a result file.
- [ ] Log errors to standard output without interrupting processing unless a fatal error occurs.

## 6. Testing
- [ ] Create small sample datasets to validate the tool.
- [ ] Verify performance on large files using multiple cores.
