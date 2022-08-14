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
        pass

    @staticmethod
    def transpose_array(array, order=(1, 2, 0)):
        """
        Transposes the numpy array according to the desired order.
        :param array: ndarray as shape (x, y, z)
        :param order: transpose order
        :return: transposed array
        """
        return np.transpose(array, order)

    @staticmethod
    def rgb_to_bgr(array):
        """
        Converts the image from rgb to bgr with OpenCV.
        :param array: input image as ndarray
        :return: bgr image as ndarray
        """
        return cv2.cvtColor(array.astype(np.float32), cv2.COLOR_RGB2BGR)
