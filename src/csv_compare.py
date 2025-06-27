import sys
import polars as pl


def validate_headers(path1: str, path2: str) -> list[str]:
    header1 = pl.read_csv(path1, n_rows=0).columns
    header2 = pl.read_csv(path2, n_rows=0).columns
    if header1 != header2:
        raise ValueError("CSV headers differ")
    return header1


def compare_csvs(file1: str, file2: str, output_path: str) -> None:
    columns = validate_headers(file1, file2)
    df1 = pl.scan_csv(file1)
    df2 = pl.scan_csv(file2)
    df2 = df2.select(columns)  # reorder columns

    df1 = df1.rename({c: f"{c}_file1" for c in columns if c != "hash_id"})
    df2 = df2.rename({c: f"{c}_file2" for c in columns if c != "hash_id"})

    join_df = df1.join(df2, on="hash_id", how="outer")

    mismatches = []
    for col in columns:
        if col == "hash_id":
            continue
        diff = (
            join_df
            .filter(pl.col(f"{col}_file1") != pl.col(f"{col}_file2"))
            .select(
                [
                    pl.col("hash_id"),
                    pl.lit(col).alias("column"),
                    pl.col(f"{col}_file1").cast(pl.Utf8).alias("old_value"),
                    pl.col(f"{col}_file2").cast(pl.Utf8).alias("new_value"),
                ]
            )
        )
        mismatches.append(diff)

    mismatch_df = pl.concat(mismatches) if mismatches else pl.DataFrame()

    non_hash_columns = [c for c in columns if c != "hash_id"]
    first_col = non_hash_columns[0]

    missing_in_file1 = (
        join_df.filter(pl.col(f"{first_col}_file1").is_null())
        .select(
            [
                pl.col("hash_id"),
                pl.lit("missing_in_file1").alias("column"),
                pl.lit(None).cast(pl.Utf8).alias("old_value"),
                pl.lit(None).cast(pl.Utf8).alias("new_value"),
            ]
        )
    )

    missing_in_file2 = (
        join_df.filter(pl.col(f"{first_col}_file2").is_null())
        .select(
            [
                pl.col("hash_id"),
                pl.lit("missing_in_file2").alias("column"),
                pl.lit(None).cast(pl.Utf8).alias("old_value"),
                pl.lit(None).cast(pl.Utf8).alias("new_value"),
            ]
        )
    )

    result = pl.concat([mismatch_df, missing_in_file1, missing_in_file2])
    result.collect().write_csv(output_path)


def main(argv: list[str]) -> None:
    if len(argv) != 4:
        print("Usage: python csv_compare.py <file1.csv> <file2.csv> <output.csv>")
        sys.exit(1)
    _, file1, file2, output_path = argv
    try:
        compare_csvs(file1, file2, output_path)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv)
