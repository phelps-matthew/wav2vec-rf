# wav2vec-rf
wav2vec-RF: Applying ASR to Raw Radio Signals Intercepted From Low Earth Orbit Satellites (Official Repo)

Release coming soon.

## LibriIQ-Dwingeloo Dataset
The LibriIQ-Dwingeloo dataset contains RF observations of low Earth orbit (LEO) satellite transmissions in the ultra-high-frequency (UHF) band sourced from https://charon.camras.nl/public/satnogs/. Each observation comprises an RF IQ (in-phase, quadrature) signal sampled at 48kHz. LibriIQ-Dwingeloo spans 44 distinct satellites, 7 modulation types, and 100 total observations.

For seamless integration into ASR-based architectures, LibriIQ-Dwingeloo is designed to mimic the LibriSpeech ASR corpus. Each RF IQ observation is split into a series of sequences, with each sequence having a length approximately equal to the LibriSpeech sequence lenghts used in wav2vec2.

### Download dataset

### Format dataset
