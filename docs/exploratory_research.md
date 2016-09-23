## General approach

1. Detect/isolate hand geometry from the background
  * With one camera
    * By color
    * By frame differences
  * With two or more cameras
    * By depth (stereoscopy)
  * With IR light filters
    * By color
2. Estimate hand pose
  * 2D
    * Convex hull & concavity defects
    * Gradient descent / energy minimization
  * 3D
    * ?
3. Estimate hand motion
  * 2D
    * Optical flow
    * Feature detection & correlation
  * 3D
    * ?

Different approaches provide different levels of fidelity, at the cost of performance or implementation difficulty.

## Possible libraries/services

### Clarifai

Only available as a web API, not a local library
Focuses on image and video tagging, cannot be done in real-time
Probably not suitable for our use case

### OpenCV

Straightforward to use on Android & iOS
Low-level, somewhat challenging to use
Good documentation and many examples

### TensorFlow

Available on Android
Only performs machine learning, no explicit image processing
Could be used for robust detection without explicitly writing processing code

## Sources
* http://simena86.github.io/blog/2013/08/12/hand-tracking-and-recognition-with-opencv/
