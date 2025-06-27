# Polars vs Apache Spark

This project uses **Polars**, a fast DataFrame library written in Rust and available in Python. Below is a quick comparison with Apache Spark to highlight why Polars is chosen for this single‑machine workflow.

| Feature | Polars | Apache Spark |
|---------|--------|--------------|
| **Execution Model** | Columnar, in‑memory, optimized for single machine | Distributed computing across clusters |
| **Performance** | Very fast on large datasets that fit in memory; lightweight | Scales horizontally but incurs network and cluster overhead |
| **Language Bindings** | Python (with Rust backend) | Scala, Python (PySpark), Java, R |
| **Best Use Case** | High‑performance processing on a powerful workstation or server | Massive datasets that require distributed resources |
| **Learning Curve** | API similar to pandas, easy to pick up | Requires understanding Spark cluster concepts |

## Why Polars for This Project?
- The data fits on a single machine with ample memory (330 GB RAM).
- Polars has low overhead compared to running a local Spark cluster.
- It integrates smoothly with Python and supports multi‑core execution.

## Getting Started with Polars
1. Install the library in your virtual environment:
   ```bash
   pip install polars
   ```
2. Polars supports eager and lazy execution. For large files, prefer **lazy** loading:
   ```python
   import polars as pl
   df = pl.scan_csv("file.csv")  # lazy
   ```
3. Operations can be chained and executed at the end with `collect()`.

Refer to the [Polars documentation](https://pola.rs/docs/) for detailed tutorials and API references.
