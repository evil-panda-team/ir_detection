import cv2 
import os
import glob

dataset_path = '/home/rauf/datasets/ir/'
mipt_dataset_path = dataset_path + 'mipt/images/'
mipt_normilized_dataset_path = dataset_path + 'mipt/images_normilized_hist/'
os.makedirs(mipt_normilized_dataset_path, exist_ok=True)

files = [f for f in glob.glob(mipt_dataset_path + "*.png", recursive=True)]

for f in files:
    img = cv2.imread(f,0)
    img = cv2.equalizeHist(img)
    #cv2.normalize(img, img, 0, 255, cv2.NORM_MINMAX)
    cv2.imwrite('{}{}'.format(mipt_normilized_dataset_path,f.split('/')[-1]), img)


