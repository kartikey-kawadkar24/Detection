import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox

im = cv2.imread('Add your own image path/image.jpg')
image = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
bbox, label, conf = cv.detect_common_objects(image)
output_image = draw_bbox(image, bbox, label, conf)
plt.imshow(output_image)
plt.show()
