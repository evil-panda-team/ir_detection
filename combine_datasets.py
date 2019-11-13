# -*- coding: utf-8 -*-

import cv2
from glob import glob
import os
from tqdm import tqdm
import json
import matplotlib.pyplot as plt

# In[]: MIPT DATASET
#folder_mipt = '/home/kenny/dgx/home/datasets/ir/mipt/'
folder_mipt = '/home/datasets/ir/mipt/'

# In[]:
with open(folder_mipt + 'train.json') as json_file:
    train_data = json.load(json_file)
    annotations_mipt = train_data['annotations']
    categories_mipt = train_data['categories']
    images_mipt = train_data['images']
        
# In[]:
for ann in annotations_mipt:
    ann['bbox'] = list(map(int, ann['bbox']))
    x, y, w, h = ann['bbox']
    ann['segmentation'] = [[x, y, x, y+h, x+w, y+h, x+w, y]]
    
for img in images_mipt:
    img['file_name'] = folder_mipt + 'images/' + img['name']
    del(img['name'])
    
objects_count = len(annotations_mipt)
images_count = len(images_mipt)

#train_data_mipt = {'annotations': annotations_mipt,
#                    'categories': categories_mipt,
#                    'images': images_mipt,
#                    'info': {'contributor': 'no contributor specified',
#                             'date_created': 'today',
#                             'description': '',
#                             'url': 'no url specified',
#                             'version': 1.0,
#                             'year': 2019},
#                    'licenses': []
#                    }

#with open('train_data_mipt.json', 'w') as outfile:
#    json.dump(train_data_mipt, outfile)
    
# In[]:
#for ann in annotations_mipt:
#    
#    ann = annotations_mipt[917]
#    img = cv2.imread(images_mipt[ann['image_id']]['file_name'], 0)
#    bbox = ann['bbox']
#    cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3])), (255, 0, 0), 2)
#    plt.imshow(img, cmap='gray')
#    print(categories_mipt[ann['category_id']-1]['name'])
#    
#    break

# In[]: FLIR DATASET
#folders_flir = ['/home/kenny/dgx/home/datasets/ir/flir/train/', '/home/kenny/dgx/home/datasets/ir/flir/val/', '/home/kenny/dgx/home/datasets/ir/flir/video/']
folders_flir = ['/home/datasets/ir/flir/train/', '/home/datasets/ir/flir/val/', '/home/datasets/ir/flir/video/']

# In[]:
for folder_flir in folders_flir:

    with open(folder_flir + 'thermal_annotations.json') as json_file:
        train_data = json.load(json_file)
        annotations_flir = train_data['annotations']
        images_flir = train_data['images']

    for i,ann in enumerate(annotations_flir):
        ann['id'] = ann['id'] + objects_count
        ann['image_id'] = ann['image_id'] + images_count
        if ann['category_id'] > 3 or ann['category_id'] == 2:
            annotations_flir[i] = None
        elif ann['category_id'] == 3:
            ann['category_id'] = 2
            
    for img in images_flir:
        img['file_name'] = folder_flir + img['file_name']
        img['id'] = img['id'] + + images_count
        
    objects_count += len(annotations_flir)
    images_count += len(images_flir)
            
    if 'train' in folder_flir:
        annotations_flir_train = [i for i in annotations_flir if i]
        images_flir_train = images_flir
    elif 'val' in folder_flir:
        annotations_flir_val = [i for i in annotations_flir if i]
        images_flir_val = images_flir
    elif 'video' in folder_flir:
        annotations_flir_video = [i for i in annotations_flir if i]
        images_flir_video = images_flir

# In[]:
annotations_global = annotations_mipt + annotations_flir_train + annotations_flir_val + annotations_flir_video
images_global = images_mipt + images_flir_train + images_flir_val + images_flir_video
categories_global = categories_mipt

del(annotations_mipt, annotations_flir, annotations_flir_train, annotations_flir_val, annotations_flir_video)
del(images_mipt, images_flir, images_flir_train, images_flir_val, images_flir_video)

train_data_global = {'annotations': annotations_global,
                    'categories': categories_global,
                    'images': images_global,
                    'info': train_data['info'],
                    'licenses': train_data['licenses']}

with open('train_data_global.json', 'w') as outfile:
    json.dump(train_data_global, outfile)

# In[]: Visualize
#for ann in annotations_global:
#    
#    ann = annotations_global[1226]
#    img = cv2.imread(images_global[ann['image_id']]['file_name'], 0)
#    bbox = ann['bbox']
#    cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3])), (255, 0, 0), 2)
#    plt.imshow(img, cmap='gray')
#    
#    break

# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




