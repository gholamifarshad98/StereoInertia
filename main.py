from  StereoInertia import StereoInertia
import matplotlib.pyplot as plt
import cv2

leftImage = cv2.imread('/home/farshad/Desktop/Phd/downloadData/drivingStereo_left/2018-07-09-16-11-56_2018-07-09-16-32-35-850.jpg', 0)
rightImage = cv2.imread('/home/farshad/Desktop/Phd/downloadData/drivingStereo_right/2018-07-09-16-11-56_2018-07-09-16-32-35-850.jpg', 0)

# leftImage = cv2.imread('leftPic.png', 0)
# rightImage = cv2.imread('rightPic.png', 0)
disparity = 20
scale_percent = 100 # percent of original size
width = int(leftImage.shape[1] * scale_percent / 100)
height = int(leftImage.shape[0] * scale_percent / 100)
dim = (width, height)
print(dim)
leftImage = cv2.resize(leftImage, dim, interpolation = cv2.INTER_AREA)
rightImage = cv2.resize(rightImage, dim, interpolation = cv2.INTER_AREA)

stereo = StereoInertia(rightImage=rightImage , leftImage=leftImage , selectedDisparity= disparity)

i_yy = stereo.calcStereoInertia()
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(i_yy)


ax2.imshow(leftImage,cmap='gray', vmin=0, vmax=255)

plt.show()

