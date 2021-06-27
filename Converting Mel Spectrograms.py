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


def create_fold_spectrograms():
    spectrogram_path = Path('Path of directory where you want to save Mel spectrograms')  
    audio_path = Path('Path of directory where all audio files are')  
    
    os.mkdir(spectrogram_path)
    for audio_file in list(Path(audio_path).glob('*.wav')):
        samples, sample_rate = librosa.load(audio_file)
        fig = plt.figure(figsize=[0.72,0.72])
        ax = fig.add_subplot(111)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        ax.set_frame_on(False)
        filename  = spectrogram_path/Path(audio_file).name.replace('.wav','.png')
        S = librosa.feature.melspectrogram(y=samples, sr=sample_rate)
        librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
        plt.savefig(filename, dpi=400, bbox_inches='tight',pad_inches=0)
        plt.close('all')
