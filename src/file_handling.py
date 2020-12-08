from PIL import Image
import numpy as np

def read_image(image_path):
    """
    指定されたパスの画像データを画像処理ライブラリのPILのImageを使って読み込む
    Args:
        image_path: string : 画像のパス
    Returns:
        画像データを読み込んだ結果
    """
    img = Image.open(image_path)
    rgb_img = img.convert('RGB')
    return rgb_img

def get_each_pixel_color(img_data):
    """
    PILライブラリを使用して読み込まれたデータから各ピクセル毎の色データを配列として取得する
    Args:
        img_data: PIL.Image : PILライブラリによって読み込まれた画像データ
    Returns:
        対象画像の各ピクセルの色配列
    """
    width, height = img_data.size
    each_pixel_colors = []
    for column in range(height):
        vector = []
        for row in range(width):
            vector.append(img_data.getpixel((row, column)))
        each_pixel_colors.append(vector)
    each_pixel_colors = np.array(each_pixel_colors)
    return each_pixel_colors

def write_image(img_array, path):
    """
    図案として生成された画像を出力する
    Args:
        img_data: PIL.Image.convert('RGB') : 図案として作成された図案のドット絵のRGBデータ
        path: string : 図案の書き込み先のパス
    Returns:
        None
    """
    img_data = Image.fromarray(np.uint8(img_array))
    img_data.save(path, quality=100)
