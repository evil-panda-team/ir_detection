# -*- coding: utf-8 -*-

import cv2
from glob import glob
import os
from tqdm import tqdm
import json
import matplotlib.pyplot as plt
import pickle

# In[]:
folder = 'results/combined/'

with open(folder + 'res_combined.pkl', 'rb') as f:
    results = pickle.load(f)

# In[]:
res_list = []

thresh = 0.0001

for i, res in enumerate(results):
    persons = res[0]
    for person in persons:
        x,y,x2,y2,s = person
        w = x2-x
        h = y2-y
        if s > thresh:
            res_list.append({"image_id" : i, 
                             "category_id" : 1, 
                             "bbox" : [float(x), float(y), float(w), float(h)], 
                             "score" : float(1)
                             })
        
    cars = res[1]
    for car in cars:
        x,y,x2,y2,s = car
        w = x2-x
        h = y2-y
        if s > thresh:
            res_list.append({"image_id" : i, 
                             "category_id" : 2, 
                             "bbox" : [float(x), float(y), float(w), float(h)], 
                             "score" : float(1)
                             })

# In[]:
with open(folder + 'dt.json', 'w') as outfile:
    json.dump(res_list, outfile)

# In[]:





# In[]:





# In[]:




