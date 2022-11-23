# wav2vec-rf
wav2vec-RF: Applying ASR to Raw Radio Signals Intercepted From Low Earth Orbit Satellites (Official Repo)

Release coming soon.

## Installation
* Create conda environment
```
conda create -n wav2rf python=3.9 pip
conda activate wav2rf
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

* Install wav2vec-rf repo
```
git clone https://github.com/phelps-matthew/wav2vec-rf.git
cd wav2vec-rf
pip install -e .
```

## LibriIQ-Dwingeloo Dataset
The LibriIQ-Dwingeloo dataset contains RF observations of low Earth orbit (LEO) satellite transmissions in the ultra-high-frequency (UHF) band sourced from https://charon.camras.nl/public/satnogs/. Each observation comprises an RF IQ (in-phase, quadrature) signal sampled at 48 kHz. LibriIQ-Dwingeloo spans 44 distinct satellites, 7 modulation types, and 100 total observations.

For seamless integration into ASR-based architectures, LibriIQ-Dwingeloo is designed to mimic the LibriSpeech ASR corpus. Taking account of the 48kHz sample rate, each RF IQ observation is split into a series of sequences with each sequence having an approximately equal number of samples as the LibriSpeech sequences used in wav2vec2.

### Download
Download LibriIQ-Dwingeloo from https://www.kaggle.com/datasets/matthewphelps/libriiq-dwingeloo. Requires registering a Kaggle account (free). Output is a 5 GB `archive.zip` file.

### Create
Ensure the wav2vec-rf library is installed as in [Installation](#installation)



