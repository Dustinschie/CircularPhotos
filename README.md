# CircularPhotos
simple tool to generate circularly 'masked, or cut-out' images. 

###Example Image
![Original Image](https://github.com/Dustinschie/CircularPhotos/blob/master/pasted-image.png)
![Generated Image](https://github.com/Dustinschie/CircularPhotos/blob/master/pasted-imageCircle.png)
###Software Dependencies
CircularPhotosGenerator is written in [Python 3.4](https://www.python.org/download/releases/3.4.0/) and uses the [Pillow](https://python-pillow.github.io) module for image manipulation and generation.

###Setting Up with PIP
```Bash
pip install -r /path/to/requirements.txt
```
###Usage
```Bash
python3 /path/to/CircularPhotoGenerator.py <image>
```
######Examples
```Bash
python3 CircularPhotoGenerator.py *.tiff
python3 CircularPhotoGenerator.py *.tiff image.png
```



