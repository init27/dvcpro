# USAGE
# python sobel.py --image bricks.png

# import the necessary packages
import argparse
import cv2
import numpy as np

# construct the argument parser and parse the arguments

# load the image, convert it to grayscale, and display the original
# image
image = cv2.imread("data/blur.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

ap = argparse.ArgumentParser()

ap.add_argument("-l", "--lower-angle", type=float, default=175.0,
	help="Lower orientation angle")
ap.add_argument("-u", "--upper-angle", type=float, default=180.0,
	help="Upper orientation angle")
args = vars(ap.parse_args())

# compute gradients along the X and Y axis, respectively
gX = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
gY = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1)

# compute the gradient magnitude and orientation, respectively
mag = np.sqrt((gX ** 2) + (gY ** 2))
orientation = np.arctan2(gY, gX) * (180 / np.pi) % 180

# find all pixels that are within the upper and low angle boundaries
idxs = np.where(orientation >= args["lower_angle"], orientation, -1)
idxs = np.where(orientation <= args["upper_angle"], idxs, -1)
mask = np.zeros(gray.shape, dtype="uint8")
mask[idxs > -1] = 255

# show the images
cv2.imshow("Mask", mask)
cv2.imwrite("data/angle.jpg",mask)
cv2.waitKey(0)


# the `gX` and `gY` images are now of the floating point data type,
# so we need to take care to convert them back a to unsigned 8-bit
# integer representation so other OpenCV functions can utilize them
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

# combine the sobel X and Y representations into a single image
sobelCombined = cv2.addWeighted(gX, 10.5, gY, 10.5, 0)

# show our output images
cv2.imshow("Sobel X", gX)
cv2.imshow("Sobel Y", gY)
cv2.imshow("Sobel Combined", sobelCombined)
cv2.waitKey(0)