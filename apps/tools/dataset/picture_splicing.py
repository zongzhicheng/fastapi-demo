# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe: 图片拼接
"""
import numpy as np
from PIL import Image
import os


def concatenate_and_crop(img1_path, img2_path, output_path):
    """
    将img1的下半部分和img2的上半部分拼接到一起
    :param img1_path:
    :param img2_path:
    :param output_path:
    :return:
    """
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # 保留img1下半部分
    img1_crop = img1.crop((0, img1.size[1] / 2, img1.size[0], img1.size[1]))
    # 保留img2上半部分
    img2_crop = img2.crop((0, 0, img2.size[0], img2.size[1] / 2))

    # 纵向拼接
    output_img = Image.fromarray(np.concatenate((img1_crop, img2_crop), axis=0))
    # 横向拼接
    # output_img = Image.fromarray(np.concatenate((img1_crop, img2_crop), axis=1))

    # 保存图片
    output_img.save(output_path)


if __name__ == '__main__':
    input_path = '../../../data/first_aid_device/before_splicing'
    output_path = '../../../data/first_aid_device/after_splicing'
    for filename in os.listdir(input_path):
        picture_id = filename.split('_')[2].split('.')[0]
        if os.path.exists(
                f"{input_path}/{filename.split('_')[0]}_{filename.split('_')[1]}_{int(picture_id) + 1}.jpg"):
            concatenate_and_crop(
                f"{input_path}/{filename}",
                f"{input_path}/{filename.split('_')[0]}_{filename.split('_')[1]}_{int(picture_id) + 1}.jpg",
                f"{output_path}/{filename.split('.')[0]}_{int(picture_id) + 1}.jpg")
