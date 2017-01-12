# Deep Hand Pose Implementation Overview

This document outlines the structure of the [Caffe implementation](https://github.com/jsupancic/deep_hand_pose) of the [Hands Deep in Deep Learning](https://arxiv.org/abs/1502.06807) paper.

Relevant files:

* deep_hand_pose/examples/deep_hand_pose/solver.prototxt
* deep_hand_pose/examples/deep_hand_pose/oberweger-pca.prototxt
* deep_hand_pose/src/caffe/layers/pca_layer.cpp
* deep_hand_pose/examples/deep_hand_pose/pca_eigenvectors.dat
* deep_hand_pose/examples/deep_hand_pose/pca_eigenvalues.dat
* deep_hand_pose/examples/deep_hand_pose/pca_mean.dat



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
