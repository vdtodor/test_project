# CSV Comparison Project Plan

This document outlines the high‑level plan for building a tool that compares two large CSV files containing more than 20 million rows each. The tool will run on a powerful single machine (330 GB RAM, 24+ cores) using the Python language and the [Polars](https://pola.rs) library.

## Goals
- Ensure the CSV headers match in name (order can differ).
- Efficiently compare records by `hash_id` and capture differences.
- Produce logs of mismatched records and records missing from either file.
- Handle errors without interrupting processing unless absolutely necessary.

## Steps
1. **Environment Setup**
   - Install Python using `pyenv` and create a virtual environment.
   - Install required Python packages (`polars` and other dependencies).

2. **Input Validation**
   - Verify that both CSV files contain the same columns (case‑sensitive by name).
   - Fail early with a clear message if headers differ.

3. **Data Loading**
   - Load both CSV files into Polars DataFrames using lazy execution to reduce memory consumption.
   - Reorder columns to a consistent ordering for comparison.

4. **Comparison Logic**
   - Join the DataFrames on `hash_id`.
   - For each joined row, identify columns with differing values and record the old/new values.
   - Capture rows that appear in one file but not the other.

5. **Logging and Output**
   - Write comparison results to an output file (e.g., `comparison_results.csv`).
   - Print errors and progress information to standard output.
   - Defer any formatting or presentation of results until processing completes.

6. **Testing**
   - Create small sample CSV files to verify the tool’s behavior.
   - Ensure the script handles large input sizes and uses available cores.

## Future Enhancements
- Consider parallelizing file reading and comparison using Polars’ built‑in multicore support.
- Add command‑line arguments to configure input paths and output location.

