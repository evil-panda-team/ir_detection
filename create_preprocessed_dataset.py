import cv2
import glob
import numpy as np
import os
import tqdm

dataset_path = '/home/rauf/datasets/ir/merged/'
dataset_path_to_save = '/home/rauf/datasets/ir/merged_preprocessed/'
os.makedirs(dataset_path_to_save, exist_ok=True)

folders = ['mipt', 'FLIR', 'FLIR_video','fir','mir','nir']

for fldr in tqdm.tqdm(folders):
    os.makedirs('{}{}/'.format(dataset_path_to_save,fldr), exist_ok=True)
    for ftype in ['png','jpeg','jpg']:
        for filepath in glob.iglob('{}/*.{}'.format(dataset_path + fldr, ftype)):
            img = cv2.imread(filepath,0)
            img_total = np.zeros((img.shape[0],img.shape[1],3))
            img_1 = cv2.equalizeHist(img)
            img_2 = cv2.normalize(img, 0, 255, cv2.NORM_MINMAX)

            img_total[:,:,0]=img
            img_total[:,:,1]=img_1
            img_total[:,:,2]=img_2
    
            cv2.imwrite('{}{}/{}'.format(dataset_path_to_save,fldr,filepath.split('/')[-1]), img_total)
