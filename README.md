# Hand Pose Estimation with Keras

## Overview

This project contains my [Rose-Hulman undergraduate thesis](https://zanecodes.github.io/thesis/) on mobile hand pose estimation with deep learning.

## Getting Started

### Prerequisites

In order to run this project, you will need the following packages:

* [Jupyter Notebook](http://jupyter.readthedocs.io/en/latest/install.html)
* [TensorFlow](https://www.tensorflow.org/install/)
* [Keras](https://keras.io/#installation)
* [h5py](http://docs.h5py.org/en/latest/build.html)
* [NYU Hand Pose Dataset](http://cims.nyu.edu/~tompson/NYU_Hand_Pose_Dataset.htm#download)

There are several ways to install these, namely Pip and Anaconda; I recommend using Anaconda.

### Quickstart

If you're impatient, you can simply run the following in a Linux terminal to get up and running:

    git clone git@github.com:zanecodes/thesis.git
    cd thesis
    wget http://horatio.cs.nyu.edu/mit/tompson/nyu_hand_dataset_v2.zip
    unzip nyu_hand_dataset_v2.zip -d nyu_hand_dataset_v2
    pip3 install -r requirements.txt
    jupyter notebook

The NYU Hand Pose Dataset is 92gb, so be sure you have the disk space and bandwidth for this, and expect it to take a while.
You should now have a web browser open with a running instance of Jupyter Notebook.
