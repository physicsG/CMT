# Introduction
CMT (Consensus-based Matching and Tracking of Keypoints for Object Tracking) is
a novel keypoint-based method for long-term model-free object tracking in a
combined matching-and-tracking framework.
Details can be found on the [project page](http://www.gnebehay.com/cmt)
and in our [publication](http://www.gnebehay.com/publications/wacv_2014/wacv_2014.pdf).
The Python implementation in this repository is platform-independent and runs
on Linux, Windows and OS X.

#License
CMT is freely available under the [3-clause BSD license][1],
meaning that you can basically do with the code whatever you want.
If you use our algorithm in scientific work, please cite our publication
```
@inproceedings{Nebehay2014WACV,
    author = {Nebehay, Georg and Pflugfelder, Roman},
    booktitle = {Winter Conference on Applications of Computer Vision},
    month = mar,
    publisher = {IEEE},
    title = {Consensus-based Matching and Tracking of Keypoints for Object Tracking},
    year = {2014}
}
```

# Dependencies
* Python
* OpenCV-Python (>= 2.4)
* NumPy
* SciPy
* optional: ipdb (for debugging the code)

Note for Windows users: if you are unable to read video files, please follow this suggestion: http://stackoverflow.com/questions/11699298/opencv-2-4-videocapture-not-working-on-windows

# Usage
```
usage: python ObjectTracker.py
```

[1]: http://en.wikipedia.org/wiki/BSD_licenses#3-clause_license_.28.22Revised_BSD_License.22.2C_.22New_BSD_License.22.2C_or_.22Modified_BSD_License.22.29
