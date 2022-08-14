"""
Author: Resul Emre AYGAN
Copyright: Copyright 2022, Image Processing Toolkit
License: MIT
Version: 0.0.1
E-mail: remreaygan@gmail.com
"""

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
