
import fire
import sys
sys.path.append("./")
import os
import glob

def video_show(input_dir):

    cmd = f'bash ~/.vim/bins/GAPVideoViewer/run_img.sh {input_dir}'
    os.system(cmd)

if __name__ == '__main__':
    fire.Fire(video_show)

