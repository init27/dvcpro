import argparse
import cv2

# construct the argument parser and parse the arguments

image = cv2.imread("data/ResizedImage.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)




kernelSizes = (5, 5)
 
# loop over the kernel sizes and apply an "average" blur to the image
blurred = cv2.blur(image, (15,15))
cv2.imshow("Average (5, 5)", blurred)
cv2.waitKey(0)
cv2.imwrite("data/blur.jpg",blurred)