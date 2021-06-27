import splitfolders  # or import split_folders
# pip install split-folders  if you don't have splitfolders run this as well

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
splitfolders.ratio(r"Path of directory where folders for classes located", output="Path of directory where train and validation folders will be", seed=1337, ratio=(.8, .2), group_prefix=None) 

