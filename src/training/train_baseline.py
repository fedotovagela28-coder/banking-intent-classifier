from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.pipeline import Pipeline

from src.data.dataset_loader import get_label_names, load_banking77_dataset


ARTIFACTS_DIR = Path("artifacts")
MODEL_PATH = ARTIFACTS_DIR / "tfidf_logreg.joblib"
REPORT_PATH = Path("reports") / "baseline_classification_report.txt"


def main() -> None:
    dataset = load_banking77_dataset()
    label_names = get_label_names(dataset)

    train_df = pd.DataFrame(dataset["train"])
    test_df = pd.DataFrame(dataset["test"])

    x_train = train_df["text"]
    y_train = train_df["label"]

    x_test = test_df["text"]
    y_test = test_df["label"]

    pipeline = Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    lowercase=True,
                    ngram_range=(1, 2),
                    min_df=2,
                    max_features=50_000,
                    sublinear_tf=True,
                ),
            ),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    class_weight="balanced",
                    n_jobs=-1,
                ),
            ),
        ]
    )

    print("Training baseline model...")
    pipeline.fit(x_train, y_train)

    predictions = pipeline.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)
    macro_f1 = f1_score(y_test, predictions, average="macro")
    weighted_f1 = f1_score(y_test, predictions, average="weighted")

    print(f"Accuracy: {accuracy:.4f}")
    print(f"Macro F1: {macro_f1:.4f}")
    print(f"Weight F1: {weighted_f1:.4f}")

    report = classification_report(
        y_test,
        predictions,
        target_names=label_names,
        digits=4,
    )

    print("\nClassification report:")
    print(report)

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(pipeline, MODEL_PATH)
    REPORT_PATH.write_text(report, encoding="utf-8")

    print(f"\nModel saved to: {MODEL_PATH}")
    print(f"Report saved to: {REPORT_PATH}")

if __name__ == "__main__":
    main()