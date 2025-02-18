
import os
import sys

# content = '<center><a href="{}">%s</a></br><video src="{}%s" controls="controls" width="800px"></video></center></br></br>'.format(sys.argv[1], sys.argv[1])
content = '<center><a href="{}">%s</a></br><img src="{}%s" width="800px"></img></center></br></br>'.format(sys.argv[1], sys.argv[1])
text = ""

img_format = ['.jpg', '.png', '.jpeg','.JPG','.JPEG','.PNG']

# for f in os.listdir("x./assets"):
#     text += content % (f, f)
imgs = os.listdir(sys.argv[1])

def sorted_by_order(imgs):
    new_imgs = []
    for f in imgs:
        for stem in img_format:
            if stem in f:
                break
        else:
            continue
        new_imgs.append(f)

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

        return int(img[left:right], base = base)







    new_imgs = [(obtain_digit(img.split('.')[0], base = 10), img) for img in new_imgs]
    new_imgs = sorted(new_imgs, key = lambda x:x[0])
    new_imgs = [img[1] for img in new_imgs]
    return new_imgs


imgs = os.listdir(sys.argv[1])
imgs = sorted_by_order(imgs)


for f in imgs:

    text += content % (f, f)

with open("./index.html","w", encoding="utf-8") as f:
    f.write(text)
