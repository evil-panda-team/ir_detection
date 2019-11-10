# -*- coding: utf-8 -*-

import cv2
from glob import glob
import os
from tqdm import tqdm
import json
import matplotlib.pyplot as plt

# In[]:
folder ='../../datasets/ir/flir/'
images = [f for f in glob(folder + 'train/thermal_8_bit/*.jpeg', recursive=True)]
images.sort()

# In[]:
with open(folder + 'train/thermal_annotations.json') as json_file:
    train_data = json.load(json_file)
    annotations = train_data['annotations']
    categories = train_data['categories']
    images = train_data['images']

# In[]:
for ann in annotations:
    
    ann = annotations[1]
    img = cv2.imread(folder + 'train/' + images[ann['image_id']]['file_name'], 0)
    bbox = ann['bbox']
    category = categories[ann['category_id']-1]['name']
    
    cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3])), (255, 0, 0), 2)
    plt.imshow(img, cmap='gray')
    
    break

#    print(category)



# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




