from pathlib import Path
import pandas as pd

RAW = Path(__file__).resolve().parent.parent / "data" / "raw"


def clean_student_assessment(df):
    df = df.copy()
    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    return df


if __name__ == "__main__":
    df = pd.read_csv(RAW / "studentAssessment.csv")
    cleaned = clean_student_assessment(df)
    print(cleaned["score"].dtype)
    print(cleaned["score"].isna().sum())
