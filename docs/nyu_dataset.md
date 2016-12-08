The NYU dataset used in [Real-Time Continuous Pose Recovery of Human Hands Using Convolutional Networks](http://cims.nyu.edu/~tompson/others/TOG_2014_paper.pdf) consists of the following files:

### Test labels

* test/joint_data.mat
* test/test_predictions.mat

### Test images (8252)

* test/depth_1_NNNNNNN.png
* test/depth_2_NNNNNNN.png
* test/depth_3_NNNNNNN.png
* test/rgb_1_NNNNNNN.png
* test/rgb_2_NNNNNNN.png
* test/rgb_3_NNNNNNN.png
* test/synthdepth_1_NNNNNNN.png
* test/synthdepth_2_NNNNNNN.png
* test/synthdepth_3_NNNNNNN.png

### Train labels

* train/joint_data.mat

### Train images (72757)

* train/depth_1_NNNNNNN.png
* train/depth_2_NNNNNNN.png
* train/depth_3_NNNNNNN.png
* train/rgb_1_NNNNNNN.png
* train/rgb_2_NNNNNNN.png
* train/rgb_3_NNNNNNN.png
* train/synthdepth_1_NNNNNNN.png
* train/synthdepth_2_NNNNNNN.png
* train/synthdepth_3_NNNNNNN.png

where NNNNNNN starts at 0000001.

### Image types

#### Depth images
640 x 480 x 1
Blue channel contains depth information.

##### depth_1_NNNNNNN.png
Front view depth images.

##### depth_2_NNNNNNN.png
Top view depth images.

##### depth_3_NNNNNNN.png
Right view depth images.

#### RGB images
640 x 480 x 3

##### rgb_1_NNNNNNN.png
Front view RGB images.

##### rgb_2_NNNNNNN.png
Top view RGB images.

##### rgb_3_NNNNNNN.png
Right view RGB images. 
