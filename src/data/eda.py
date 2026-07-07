from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt

from src.data.dataset_loader import get_label_names, load_banking77_dataset


def main() -> None:
    dataset = load_banking77_dataset()
    label_names = get_label_names(dataset)

    train_df = pd.DataFrame(dataset["train"])
    test_df = pd.DataFrame(dataset["test"])

    train_df["label_name"] = train_df["label"].apply(lambda x: label_names[x])
    test_df["label_name"] = test_df["label"].apply(lambda x: label_names[x])

    train_df["text_length"] = train_df["text"].str.len()

    class_counts = (
        train_df["label_name"]
        .value_counts()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(16, 8))
    class_counts.plot(kind="bar")

    plt.title("Number of samples for each intent")
    plt.xlabel("Intent")
    plt.ylabel("Number of samples")

    plt.xticks([], [])

    plt.tight_layout()

    plt.savefig("reports/figures/class_distribution.png")
    plt.close()

    plt.figure(figsize=(10, 6))

    plt.hist(train_df["text_length"], bins=40)

    plt.title("Distribution of text lengths")
    plt.xlabel("Text length (Characters)")
    plt.ylabel("Number of samples")

    plt.tight_layout()

    plt.savefig("reports/figures/text_length_distribution.png")
    plt.close()

    print("Train shape:", train_df.shape)
    print("Test shape:", test_df.shape)
    print("Number of labels:", len(label_names))

    print("\nTop 10 classes:")
    print(train_df["label_name"].value_counts().head(10))

    print("\nText length statistics:")
    print(train_df["text_length"].describe())

    print("\nPercentiles:")

    for p in [50, 75, 90, 95, 99]:
        value = train_df["text_length"].quantile(p/100)
        print(f"{p}%: {value:.0f} characters")

    print("\nExample:")
    print(train_df.sample(1, random_state=42)[["text", "label_name"]])

    label_counts = Counter(train_df["label_name"])
    print("\nMin class size:", min(label_counts.values()))
    print("\nMax class size:", max(label_counts.values()))

if __name__ == "__main__":
    main()