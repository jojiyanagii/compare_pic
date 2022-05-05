from PIL import Image
import cv2 

IMG_SIZE = (200, 200)
target_img = cv2.imread("target_file")
target_img = cv2.resize(target_img, IMG_SIZE)
target_hist = cv2.calcHist([target_img], [0], None, [256], [0,256])

comparing_img = cv2.imread("/Users/yanagii/Code/compare_pics/comparing_file")
comparing_img = cv2.resize(comparing_img, IMG_SIZE)
comparing_hist = cv2.calcHist([comparing_img], [0], None, [256], [0,256])

ret = cv2.compareHist(target_hist, comparing_hist, method=0)

print(ret)
