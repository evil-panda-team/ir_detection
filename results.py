# -*- coding: utf-8 -*-

import cv2
from glob import glob
import os
from tqdm import tqdm
import json
import matplotlib.pyplot as plt
import pickle

# In[]:

#[{
#"image_id" : int, "category_id" : int, "bbox" : [x,y,width,height], "score" : float,
#}]

# In[]:
folder = 'results/1/'

with open(folder + 'res1.pkl', 'rb') as f:
    results = pickle.load(f)

# In[]:
res_list = []

thresh = 0.25

for i, res in enumerate(results):
    persons = res[0]
    for person in persons:
        x,y,x2,y2,s = person
        w = x2-x
        h = y2-y
        if s > thresh:
            res_list.append({"image_id" : i, 
                             "category_id" : 1, 
#                             "bbox" : [round(x, 1), round(y, 1), round(w, 1), round(h, 1)], 
#                             "score" : round(s, 1)
                             "bbox" : [float(x), float(y), float(w), float(h)], 
                             "score" : float(s)
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
                             "score" : float(s)
                             })

# In[]:
with open(folder + 'dt.json', 'w') as outfile:
    json.dump(res_list, outfile)

# In[]:





# In[]:





# In[]:




