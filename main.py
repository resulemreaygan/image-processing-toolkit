"""
Author: Resul Emre AYGAN
Copyright: Copyright 2022, Image Processing Toolkit
License: MIT
Version: 0.0.1
E-mail: remreaygan@gmail.com
"""

from core.operations import Operations
from utils.constants import Constants

if __name__ == '__main__':
    ops = Operations()
    constants = Constants()

    try:
        with open(constants.banner, 'r') as f:
            contents = f.read()
            print(contents)
    except Exception as error:
        print(f"{constants.banner} does not exists!: {error}")

    print(f"Version: {constants.version}")
