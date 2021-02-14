"""
Geological Image Similarity dataset.  Download from AWS.
"""
import os
import toml
import zipfile

from similarity_search.datasets.dataset import _download_raw_dataset, Dataset, _parse_args


SAMPLE_TO_BALANCE = True

RAW_DATA_DIRNAME = Dataset.data_dirname() / "raw" / "geoimage"
METADATA_FILENAME = RAW_DATA_DIRNAME / "metadata.toml"

ESSENTIALS_FILENAME = RAW_DATA_DIRNAME / "geological_similarity.zip"


class GeoimageDataset(Dataset):
    """
    Geological Similarity Image
    """

    def __init__(self, subsample_fraction: float = None):
        if not os.path.exists(ESSENTIALS_FILENAME):
            _download_and_process_geoimage()


def _download_and_process_geoimage():
    metadata = toml.load(METADATA_FILENAME)
    curdir = os.getcwd()
    os.chdir(RAW_DATA_DIRNAME)
    _download_raw_dataset(metadata)
    _process_raw_dataset(metadata["filename"])
    os.chdir(curdir)


def _process_raw_dataset(filename: str):
    print("Unzipping Geological Similarity Data...")
    with zipfile.ZipFile(filename, "r") as zip_ref:
        zip_ref.extractall(RAW_DATA_DIRNAME)


def main():
    args = _parse_args()
    dataset = GeoimageDataset(subsample_fraction=args.subsample_fraction)
    dataset.load_or_generate_data()


if __name__ == "__main__":
    main()



