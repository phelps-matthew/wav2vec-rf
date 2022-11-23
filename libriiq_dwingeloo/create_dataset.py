"""
Create LibriIQ-Dwingeloo dataset by unpacking Kaggle archive.zip and partitioning .raw
files into .npy sequences.
"""

import random
from pathlib import Path

import numpy as np
from tqdm import tqdm

SAMPLE_FREQ = 48000
SAMPLE_TIME = 5
SAMPLES = SAMPLE_TIME * SAMPLE_FREQ


def _raw_to_64(datafile):
    """
    Convert 16 bit IQ (32 bit sample = 16 bit I, 16 bit Q) to np.complex64.
    Output is composed of 2 32-bit floats, v(t) = inphase(t) + i quadrature(t)
    """
    return np.fromfile(datafile, np.int16).astype(np.float32).view(np.complex64)


def _pad_to_sample_len(x):
    """Pad end of array with symmetric signal such that x % sample_len = 0"""
    padding = SAMPLES - (len(x) % SAMPLES)
    x = np.pad(x, (0, padding), "symmetric")
    x[-padding:] = x[-padding:].conjugate()
    return x


def raw_to_iq_2ch(datafile):
    """Convert .raw binary sample to two channel float32 IQ array
    Returns:
        np.float32 of shape (n_samples, 2, sample_len)
    """
    # convert from binary 16 bit IQ to complex 64
    x = _raw_to_64(datafile)
    # pad end of array with symmetric signal
    x = _pad_to_sample_len(x)
    # split array according to sample length
    x = np.array(np.array_split(x, len(x) // SAMPLES))
    # convert complex64 to two channel array
    iq = np.stack([np.real(x), np.imag(x)], axis=1)
    return iq


def write_npy_samples(root, target_root, dry_run=False, glob_key="*.raw", shuffle=True):
    """load each .raw file, process, and write samples as .npy's
    Returns:
        list of sample paths for creating labels json
    """
    paths = [p for p in root.glob(glob_key)]
    label_paths = []
    for p in tqdm(paths):
        iq = raw_to_iq_2ch(p)
        for i, x in enumerate(iq):
            outfile = target_root / f"{p.stem}_{i:04d}.npy"
            label_paths.append(outfile)
            if not dry_run:
                with open(outfile, "wb") as f:
                    np.save(f, x)
    if shuffle:
        random.shuffle(label_paths)  # in place
    return label_paths


if __name__ == "__main__":
    import argparse
    import zipfile
    import shutil

    parser = argparse.ArgumentParser(
        description="Create dataset. Requires archive.zip from Kaggle download.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--source",
        type=str,
        default="./archive.zip",
        help="Path to archive.zip from Kaggle download",
    )
    args = parser.parse_args()
    source = Path(args.source).expanduser()
    target_dir = Path(__file__).resolve().parent  # libriiq_dwingeloo directory

    # unzip archive.zip
    print(f"📦 Unzipping {source} to {target_dir}")
    # with zipfile.ZipFile(source, 'r') as f:
    #    f.extractall(target_dir)

    # Typical ASR uses 10-15 secs for translation and 2-4 secs for tasks like speaker id.
    # We will use 5 secs.
    raw_dir = target_dir / "raw"
    samples_dir = target_dir / "samples"
    samples_dir.mkdir(exist_ok=True)

    # load each .raw file, process, and write samples as .npy's
    print("🔢 Splitting .raw IQ observations into .npy sequences")
    label_paths = write_npy_samples(
        raw_dir,
        samples_dir,
        dry_run=False,
        shuffle=True,
        glob_key="*.raw",
    )

    # remove 14.6 GB ./raw directory
    print("🧹 Cleaning up")
    shutil.rmtree(raw_dir)

    print("✅ Done")
