# Importing modules
import cv2
import numpy
import matplotlib.pyplot as plt

# Sample image for shapes with 4 vertices
img = cv2.imread('C:\Users\Richa\Downloads\images.jpg')

# Reading the image from the user
inp_img = cv2.imread('C:\Users\Richa\Downloads\hexagon.jpg')

# Converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)

# Convert to RGB
inp_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Thresholding
ret, thresh = cv2.threshold(gray, 0, 255, 0)
ret, thresh1 = cv2.threshold(gray1, 0, 255, 0)

# Using Canny for perfect edge detection
canny = cv2.Canny(img, 100, 200)

# Finding contours
contours, heirarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours[0]
contours1, heirarchy = cv2.findContours(
    thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours1[0]


# Finding the centroid
for s in contours1:
    M = cv2.moments(s)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])


#####################Detection of shape####################################
font = cv2.FONT_HERSHEY_SIMPLEX

# Creating lists
a = []
b = []

# Finding vertices in input image
for i in contours1:
    approx = cv2.approxPolyDP(i, 0.01 * cv2.arcLength(i, True), True)
    print len(approx)
    x = len(approx)
    a.append(x)
print a

# Finding vertices in sample image
for i in contours:
    approx = cv2.approxPolyDP(i, 0.01 * cv2.arcLength(i, True), True)
    print len(approx)
    x = len(approx)
    b.append(x)
print b

 # Detection and display of name of shape
for i in contours1:
    for m in a:
        for n in b:
            if m == 6:
                print "hexagon"
                cv2.drawContours(inp_img,[i],0,(0,255,0),2)
                cv2.putText(inp_img,"Hexagon",(cx-20,cy),font,0.5,(0,0,255),2)

 # Plotting the image
plt.subplot(121),plt.imshow(img), plt.title('Original image'),plt.set_cmap('bone')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(inp_img),plt.title('Shape found'),plt.set_cmap('bone')
plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
