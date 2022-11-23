# wav2vec-rf
wav2vec-RF: Applying ASR to Raw Radio Signals Intercepted From Low Earth Orbit Satellites (Official Repo)

Release coming soon.


## LibriIQ-Dwingeloo Dataset
The LibriIQ-Dwingeloo dataset contains RF observations of low Earth orbit (LEO) satellite transmissions in the ultra-high-frequency (UHF) band sourced from https://charon.camras.nl/public/satnogs/. Each observation comprises an RF IQ (in-phase, quadrature) signal sampled at 48 kHz. LibriIQ-Dwingeloo spans 44 distinct satellites, 7 modulation types, and 100 total observations.

For seamless integration into ASR-based architectures, LibriIQ-Dwingeloo is designed to mimic the LibriSpeech ASR corpus. Taking account of the 48kHz sample rate, each RF IQ observation is split into a series of sequences with each sequence having an approximately equal number of samples as the LibriSpeech sequences used in wav2vec2.

### Download
Download LibriIQ-Dwingeloo from https://www.kaggle.com/datasets/matthewphelps/libriiq-dwingeloo. Requires registering a Kaggle account (free). Output is a 5 GB `archive.zip` file.

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
+-- _config.yml
+-- _drafts
|   +-- begin-with-the-crazy-ideas.textile
|   +-- on-simplicity-in-technology.markdown
+-- _includes
|   +-- footer.html
|   +-- header.html
+-- _layouts
|   +-- default.html
|   +-- post.html
+-- _posts
|   +-- 2007-10-29-why-every-programmer-should-play-nethack.textile
|   +-- 2009-04-26-barcamp-boston-4-roundup.textile
+-- _data
|   +-- members.yml
+-- _site
+-- index.html


## wav2vec-rf Installation
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

* Install wav2vec-rf repo
```
git clone https://github.com/phelps-matthew/wav2vec-rf.git
cd wav2vec-rf
pip install -e .
```
