# -*- coding: utf-8 -*-

import cv2
from glob import glob
import os
from tqdm import tqdm
import json

import matplotlib.pyplot as plt

# In[]:
folder = '/home/kenny/dgx/home/datasets/ir/tokyo/'

# In[]:


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




