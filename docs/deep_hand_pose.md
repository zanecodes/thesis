# Deep Hand Pose Implementation Overview

This document outlines the structure of the [Caffe implementation](https://github.com/jsupancic/deep_hand_pose) of the [Hands Deep in Deep Learning](https://arxiv.org/abs/1502.06807) paper.

Relevant files:

* deep_hand_pose/examples/deep_hand_pose/solver.prototxt
* deep_hand_pose/examples/deep_hand_pose/oberweger-pca.prototxt
* deep_hand_pose/src/caffe/layers/pca_layer.cpp
* deep_hand_pose/examples/deep_hand_pose/pca_eigenvectors.dat
* deep_hand_pose/examples/deep_hand_pose/pca_mean.dat
* deep_hand_pose/src/caffe/jvl.cpp
* deep_hand_pose/include/jvl/blob_io.hpp



## Outline


Input ->
Convolution -> Max pool -> Leaky ReLU ->
Convolution -> Max pool -> Leaky ReLU ->
Convolution -> Leaky ReLU ->
Fully connected 1024 nodes, std dev 0.01 -> ReLU ->
Fully connected 1024 nodes, std dev 0.05 -> ReLU ->
Fully connected 22 nodes, std dev 0.02 ->
Fully connected 28 nodes ->
Euclidean loss


### All layers

Initial biases:		0


### Convolution

Filters:		8
Kernel size:		5 x 5
Stride length:		1 x 1
Initial weights:	Xavier


### Max pool

Size:			2 x 2
Stride length:		2 x 2


### Leaky ReLU

Alpha:			0.05


### Fully connected

Initial weights:	Gaussian

The final fully connected layer does not learn. Its weights and biases are initialized using the PCA eigenvectors and PCA means computed from the labels.



## Solver Parameters


See the [Caffe docs](http://caffe.berkeleyvision.org/tutorial/solver.html#sgd) for more information.

* Solver:		Stochastic Gradient Descent
* Batch size: 		64
* Base learning rate:	0.000005
* Momentum:		0.9
* Maximum iterations:	40000

* Learning rate decay:	lr = base_lr * (1 + gamma * iter) ^ -power
* Gamma:		0.0001
* Power:		0.75



## Inputs


This implementation only trains on the front view depth images.
Input depth data is resized to 128 x 128 using the OpenCV INTER_AREA sampling method.
The depth values are then divided by 10.
The input therefore consists of a (64 x 128 x 128 x 1) tensor.



## Outputs


Output labels consist of the u and v values from the following joints:

F1_KNU3_A (0)
F1_KNU2_B (3)
F2_KNU3_A (6)
F2_KNU2_B (9)
F3_KNU3_A (12)
F3_KNU2_B (15)
F4_KNU3_A (18)
F4_KNU2_B (21)
TH_KNU3_A (24)
TH_KNU3_B (25)
TH_KNU2_B (27)
PALM_1    (30)
PALM_2    (31)
PALM_3    (32)

The depth values are then divided by 10.
The output therefore consists of a (28 x 1) tensor.
