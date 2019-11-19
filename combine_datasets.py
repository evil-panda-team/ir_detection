# -*- coding: utf-8 -*-

import cv2
from glob import glob
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
        img['id'] = img['id'] + images_count
        
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
    
    j = 0
    for i, file in tqdm(enumerate(files)):
        with open(file) as f:
            for line in f:
                cl, x, y, w, h = line[:-1].split(" ")
                if int(cl) < 2:
                    w = float(w)*width
                    h = float(h)*height
                    x = int(float(x)*width - w/2)
                    y = int(float(y)*height - h/2)
                    annotation = {'area': w*h,
                                  'bbox': [x, y, int(w), int(h)],
                                  'category_id': int(cl) + 1,
                                  'id': j + objects_count,
                                  'image_id': i + images_count,
                                  'iscrowd': 0,
                                  'segmentation': [x, y, x, y + int(h), x + int(w), y + int(h), x + int(w), y] 
                                  }
                    annotations_tokyo.append(annotation)
                    j += 1
            
        image = {'file_name': file.replace('labels', 'Images').replace('.txt', '.png'),
             'height': height,
             'id': i + images_count,
             'width': width,
        }
        
        images_tokyo.append(image)
            
    objects_count += len(annotations_tokyo)
    images_count += len(images_tokyo)

    if 'fir' in folder_tokyo:
        annotations_tokyo_fir = [i for i in annotations_tokyo if i]
        images_tokyo_fir = images_tokyo
    elif 'mir' in folder_tokyo:
        annotations_tokyo_mir = [i for i in annotations_tokyo if i]
        images_tokyo_mir = images_tokyo
    elif 'nir' in folder_tokyo:
        annotations_tokyo_nir = [i for i in annotations_tokyo if i]
        images_tokyo_nir = images_tokyo

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

with open('train_data_3ds.json', 'w') as outfile:
    json.dump(train_data_global, outfile)