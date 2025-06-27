"""Simple performance check for the CSV comparison tool."""

from __future__ import annotations

import argparse
import os
import tempfile
import time

# set POLARS_MAX_THREADS before importing polars
parser = argparse.ArgumentParser(description="Run performance comparison.")
parser.add_argument("--rows", type=int, default=1_000_000, help="Number of rows in generated CSVs")
parser.add_argument("--threads", type=int, default=None, help="Number of Polars threads to use")
args = parser.parse_args()

if args.threads is not None:
    os.environ["POLARS_MAX_THREADS"] = str(args.threads)

import polars as pl
from csv_compare import compare_csvs


def make_data(path: str, start: int, end: int, offset: int = 0) -> None:
    df = pl.DataFrame(
        {
            "hash_id": list(range(start, end)),
            "name": [f"name{i}" for i in range(start, end)],
            "value": list(range(start + offset, end + offset)),
        }
    )
    df.write_csv(path)


with tempfile.TemporaryDirectory() as tmpdir:
    file1 = os.path.join(tmpdir, "file1.csv")
    file2 = os.path.join(tmpdir, "file2.csv")

    make_data(file1, 0, args.rows)
    make_data(file2, 0, args.rows, offset=1)

    out_path = os.path.join(tmpdir, "result.csv")

    start = time.perf_counter()
    compare_csvs(file1, file2, out_path)
    duration = time.perf_counter() - start

    print(
        f"Compared {args.rows} rows in {duration:.2f}s using {pl.thread_pool_size()} threads"
    )
