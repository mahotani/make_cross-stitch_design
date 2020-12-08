import numpy as np
import file_handling
from matplotlib import pyplot as plt

image_path = "./../test_data/魔理沙.png"
write_path = "./../test_data/変換後.png"
img = file_handling.read_image(image_path)

file_handling.write_image(np.array(img), write_path)
