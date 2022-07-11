# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe: 数据增强
"""
import cv2
from PIL import Image
import numpy as np
import random


def flip_horizontally(img_path, txt_path, save_img_path, save_txt_path):
    """
    水平翻转
    :param img_path: 'xxx/xxx/test.jpg'
    :param txt_path: 'xxx/xxx/test.txt'
                     YOLO格式：class center_x/X center_y/Y width/X height/Y
    :param save_img_path: 'xxx/yyy/' 默认保存至'xxx/yyy/test_horizontally.jpg'
    :param save_txt_path: ‘xxx/yyy/’ 默认保存至'xxx/yyy/test_horizontally.txt'
    :return:
    """
    img_name = img_path.split('/')[-1]  # xxx.jpg / xxx.png
    txt_name = txt_path.split('/')[-1]  # xxx.txt
    img = cv2.imread(img_path)
    fh = open(txt_path, 'r')
    for line in fh:
        line = line.strip('\n').rstrip()
        l = line.split(' ')
        with open(f"{save_txt_path + txt_name.split('.')[0] + '_horizontally.' + txt_name.split('.')[-1]}", "a") as f:
            f.write(f"{l[0]} {1 - float(l[1])} {l[2]} {l[3]} {l[4]}\n")
    cv2.imwrite(save_img_path + img_name.split('.')[0] + "_horizontally." + img_name.split('.')[-1], img[:, ::-1, ])


def flip_vertical(img_path, txt_path, save_img_path, save_txt_path):
    """
    竖直翻转
    :param img_path: 'xxx/xxx/test.jpg' 图片通道为3，例如55*50*3
    :param txt_path: 'xxx/xxx/test.txt'
                     YOLO格式：class center_x/X center_y/Y width/X height/Y
    :param save_img_path: 'xxx/yyy/' 默认保存至'xxx/yyy/test_vertical.jpg'
    :param save_txt_path: ‘xxx/yyy/’ 默认保存至'xxx/yyy/test_vertical.txt'
    :return:
    """
    img_name = img_path.split('/')[-1]  # xxx.jpg / xxx.png
    txt_name = txt_path.split('/')[-1]  # xxx.txt
    img = cv2.imread(img_path)
    fh = open(txt_path, 'r')
    for line in fh:
        line = line.strip('\n').rstrip()
        l = line.split(' ')
        with open(f"{save_txt_path + txt_name.split('.')[0] + '_vertical.' + txt_name.split('.')[-1]}", "a") as f:
            f.write(f"{l[0]} {l[1]} {1 - float(l[2])} {l[3]} {l[4]}\n")
    cv2.imwrite(save_img_path + img_name.split('.')[0] + "_vertical." + img_name.split('.')[-1], img[::-1])


def rotate(img_path, txt_path, save_img_path, save_txt_path, rotate="ROTATE_90"):
    """
    旋转
    :param img_path: 'xxx/xxx/test.jpg'
    :param txt_path: 'xxx/xxx/test.txt'
                     YOLO格式：class center_x/X center_y/Y width/X height/Y
    :param save_img_path: 'xxx/yyy/' 默认保存至'xxx/yyy/test_ROTATE_90.jpg'
    :param save_txt_path: 'xxx/yyy/' 默认保存至'xxx/yyy/test_ROTATE_90.txt'
    :param rotate:默认 Image.ROTATE_90 逆时针旋转90度
                  Image.ROTATE_180 逆时针选择180度
                  Image.ROTATE_270 逆时针旋转270度
    :return:
    """
    rotate_dist = {"ROTATE_90": Image.ROTATE_90,
                   "ROTATE_180": Image.ROTATE_180,
                   "ROTATE_270": Image.ROTATE_270}
    img_name = img_path.split('/')[-1]  # xxx.jpg / xxx.png
    txt_name = txt_path.split('/')[-1]  # xxx.txt
    img = Image.open(img_path)
    # 旋转矩阵
    rotate_img = img.transpose(rotate_dist[rotate])
    fh = open(txt_path, 'r')
    for line in fh:
        line = line.strip('\n').rstrip()
        l = line.split(' ')
        if rotate == "ROTATE_90":
            with open(f"{save_txt_path + txt_name.split('.')[0] + '_ROTATE_90.' + txt_name.split('.')[-1]}", "a") as f:
                f.write(f"{l[0]} {l[2]} {1 - float(l[1])} {l[4]} {l[3]}\n")
        if rotate == "ROTATE_180":
            with open(f"{save_txt_path + txt_name.split('.')[0] + '_ROTATE_180.' + txt_name.split('.')[-1]}", "a") as f:
                f.write(f"{l[0]} {1 - float(l[1])} {1 - float(l[2])} {l[3]} {l[4]}\n")
        if rotate == "ROTATE_270":
            with open(f"{save_txt_path + txt_name.split('.')[0] + '_ROTATE_270.' + txt_name.split('.')[-1]}", "a") as f:
                f.write(f"{l[0]} {1 - float(l[2])} {l[1]} {l[4]} {l[3]}\n")
    rotate_img.save(save_img_path + img_name.split('.')[0] + f"_{rotate}." + img_name.split('.')[-1])


def lighting_adjust(img_path, save_img_path, k_down=0.0, k_up=2.0, b_down=0.0, b_up=3.0):
    """
    图像亮度、对比度调整
    :param img_path: 'xxx/xxx/test.jpg'
                    程序会自动匹配 test.txt 一定得是标注好的yolo格式的txt
    :param save_img_path: 'xxx/yyy/'
    :param k_down: 对比度系数下限
                对比度的上下限最好先手工固定几个值看看效果
    :param k_up: 对比度系数上限
    :param b_down: 亮度增值上限
    :param b_up: 亮度增值下限
    :return:
    """

    img_name = img_path.split('/')[-1]  # xxx.jpg / xxx.png
    txt_path = f"{img_path.rstrip(img_path.split('/')[-1])}/{img_name.split('.')[0]}.txt"

    img = cv2.imread(img_path)
    # 对比度调整系数
    slope = random.uniform(k_down, k_up)
    # 亮度调整系数
    bias = random.uniform(b_down, b_up)
    # 图像亮度和对比度调整
    img = img * slope + bias
    # 灰度值截断，防止超出255
    img = np.clip(img, 0, 255)
    img = img.astype(np.uint8)
    fh = open(txt_path, 'r')
    for line in fh:
        line = line.strip('\n').rstrip()
        with open(f"{save_img_path}{img_name.split('.')[0]}_random_lighting_{slope:.3f}_{bias:.3f}.txt", "a") as f:
            f.write(f"{line}\n")
    cv2.imwrite(
        f"{save_img_path}{img_name.split('.')[0]}_random_lighting_{slope:.3f}_{bias:.3f}.{img_name.split('.')[-1]}",
        img)
