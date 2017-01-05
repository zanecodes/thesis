# Related Work

Several previous papers have looked at recovering hand poses using convolutional and deep networks, and these are what I will be basing the bulk of my research on. Tompson et al. were the first to use convolutional networks for this particular task, and were able to improve on existing techniques. Previous works relied on methods such as randomized decision forests (Shotton et al. 2011, Keskin et al. 2011/2012), energy minimization for model fitting (Li et al. 2013, Ballan et al. 2012), and constraint solving (Melax et al. 2013). More recent approaches made use of particle swarm optimization (Oikonomidis et al. 2011, Qian et al. 2014) and regression forests (Tang et al. 2014).
There are several hand pose datasets in existence, which typically provide a set of depth images, corresponding RGB images, and ground truth hand pose labels. The NYU dataset is one such example, consisting of 3 different viewpoints captured by Kinect sensors and ground truth poses approximated using manual labeling combined with a particle swarm based estimation algorithm. The ICVL dataset is similar, captured using a time of flight camera. The former has more pose variability but less clean depth information, while the latter has more imagery but less accurate labels. My research will depend primarily on the NYU dataset, as I will be attempting to reproduce the results of Oberweger et al. using Tensorflow on a mobile platform.