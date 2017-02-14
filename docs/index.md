# Hand Pose Estimation with Keras
## Zane Geiger

	Hand pose estimation is a difficult problem with many potential applications in virtual reality, augmented reality. Depth information makes it a more tractable task, but there are still many challenges involved due to the high dimensionality of hand pose information, self-similarity, and self-occlusion. Recent papers have applied deep convolutional neural networks to this problem, with high levels of success. Enforcing a prior model on the hand pose further improves predictions, as well as refining joint locations using independent networks.

	Modern deep learning toolkits such as TensorFlow and Keras enable rapid prototyping of network architectures and hyperparameters. Importantly, TensorFlow makes it relatively easy to run models on low-powered hardware, providing libraries for Android and ARM devices and accelerating computations by offloading them to the mobile GPU. With this in mind, we have taken an existing approach to hand pose estimation, first introduced by Oberweger et. al, and created an implementation in Keras using TensorFlow as a backend.
