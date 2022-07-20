
import os
import sys

# content = '<center><a href="{}">%s</a></br><video src="{}%s" controls="controls" width="800px"></video></center></br></br>'.format(sys.argv[1], sys.argv[1])
content = '<center><a href="{}">%s</a></br><img src="{}%s" width="800px"></img></center></br></br>'.format(sys.argv[1], sys.argv[1])
text = ""

img_format = ['.jpg', '.png', '.jpeg','.JPG','.JPEG','.PNG']

# for f in os.listdir("x./assets"):
#     text += content % (f, f)
for f in sorted(os.listdir(sys.argv[1])):
    for stem in img_format:
        if stem in f:
            break
    else:
        continue

    text += content % (f, f)

with open("./index.html","w", encoding="utf-8") as f:
    f.write(text)
