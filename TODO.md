# TODO

## Overall

* Research research strategies
* ~~Email EIT for download exemption~~
* ~~Download http://horatio.cs.nyu.edu/mit/tompson/nyu_hand_dataset_v2.zip~~
* ~~Clone https://github.com/jsupancic/deep_hand_pose and run some code~~
* Reimplement Deep Hand Pose in TensorFlow
  * Build the graph structure
    * Read the graph protobuffer format, understand the graph layers & vector input/output shapes, document
    * Translate graph into TensorFlow graph
  * Convert the NYU dataset to something TensorFlow can read
    * ~~Look at converting .png to TensorFlow vectors (TFRecord files?)~~
    * ~~Figure out how to add images to .npz file individually~~
    * Read labels and understand/document their format
    * Add .csv labels to HDF5 file
  * Convert the trained weights if possible
    * Look up Caffe weight format
    * Try using caffe-tensorflow to convert weights
    * Otherwise, convert Caffe weights into TensorFlow weights
* ~~Make a short slideshow~~
  * ~~Overview/background of project~~
  * ~~Problem statement (inputs, outputs, process)~~
  * ~~Goals (mobile, non-depth)~~

## This week

* Read labels and understand/document their format