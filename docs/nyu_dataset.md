# NYU Hand Pose Dataset Overview

The NYU dataset used in [Real-Time Continuous Pose Recovery of Human Hands Using Convolutional Networks](http://cims.nyu.edu/~tompson/others/TOG_2014_paper.pdf) contains 8252 testing images and 72757 training images, plus labels for each.
Testing data is contained in the test/ subdirectory, and training data is contained in the train/ subdirectory.


## Images

### Format

All images consist of 640 x 480 x 3 unsigned 8-bit integers stored in .png format.
Each image contains either RGB, depth, or synthetic depth data, from a front, top, or side view.
Depth and synthetic depth data is stored with the most significant bits in the green channel and the least significant in the blue channel.

### Image names

[Type]_[Angle]_[Number].png

#### Types

* rgb
* depth
* synthdepth

#### Angles

* 1 Front view
* 2 Top view
* 3 Side view

#### Numbers

Numbers start at 0000001 and are padded with zeroes to 7 digits.


## Labels

### Format

Labels consist of 36 x 3 double precision floating point numbers stored in the MATLAB .mat format, in the file joint_data.mat.
Each 3-tuple makes up a point in the uvd coordinate system, which is the coordinate system used by the depth images above.

### Columns

[Finger]_[Segment]_[Component]

Each finger segment is represented by two points, one for the joint and one for the bone, for a total of 6 points per finger.
The palm is represented by six points, three for the palm itself and three for the wrist.

#### Fingers

* F1 Pinky
* F2 Ring finger
* F3 Middle finger
* F4 Index finger
* TH Thumb

#### Segments

* KNU3 Fingertip (distal phalanx)
* KNU2 Finger middle (middle phalanx)
* KNU1 Finger base (proximal phalanx)

#### Components

* A Bone (bone neck)
* B Joint (bone base)

#### Palm

* PALM_1 Outer (ulnar) side of wrist (pisiform)
* PALM_2 Inner (radial) side of wrist (scaphoid)
* PALM_3 Inner (radial) side of palm (pinky metacarpal)
* PALM_4 Outer (ulnar) side of palm (middle metacarpal)
* PALM_5 Middle of palm (ring metacarpal)
* PALM_6 Middle of wrist (lunate)

#### Order

* F1_KNU3_A
* F1_KNU3_B
* F1_KNU2_A
* F1_KNU2_B
* F1_KNU1_A
* F1_KNU1_B
* F2_KNU3_A
* F2_KNU3_B
* F2_KNU2_A
* F2_KNU2_B
* F2_KNU1_A
* F2_KNU1_B
* F3_KNU3_A
* F3_KNU3_B
* F3_KNU2_A
* F3_KNU2_B
* F3_KNU1_A
* F3_KNU1_B
* F4_KNU3_A
* F4_KNU3_B
* F4_KNU2_A
* F4_KNU2_B
* F4_KNU1_A
* F4_KNU1_B
* TH_KNU3_A
* TH_KNU3_B
* TH_KNU2_A
* TH_KNU2_B
* TH_KNU1_A
* TH_KNU1_B
* PALM_1
* PALM_2
* PALM_3
* PALM_4
* PALM_5
* PALM_6
