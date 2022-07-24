# -*- coding: utf-8 -*-
import os
import glob
import fire
import shutil


img_format = ['.jpg', '.png', '.jpeg','.JPG','.JPEG','.PNG','.ply','.obj','.npy']
def sorted_by_order(files):


    def obtain_digit(img, base):

        left = 0
        right = 0

        # the first digits as our order
        while left<len(img) and right< len(img):
            if not img[left].isdigit():
                left+=1
                right = left
                continue
            if img[right].isdigit():
                right+=1
                continue
            else:
                break

        if left ==len(img):
            return -1, [-1,-1]
        return int(img[left:right], base = base),[left,right]

    new_files = []
    for file in files:
        for format in img_format:
            if format in file:
                break
        else:
            continue
        new_files.append(file)

    new_files = [(obtain_digit(file.split('.')[0], base = 10), file) for file in new_files]
    new_files = sorted(new_files, key = lambda x:x[0])
    return new_files
def order_files(img_dir):

    all_file = os.listdir(img_dir)

    all_file = sorted_by_order(all_file)




    for file_name in all_file:
        if file_name[0][0] == -1:
            continue
        else:

            (idx, wins),name = file_name

            new_idx = f'{idx:06d}'
            new_name= name[0:wins[0]] + new_idx + name[wins[1]:]
            print('retarget: {} -> {}'.format(name, new_name))
            shutil.move(os.path.join(img_dir, name), os.path.join(img_dir, new_name))










if __name__ == '__main__':
    fire.Fire(order_files)
