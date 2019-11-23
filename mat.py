# -*- coding: utf-8 -*-

import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import scipy.io

# In[]]:
folder = '/home/kenny/dgx/home/datasets/ir/'

mat = scipy.io.loadmat(folder+ 'GNT.mat')

# In[]:
GNT = mat['GNT']

# In[]:
images_count = 0
objects_count = 0

#/home/kenny/dgx/home/datasets/ir/Pedestrian/Data/seq1/thermal/thermal_0000001.jpg

annotations_pedestrian = []
images_pedestrian = []

for i, gnt in enumerate(GNT):
    for gn in gnt:
        for g in gn:
            objects_count += 1
            x, y, w, h, frame_id, pedestrian_id = g.astype(int)
            print(frame_id)
            annotation = {'area': w*h,
                          'bbox': [x, y, w, h],
                          'category_id': 1,
                          'id': objects_count,
                          'image_id': frame_id + images_count - 1,
                          'iscrowd': 0,
                          'segmentation': [[x, y, x, y + h, x + w, y + h, x + w, y]] 
                          }
            annotations_pedestrian.append(annotation)
    
    for idx in range(len(gn)//pedestrian_id):
        image = {'file_name': folder + 'Pedestrian/Data/seq{}/thermal/thermal_{:07d}.jpg'.format(i+1, idx+1),
                 'height': 480,
                 'id': images_count,
                 'width': 640,
        }
        images_pedestrian.append(image)
        images_count += 1
            
# In[]:



# In[]:





# In[]:





# In[]:





