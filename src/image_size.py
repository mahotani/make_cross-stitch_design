from PIL import Image
import numpy as np

def get_image_size(img_data):
    """
    入力された画像の縦横の長さを出力する
    Args:
        img_data: numpy.array : 画像のRGB情報の入ったnumpy配列
    Returns:
        width: int : 画像の横のサイズ
        height: int : 画像の縦のサイズ
    """
    height = img_data.shape[0]
    width = img_data.shape[1]
    return height, width

def embroidery_design_size(height, width):
    """
    入力されたサイズを元に刺繍図案のサイズを出力する
    出力されるサイズは、元画像の高さまたは幅のどちらかが
    150以下:
        そのままのサイズ
    500以下:
        そのままのサイズと1/3倍のサイズ
    1000以下:
        そのままのサイズと1/3倍のサイズと1/5倍のサイズ
    1001以上:
        1/3倍のサイズと1/5倍のサイズと1/10倍のサイズ
    Args:
        height: int : 画像長
        width: int : 画像幅
    Returns:
        embroidery_size: int[][] : 刺繍図案用のサイズ
    """
    embroidery_size = []
    
    # 入力された画像長、画像幅のどちらかが150px以下か否かを出力する
    if height > 150 or width > 150:
        embroidery_size.append([int(height/3), int(width/3)])
    # 入力された画像長、画像幅のどちらかが500px以下か否かを出力する
    if height > 500 or width > 500:
        embroidery_size.append([int(height/5), int(width/5)])
    # 入力された画像長、画像幅のどちらかが1000px以下か否かを出力する
    if height > 1000 or width > 1000:
        embroidery_size.append([int(height/10), int(width/10)])
    else:
        embroidery_size.append([height, width])

    return embroidery_size

def get_embroidery_size(img_data):
    """
    入力された画像から刺繍の図案サイズを出力する
    Args:
        img_data: numpy.array : 画像のRGB情報の入ったnumpy配列
    Returns:
        embroidery_size: int[][] : 刺繍図案用のサイズ
    """
    height, width = get_image_size(img_data)
    embroidery_size = embroidery_design_size(height, width)

    return embroidery_size
