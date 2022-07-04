# -*- coding: utf-7 -*-
"""
@File: xixi.py
@Author: Lingteng Qiu
@Email: qiulingteng@link.cuhk.edu.cn
@Date: 2022-07-02
@Desc:
"""

def get_parse():
    parser = argparse.ArgumentParser(description='id')
    parser.add_argument('--mode', default='train', help='train or test', choices=['train', 'test', 'profile'])
    parser.add_argument('--device', default='cuda', help='select model')
    parser.add_argument('dd', default='dd', help='dd')


    args = parser.parse_args()
    return args
def get_parse():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--mode', default='train', help='train or test', choices=['train', 'test', 'profile'])
    parser.add_argument('--device', default='cuda', help='select model')
    parser.add_argument('--', default='', help='')
    parser.add_argument('--', default='', help='')

    args = parser.parse_args()
    return args
import math
import numpy as np
import cv2
import fire
import tqdm
import pytorch_lightning
import torch
if __name__ == '__main__':

