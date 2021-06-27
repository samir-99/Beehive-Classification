# This file will create folder for each class and will add existent spectrograms
# to these folders.


import os
import glob
import shutil
from pathlib import Path  

data_path = Path('Path of directory where folders for classes will be.') 
spectrogram_path = Path('Path of Directory where all spectrograms are.')  

labels=['24','26','27','28','30','31','32','33','34','35']


def create_fold_directory():
    png_files =  list(Path(spectrogram_path).glob('*.png'))
    
    os.mkdir(data_path/'labels')
    for label in labels:
        os.mkdir(data_path/'labels'/label)
     
    for file in png_files:
        label = str(file)[75:77]
        shutil.copyfile(file, data_path/'labels'/label/file.name)   
