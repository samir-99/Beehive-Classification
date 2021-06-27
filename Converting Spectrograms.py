import os
import glob
import shutil
from pathlib import Path
import os
from pathlib import Path
from librosa import display

import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
import librosa
import numpy as np

n_fft=int(input("Length of the windowed signal after padding with zeros (if value is equal =2^n it will be FFT):"))
win_length=int(input("Window length: "))


def create_fold_spectrograms():
    spectrogram_path = Path('Path of directory where you want to save Spectrograms')  
    audio_path = Path('Path of Directory where all audio files are')  

    os.mkdir(spectrogram_path)
    for filename in glob.glob(os.path.join(path, '*.wav')):
        samples, sample_rate = librosa.load(audio_file)
        fig = plt.figure(figsize=[0.72,0.72])
        ax = fig.add_subplot(111)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.set_frame_on(False)
        filename  = filename.replace('.wav','.png')
        S = librosa.stft(y=samples, sr=sample_rate, n_fft=n_fft, win_length= win_length)
        librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
        plt.savefig(spectrogram_path, dpi=400, bbox_inches='tight',pad_inches=0)
        plt.close('all')
