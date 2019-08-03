# PUPIL-Detection-using-OpenCV
PUPIL detection from eyes images using OpenCV 3 and Python 3.6. 

Face detection and Eyes detection using OpenCV is a common project which can be demonstrated using HAARCASCADEs by OpenCV. OpenCV have provided various trainers which can be used directly in detecting Faces, Eyes and other various elements. 

## PUPIL detection
Detecting PUPIL or EyeBall using OpenCV.

### Algorithm 
  1. First take the eye image.
  2. Make it invert.
  3. Convert it to gray scale.
  4. Apply Erosion Transform.
  5. Use binary filter taking threshold value 220.
  6. Find the biggest object.
  7. Find that object's center point and height.
  8. Highlight that circle.

### Useful Links 

**Morphological Erosion** : https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

**OpenCV contours and Hierarchy** : https://github.com/eyantrainternship/eYSIP_2015_Marker_based_Robot_Localisation/wiki/Contours-and-Hierarchy
