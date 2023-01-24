# 📡 wav2vec-rf
wav2vec-RF: Applying ASR to Raw Radio Signals Intercepted From Low Earth Orbit Satellites (Official Repo)

Full release coming soon.


## LibriIQ-Dwingeloo Dataset
The LibriIQ-Dwingeloo dataset contains RF observations of low Earth orbit (LEO) satellite transmissions in the ultra-high-frequency (UHF) band sourced from https://charon.camras.nl/public/satnogs/. Each observation comprises an RF IQ (in-phase, quadrature) signal sampled at 48 kHz. LibriIQ-Dwingeloo spans 44 distinct satellites, 7 modulation types, and 100 total observations.

For seamless integration into ASR-based architectures, LibriIQ-Dwingeloo is designed to mimic the LibriSpeech ASR corpus. Taking account of the 48kHz sample rate, each RF IQ observation is split into a series of sequences with each sequence having an approximately equal number of samples as the LibriSpeech sequences used in wav2vec2.

### Download
Download LibriIQ-Dwingeloo from https://www.kaggle.com/datasets/matthewphelps/libriiq-dwingeloo. Requires registering a Kaggle account (free). Output is a 5 GB `archive.zip` file. (Link appears broken as of 2023/01/23. Reuploading dataset on 2023/01/24.)

### Create
Extract zipped contents and partition dataset, resulting in 28 GB of RF IQ sample sequences.
```python
# requires numpy and tqdm
# alteratively, you can install the wav2vec-rf library as in #wav2vec-rf Installation
pip install numpy tqdm

# from repository directory
python ./libriiq_dwingeloo/create_dataset.py
```

### Format
Acronyms: SOI = signal of interest, AMC = automatic modulation classification, SEI = signal emitter identification.

LibriIQ-Dwingeloo contains 15240 RF IQ sequences, each having a duration 5 seconds. Among these, 6262 sequences contrain the target SOI. The `soi_*.json` files specify a 90/10 train/test split followed by a 80/20 train/val split for the task of SOI detection. Due to dataset imbalance, four-way random stratified sub-sampling can be performed using the provided seeds. Similarly, `cls_*.json` specify the train/val/test splits for performing AMC and SEI on the subset of sequences that contain the SOI.
```
libriiq_dwingeloo
├── samples  				# directory of numpy float32 RF IQ sequences of shape (2, 240000)
│   ├── iq_1452111_0000.npy
│   ├── ...
│   └── iq_6291503_0142.npy
├── annot.json  			# global annotation json containing all metadata for each sequence
├── cls_test_10.json  			# SOI sequence paths for held-out test set, used for SEI and AMC
├── cls_train_80_val_20_seed_123.json   # SOI sequence paths of 80/20 train/val split, seed 123, used for SEI and AMC
├── cls_train_80_val_20_seed_1337.json
├── cls_train_80_val_20_seed_271.json
├── cls_train_80_val_20_seed_42.json
├── soi_paths.json                      # sequence paths containing SOI
├── soi_test_10.json                    # sequence paths for held-out test set, used for SOI task
├── soi_train_80_val_20_seed_123.json   # sequence paths of 80/20 train/val split, seed 123, used for SOI task
├── soi_train_80_val_20_seed_1337.json
├── soi_train_80_val_20_seed_271.json
└── soi_train_80_val_20_seed_42.json
```

## Install wav2vec-rf
* Create conda environment
```
conda create -n w2v-rf python=3.9 pip
conda activate w2v-rf
```
* Install torch and dependencies. Uses mlflow for logging artifacts/metrics and pyrallis for easy config management
```
pip install -U pip

# cuda version >= 11.0
pip install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu113
# cuda version < 11.0
pip install torch torchvision

pip install mlflow pyrallis pandas tqdm pillow
```

* Install repo
```
git clone https://github.com/phelps-matthew/wav2vec-rf.git
cd wav2vec-rf
pip install -e .
```
