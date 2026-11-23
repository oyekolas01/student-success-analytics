from pathlib import Path
import pandas as pd

RAW = Path(__file__).resolve().parent.parent / "data" / "raw"

TABLES = {
    "courses": ["code_module", "code_presentation"],
    "assessments": ["id_assessment"],
    "studentInfo": ["code_module", "code_presentation", "id_student"],
    "studentRegistration": ["code_module", "code_presentation", "id_student"],
    "studentAssessment": ["id_assessment", "id_student"],
    "vle": ["id_site"],
    "studentVle": [
        "code_module",
        "code_presentation",
        "id_student",
        "id_site",
        "date",
    ],   # keep this last, it is ~10 million rows
}

def profile(df, name, key_cols):
    print(f"\n=== {name} ===")
    print(f"Shape: {df.shape}")
    print("\nDtypes:")
    print(df.dtypes)

    null_counts = df.isna().sum()
    null_summary = pd.DataFrame(
        {
            "null_count": null_counts,
            "null_pct": null_counts / len(df) * 100,
        }
    )
    print("\nNull values:")
    print(null_summary)

    duplicate_rows = df.duplicated(subset=key_cols, keep=False).sum()
    excess_duplicate_rows = df.duplicated(subset=key_cols).sum()
    print(f"\nRows with a non-unique key on {key_cols}: {duplicate_rows}")
    print(f"Excess rows beyond the first per key: {excess_duplicate_rows}")

if __name__ == "__main__":
    for name, key_cols in TABLES.items():
        df = pd.read_csv(RAW / f"{name}.csv")
        profile(df, name, key_cols)