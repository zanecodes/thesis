# TODO

## Overall

* Research research strategies
* ~~Email EIT for download exemption~~
* ~~Download http://horatio.cs.nyu.edu/mit/tompson/nyu_hand_dataset_v2.zip~~
* ~~Clone https://github.com/jsupancic/deep_hand_pose and run some code~~
* Reimplement Deep Hand Pose in TensorFlow
  * ~~Build the graph structure~~
    * ~~Read the graph protobuffer format, understand the graph layers & vector input/output shapes, document~~
    * ~~Translate graph into Keras graph~~
    * ~~Run and debug Keras graph~~
  * ~~Convert the NYU dataset to something TensorFlow can read~~
    * ~~Look at converting .png to TensorFlow vectors (TFRecord files?)~~
    * ~~Figure out how to add images to .npz file individually~~
    * ~~Read labels and understand/document their format~~
    * ~~Write script to convert the NYU dataset into a single HDF5 archive~~
* ~~Make a short slideshow~~
  * ~~Overview/background of project~~
  * ~~Problem statement (inputs, outputs, process)~~
  * ~~Goals (mobile, non-depth)~~
* ~~Write a paper draft~~
  * ~~Synthesize information from slideshow~~
  * ~~Collect sources~~
  * Document research process
  * Work on a journal / log
  * ~~Report on preliminary results (if any)~~
* Experiment with improvements
  * ~~Augment data with scales and translations~~
    * ~~Refactor for performance~~
  * ~~Add label depths~~
  * Add batch normalization
  * Use autoencoder instead of PCA
  * Use striding instead of max pooling
  * Change number of filters
  * Change depth of network
  * Change neurons in fully connected layers
* Work on mobile port
* Document and publish
  * ~~Create a GitHub page~~
  * Generate results graphs
  * Add installation documentation
  * Add 'why' to code documentation

## This week
* Add batch normalization
* Add 'why' to code documentation
