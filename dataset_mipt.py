# -*- coding: utf-8 -*-

import cv2
from glob import glob
import os
from tqdm import tqdm
import json
import matplotlib.pyplot as plt

# In[]:
#folder = '/home/kenny/dgx/home/datasets/ir/mipt/'
folder = '/home/datasets/ir/mipt/'

# In[]:
with open(folder + 'test_info.json') as json_file:
    train_data = json.load(json_file)
#    annotations = train_data['annotations']
    categories = train_data['categories']
    images = train_data['images']
    
for img in images:
    img['file_name'] = folder + 'images/' + img['name']
    del(img['name'])
    
test_data = {'categories': categories,
             'images': images
             }
    
with open('test_data.json', 'w') as outfile:
    json.dump(test_data, outfile)

# In[]:
#for ann in annotations:
#    
#    ann = annotations[2]
#    img = cv2.imread(folder + 'images/' + images[ann['image_id']]['name'], 0)
#    bbox = ann['bbox']
#    cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3])), (255, 0, 0), 2)
#    plt.imshow(img)
#    
#    break



# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




# In[]:




