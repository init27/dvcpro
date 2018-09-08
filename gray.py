import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and display the original
# image
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imwrite("data/gray.jpg",gray)



 
# we need to keep in mind aspect ratio so the image does not look skewed
# or distorted -- therefore, we calculate the ratio of the new image to
# the old image. Let's make our new image have a width of 150 pixels
r = 500.0 / image.shape[1]
dim = (500, int(image.shape[0] * r))
 
# perform the actual resizing of the image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)
cv2.imwrite("data/ResizedImage.jpg",resized)
cv2.waitKey(0)