"""Dataset class to be extended by dataset-specific classes."""
from pathlib import Path
import argparse
import os

from similarity_search import util


class Dataset:
    """Simple abstract class for datasets."""

    @classmethod
    def data_dirname(cls):
        return Path(__file__).resolve().parents[2] / "data"

    def load_or_generate_data(self):
        pass


def _download_raw_dataset(metadata):
    if os.path.exists(metadata["filename"]):
        return
    print(f"Downloading raw dataset from {metadata['url']}...")
    util.download_url(metadata["url"], metadata["filename"])


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--subsample_fraction", type=float, default=None, help="If given, is used as the fraction of data to expose.",
    )
    return parser.parse_args()