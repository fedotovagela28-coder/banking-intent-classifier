from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix

from src.data.dataset_loader import get_label_names, load_banking77_dataset

MODEL_PATH = Path("artifacts") / "tfidf_logreg.joblib"
REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)

def main() -> None:
    dataset = load_banking77_dataset()
    label_names = get_label_names(dataset)

    test_df = pd.DataFrame(dataset["test"])

    label_mapping = dict(enumerate(label_names))

    test_df["true_label_name"] = test_df["label"].map(label_mapping)

    pipeline = joblib.load(MODEL_PATH)
    predictions = pipeline.predict(test_df["text"])

    test_df["predicted_label"] = predictions
    test_df["predicted_label_name"] = test_df["predicted_label"].map(
        dict(enumerate(label_names))
    )

    cm = confusion_matrix(
        test_df["label"],
        predictions,
    )

    fig, ax = plt.subplots(figsize=(18, 18))

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
    )

    display.plot(
        ax=ax,
        xticks_rotation=90,
        colorbar=False,
    )

    plt.title("Baseline Confusion Matrix")
    plt.tight_layout()
    plt.savefig(REPORT_DIR / "baseline_confusion_matrix.png", dpi=200)
    plt.close()

    errors_df = test_df[
        test_df["label"] != test_df["predicted_label"]
    ].copy()

    print(f"Total test samples: {len(test_df)}")
    print(f"Total errors: {len(errors_df)}")
    print(f"Error rate: {len(errors_df) / len(test_df):.4f}")

    error_pairs = (
        errors_df.groupby(
            ["true_label_name", "predicted_label_name"]
        )
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )

    print("\nTop 20 error pairs:")
    print(error_pairs.head(20).to_string(index=False))

    error_pairs.to_csv(
        REPORT_DIR / "baseline_top_error_pairs.csv",
        index=False,
    )

    errors_df[
        [
            "text",
            "true_label_name",
            "predicted_label_name",
        ]
    ].to_csv(
        REPORT_DIR / "baseline_misclassified_examples.csv",
        index=False,
    )

    print("\nError analysis files saved to reports/")


if __name__ == "__main__":
    main()