import numpy as np
class StereoInertia:
    def __init__(self, leftImage, rightImage, selectedDisparity):
        self.leftImage = leftImage
        self.rightImage = rightImage
        self.disparity = selectedDisparity
        self.rows = leftImage.shape[0]
        self.columns = leftImage.shape[1]
        self.rightImageInertia = np.zeros([self.rows, 1])
        self.leftImageInertia = np.zeros([self.rows, 1])
        self.Iyy = np.zeros([self.rows, 1])


    def calcInertiaRightImage(self):
        for row in range(self.rows):
            tempInertia = 0
            for column in range(self.columns - self.disparity):
                tempInertia = tempInertia + (column+1)*int(self.rightImage[row][column])
            self.rightImageInertia[row] = tempInertia

    def calcInertiaLeftImage(self):
        for row in range(self.rows):
            tempInertia = 0
            for column in range(self.disparity, self.columns):
                tempInertia = tempInertia + (self.columns - column)*int(self.leftImage[row][column])
            self.leftImageInertia[row]


    def calcStereoInertia(self):
        self.calcInertiaRightImage()
        self.calcInertiaLeftImage()
        self.Iyy = abs(self.leftImageInertia - self.rightImageInertia)
        return  self.Iyy
