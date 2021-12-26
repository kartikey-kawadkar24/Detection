import cv2
import matplotlib.pyplot as plt

image = cv2.imread(r"Add your own image path/image.jpg")
plt.imshow(image)

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.imshow(gray)

_, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
# To show binary image
plt.imshow(binary, cmap="gray")
plt.show()

# Using "findcontours" module from OpenCV
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw all contours
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
plt.imshow(image)
