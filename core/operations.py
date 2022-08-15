"""
Author: Resul Emre AYGAN
Copyright: Copyright 2022, Image Processing Toolkit
License: MIT
Version: 0.0.1
E-mail: remreaygan@gmail.com
"""
import cv2
import numpy as np


class Operations:
    def __init__(self):
        self.array_info = None

    def set_array_info(self, array):
        """
        Sets the info of the array
        :param array: as type ndarray
        :return: None
        """
        self.array_info = np.iinfo(array)

    @staticmethod
    def transpose_array(array, order=(1, 2, 0)):
        """
        Transposes the numpy array according to the desired order
        :param array: ndarray as shape (x, y, z)
        :param order: transpose order
        :return: transposed array as type ndarray
        """
        return np.transpose(array, order)

    @staticmethod
    def rgb_to_bgr(array):
        """
        Converts the image from rgb to bgr with OpenCV
        :param array: input rgb image as type ndarray
        :return: bgr image as type ndarray
        """
        return cv2.cvtColor(array.astype(np.float32), cv2.COLOR_RGB2BGR)

    @staticmethod
    def rgb_to_gray(array):
        """
        Converts the image from rgb to gray with OpenCV
        :param array: input rgb image as type ndarray
        :return: gray image as type ndarray
        """
        return cv2.cvtColor(array.astype(np.float32), cv2.COLOR_RGB2GRAY)

    @staticmethod
    def rgb_to_hsv(array):
        """
        Converts the image from rgb to hsv with OpenCV
        :param array: input rgb image as type ndarray
        :return: hsv image as type ndarray
        """
        return cv2.cvtColor(array.astype(np.float32), cv2.COLOR_RGB2HSV)

    @staticmethod
    def bgr_to_rgb(array):
        """
        Converts the image from bgr to rgb with OpenCV
        :param array: input bgr image as type ndarray
        :return: rgb image as type ndarray
        """
        return cv2.cvtColor(array.astype(np.float32), cv2.COLOR_BGR2RGB)

    @staticmethod
    def bgr_to_hsv(array):
        """
        Converts the image from bgr to hsv with OpenCV
        :param array: input bgr image as type ndarray
        :return: hsv image as type ndarray
        """
        return cv2.cvtColor(array.astype(np.float32), cv2.COLOR_BGR2HSV)

    @staticmethod
    def bgr_to_gray(array):
        """
        Converts the image from bgr to gray with OpenCV
        :param array: input bgr image as type ndarray
        :return: gray image as type ndarray
        """
        return cv2.cvtColor(array.astype(np.float32), cv2.COLOR_BGR2GRAY)

    @staticmethod
    def hsv_to_bgr(array):
        """
        Converts the image from hsv to bgr with OpenCV
        :param array: input hsv image as type ndarray
        :return: bgr image as type ndarray
        """
        return cv2.cvtColor(array.astype(np.float32), cv2.COLOR_HSV2BGR)

    @staticmethod
    def hsv_to_rgb(array):
        """
        Converts the image from hsv to rgb with OpenCV
        :param array: input hsv image as type ndarray
        :return: rgb image as type ndarray
        """
        return cv2.cvtColor(array.astype(np.float32), cv2.COLOR_HSV2RGB)

    @staticmethod
    def gray_to_rgb(array):
        """
        Converts the image from gray to rgb with OpenCV
        :param array: input gray image as type ndarray
        :return: rgb image as type ndarray
        """
        return cv2.cvtColor(array.astype(np.float32), cv2.COLOR_GRAY2RGB)

    @staticmethod
    def gray_to_bgr(array):
        """
        Converts the image from gray to bgr with OpenCV
        :param array: input gray image as type ndarray
        :return: bgr image as type ndarray
        """
        return cv2.cvtColor(array.astype(np.float32), cv2.COLOR_GRAY2BGR)

    def calc_hist(self, array):
        """
        Calculates the histogram of the array
        :param array: input image as type ndarray
        :return: hist and bins values
        """
        hist, bins = np.histogram(array.flatten(),
                                  (self.array_info.max + 1),
                                  [self.array_info.min, (self.array_info.max + 1)])

        return hist, bins

    def contrast(self, array, alpha=1.0, beta=0):
        """
        Adjusts the contrast of the image using numpy
        :param array: input image as type ndarray
        :param alpha: alpha value for contrast as type float
        :param beta: beta value for brightness as type integer
        :return: contrasted image array as type ndarray
        """

        return np.clip(alpha * array.astype(np.float32) + beta, 0, self.array_info.max)
