# -*- coding: utf-8 -*-
import fire
import os
import glob

def image_to_video(image_path, handler, frame = 30, object_name = None):
    if image_path[-1]=='/':
        image_path = image_path[:-1]

    handler = handler.replace('[','*')

    object_name = image_path.split("/")[-1] if object_name == None else object_name
    cmd ='rm -rf {}'.format(os.path.join(image_path, object_name))
    os.system(cmd)
    cmd = 'ffmpeg -r {} -pattern_type glob -i \'{}\' -vcodec libx264 '.format(frame, os.path.join(image_path,'{}'.format(handler))) + \
        '-crf 18 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -pix_fmt yuv420p {}'.format(os.path.join(image_path,'{}'.format(object_name)))
    os.system(cmd)


if __name__ == '__main__':
    fire.Fire(image_to_video)



