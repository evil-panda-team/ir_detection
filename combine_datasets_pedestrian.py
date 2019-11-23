# -*- coding: utf-8 -*-

import cv2
from glob import glob
from tqdm import tqdm
import json
import scipy.io
import numpy as np
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
        
categories_mipt = categories_mipt[:1]

# In[]:        
objects_count = 0
for i, ann in enumerate(annotations_mipt):
    if ann['category_id'] > 3 or ann['category_id'] == 2:
        annotations_mipt[i] = None
        continue
    objects_count += 1
    ann['id'] = objects_count
    ann['bbox'] = list(map(int, ann['bbox']))
    x, y, w, h = ann['bbox']
    ann['segmentation'] = [[x, y, x, y+h, x+w, y+h, x+w, y]]
    
for img in images_mipt:
    img['file_name'] = folder_mipt + 'images/' + img['name']
    del(img['name'])
    
annotations_mipt = [i for i in annotations_mipt if i]
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
#i = 0
#for ann in tqdm(annotations_mipt):
#    
##    ann = annotations_mipt[0]
#    img = cv2.imread(images_mipt[ann['image_id']]['file_name'], 0)
#    bbox = ann['bbox']
#    cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3])), (255, 0, 0), 2)
#    cv2.putText(img, categories_mipt[ann['category_id']-1]['name'], (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
#    plt.imshow(img, cmap='gray')
#    cv2.imwrite("mipt_vis/{}.png".format(i) ,img)
#    i += 1

# In[]: FLIR DATASET
#folders_flir = ['/home/kenny/dgx/home/datasets/ir/flir/train/', '/home/kenny/dgx/home/datasets/ir/flir/val/', '/home/kenny/dgx/home/datasets/ir/flir/video/']
folders_flir = ['/home/datasets/ir/flir/train/', '/home/datasets/ir/flir/val/', '/home/datasets/ir/flir/video/']

# In[]:
for folder_flir in folders_flir:

    with open(folder_flir + 'thermal_annotations.json') as json_file:
        train_data = json.load(json_file)
        annotations_flir = train_data['annotations']
        images_flir = train_data['images']

    for i, ann in enumerate(annotations_flir):
        if ann['category_id'] >= 2:
            annotations_flir[i] = None
            continue
        objects_count += 1
        ann['id'] = objects_count
        ann['image_id'] = ann['image_id'] + images_count
            
    for img in images_flir:
        img['file_name'] = folder_flir + img['file_name']
        img['id'] = img['id'] + images_count
        
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
#train_data_global = {'annotations': annotations_flir_train + annotations_flir_val + annotations_flir_video,
#                    'categories': categories_mipt,
#                    'images': images_flir_train + images_flir_val + images_flir_video,
#                    'info': train_data['info'],
#                    'licenses': train_data['licenses']}
#
#with open('train_data_flir.json', 'w') as outfile:
#    json.dump(train_data_global, outfile)

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
#folders_tokyo = ['/home/kenny/dgx/home/datasets/ir/tokyo/labels/fir/', '/home/kenny/dgx/home/datasets/ir/tokyo/labels/mir/', '/home/kenny/dgx/home/datasets/ir/tokyo/labels/nir/']
folders_tokyo = ['/home/datasets/ir/tokyo/labels/fir/', '/home/datasets/ir/tokyo/labels/mir/', '/home/datasets/ir/tokyo/labels/nir/']

# In[]:
#files = [f for f in glob(folders_tokyo[0] + '*.txt', recursive=True)]
#files.sort()

#for file in tqdm(files):
##    file = files[4]
#    img = cv2.imread(file.replace('labels', 'Images').replace('.txt', '.png'))
#    with open(file) as f:
#        for line in f:
#            cl, x, y, w, h = line[:-1].split(" ")
#            if int(cl) == 1:
#                w = float(w)*640
#                h = float(h)*480
#                x1 = int(float(x)*640 - w/2)
#                y1 = int(float(y)*480 - h/2)
#                x2 = int(x1+w)
#                y2 = int(y1+h)
#                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
#    break
#
#plt.imshow(img)

# In[]:
# 0 - person
# 1 - car

for folder_tokyo in folders_tokyo:
        
    files = [f for f in glob(folder_tokyo + '*.txt', recursive=True)]
    files.sort()

    annotations_tokyo = []
    images_tokyo = []
    
    width = 640 if 'fir' in folder_tokyo else 320
    height = 480 if 'fir' in folder_tokyo else 256
    
    for ind, file in tqdm(enumerate(files)):
        with open(file) as f:
            for line in f:
                cl, x, y, w, h = line[:-1].split(" ")
                if int(cl) < 1:
                    objects_count += 1
                    w = float(w)*width
                    h = float(h)*height
                    x = int(float(x)*width - w/2)
                    y = int(float(y)*height - h/2)
                    annotation = {'area': w*h,
                                  'bbox': [x, y, int(w), int(h)],
                                  'category_id': int(cl) + 1,
                                  'id': objects_count,
                                  'image_id': ind + images_count,
                                  'iscrowd': 0,
                                  'segmentation': [[x, y, x, y + int(h), x + int(w), y + int(h), x + int(w), y]] 
                                  }
                    annotations_tokyo.append(annotation)
            
        image = {'file_name': file.replace('labels', 'Images').replace('.txt', '.png'),
             'height': height,
             'id': ind + images_count,
             'width': width,
        }
        
        images_tokyo.append(image)
            
    images_count += len(images_tokyo)

    if 'fir' in folder_tokyo:
        annotations_tokyo_fir = annotations_tokyo
        images_tokyo_fir = images_tokyo
    elif 'mir' in folder_tokyo:
        annotations_tokyo_mir = annotations_tokyo
        images_tokyo_mir = images_tokyo
    elif 'nir' in folder_tokyo:
        annotations_tokyo_nir = annotations_tokyo
        images_tokyo_nir = images_tokyo
        
# In[]:
#train_data_global = {'annotations': annotations_tokyo_fir + annotations_tokyo_mir + annotations_tokyo_nir,
#                    'categories': categories_mipt,
#                    'images': images_tokyo_fir + images_tokyo_mir + images_tokyo_nir,
#                    'info': train_data['info'],
#                    'licenses': train_data['licenses']}
#
#with open('train_data_tokyo.json', 'w') as outfile:
#    json.dump(train_data_global, outfile)

# In[]:
#folder_pedestrian = '/home/kenny/dgx/home/datasets/ir/Pedestrian/'
folder_pedestrian = '/home/datasets/ir/Pedestrian/'
        
# In[]:
mat = scipy.io.loadmat(folder_pedestrian + 'GNT.mat')
GNT = mat['GNT']
        
# In[]:
annotations_pedestrian = []
images_pedestrian = []

for i, gnt in enumerate(GNT):
    for gn in gnt:
        for g in gn:
            objects_count += 1
            x, y, w, h, frame_id, pedestrian_id = g.astype(int)
            annotation = {'area': int(w*h),
                          'bbox': [int(x), int(y), int(w), int(h)],
                          'category_id': 1,
                          'id': objects_count,
                          'image_id': int(frame_id + images_count - 1),
                          'iscrowd': 0,
                          'segmentation': [[int(x), int(y), int(x), int(y + h), int(x + w), int(y + h), int(x + w), int(y)]] 
                          }
            annotations_pedestrian.append(annotation)
    
    for idx in range(len(gn)//pedestrian_id):
        image = {'file_name': folder_pedestrian + 'Data/seq{}/thermal/thermal_{:07d}.jpg'.format(i+1, idx+1),
                 'height': 480,
                 'id': images_count,
                 'width': 640,
        }
        images_pedestrian.append(image)
        images_count += 1
         
# In[]:
annotations_global = annotations_mipt + annotations_flir_train + annotations_flir_val + annotations_flir_video + annotations_tokyo_fir + annotations_tokyo_mir + annotations_tokyo_nir
images_global = images_mipt + images_flir_train + images_flir_val + images_flir_video + images_tokyo_fir + images_tokyo_mir + images_tokyo_nir
categories_global = categories_mipt

del(annotations_mipt, annotations_flir, annotations_flir_train, annotations_flir_val, annotations_flir_video, annotations_tokyo_fir, annotations_tokyo_mir, annotations_tokyo_nir)
del(images_mipt, images_flir, images_flir_train, images_flir_val, images_flir_video, images_tokyo_fir, images_tokyo_mir, images_tokyo_nir)

train_data_global = {'annotations': annotations_global,
                    'categories': categories_global,
                    'images': images_global,
                    'info': train_data['info'],
                    'licenses': train_data['licenses']}

with open('train_data_pedestrians.json', 'w') as outfile:
    json.dump(train_data_global, outfile)