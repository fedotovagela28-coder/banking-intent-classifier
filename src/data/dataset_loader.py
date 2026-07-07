from datasets import DatasetDict, load_dataset

DATASET_NAME = "PolyAI/banking77"

def load_banking77_dataset() -> DatasetDict:
    return load_dataset(DATASET_NAME, trust_remote_code=True)

def get_label_names(dataset: DatasetDict) -> list[str]:
    return dataset["train"].features["label"].names

if __name__ == "__main__":
    dataset = load_banking77_dataset()
    label_names = get_label_names(dataset)

    print(dataset)
    print(dataset["train"][0])
    print(f"Number of labels: {len(label_names)}")
    print(label_names[:10])