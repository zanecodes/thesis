# Pose Estimation Techniques

## Monocular

* Learning-based
  * Trains a model to associate 3d poses with 2d projections
  * May not be as robust as learning-free approaches
* Learning-free
  * Uses kinematic constraints to solve pose ambiguity

* Partal estimation
* Full estimation
  * Single frame
  * Model-based tracking
    * Single hypothesis
      * Particle Swarm Optimization
    * Multiple hypothesis (Erol, Bebis, et al)

### Learning-based

* Regression forest models (Xu, Chi, et al)
* Deep learning (Oberweger, Wohlhart, & Lepetit)

### Learning-free

* Line-based pose estimation (Unzueta, Luis, et al)

## Depth-based

# Challenges

* Many degrees of freedom (up to 20) 
* Self-occlusion
* Processing speed
* Environmental variation
* Hand motion speed (Erol, Bebis, et al)
