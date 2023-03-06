import sys
import time
import numpy as np
from scipy import ndimage
from scipy.interpolate import interpn
import matplotlib.pyplot as plt
import re


def read_data(t):
    filename = f"vel-{t}.txt"
    with open(filename, "r") as f:
        lines = f.readlines()
        first_line = lines[0]
        print(first_line)



read_data(300)


