import cv2
import numpy as np
import os

FOLDER = "data"
files = os.listdir(FOLDER)
print(files)

IMAGES =[]
for file in files:
    PATH = os.path.join(FOLDER,file)
    print(PATH)
    img = cv2.imread(PATH)
    img = cv2.resize(img,(0,0),None,0.2,0.2)
    cv2.imshow(PATH,img)
    IMAGES.append(img)

stitcher = cv2.Stitcher.create()
print("start")
(status,result) = stitcher.stitch(IMAGES)
print("Done")
if status == cv2.STITCHER_OK:
    print("success")
    cv2.imshow(FOLDER,result)
else:
    print("FAILED !")
cv2.waitKey(0)