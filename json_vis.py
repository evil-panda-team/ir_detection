# -*- coding: utf-8 -*-

import cv2
import json
import matplotlib.pyplot as plt

# In[]]:
folder = '/home/kenny/dgx/home/datasets/ir/'

with open(folder + 'train_data_3ds.json') as json_file:
    train_data = json.load(json_file)
    annotations = train_data['annotations']
    categories = train_data['categories']
    images = train_data['images']

# In[]]:
for ann in annotations:
    
    ann = annotations[-4100]
    img = cv2.imread('/home/kenny/dgx'+ images[ann['image_id']]['file_name'], 0)
    bbox = ann['bbox']
    cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3])), (255, 0, 0), 2)
    plt.imshow(img, cmap='gray')
    print(categories[ann['category_id']-1]['name'])
    break

# In[]]:





# In[]]:





# In[]]:





# In[]]:





