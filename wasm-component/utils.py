import io
import numpy as np
import regex as re


def load_data(data_str: str):
    #print("Processing input string as dataset...")
    # Convert string to a file-like object
    data_io = io.StringIO(data_str)

    # Load data using np.genfromtxt
    data = np.genfromtxt(
        data_io,
        delimiter=",",
        dtype=None,
        names=True,
        encoding="utf-8",
        missing_values="",
    )
    return data


def analyze_data(data):
    # Separate columns by type
    column_names = data.dtype.names
    report = {}

    # Regex to identify columns like ID
    index_column_pattern = re.compile(r"(?i)^id$")  # Match ID case-insensitively

    for col in column_names:
        # Skip columns matching the regex
        if index_column_pattern.search(col):
            #print(f"Index column detected: '{col}' - Not processed.")
            continue

        col_data = data[col]
        if np.issubdtype(col_data.dtype, np.number):
            report[col] = {
                "mean": np.nanmean(col_data),
                "min": np.nanmin(col_data),
                "max": np.nanmax(col_data),
                "std_dev": np.nanstd(col_data),
            }
        else:
            unique_values, counts = np.unique(col_data, return_counts=True)
            report[col] = {
                "unique_values": unique_values.tolist(),
                "counts": counts.tolist(),
            }
    return report