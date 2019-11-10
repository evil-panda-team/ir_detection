# -*- coding: utf-8 -*-

import cv2
from glob import glob
import os
from tqdm import tqdm
import json
import matplotlib.pyplot as plt

# In[]:
folder ='../../datasets/ir/mipt/'
images = [f for f in glob(folder + 'images/*.png', recursive=True)]
images.sort()

# In[]:
with open(folder + 'train.json') as json_file:
    train_data = json.load(json_file)
    annotations = train_data['annotations']
    categories = train_data['categories']
    images = train_data['images']

# In[]:
for ann in annotations:
    
    ann = annotations[2]
    img = cv2.imread(folder + 'images/' + images[ann['image_id']]['name'], 0)
    bbox = ann['bbox']
    cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3])), (255, 0, 0), 2)
    plt.imshow(img)
    
    break



# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




