# -*- coding: utf-8 -*-

import cv2
import json
import matplotlib.pyplot as plt

# In[]]:
folder = '/home/kenny/dgx/home/datasets/ir/'

with open(folder + 'train_data_3ds_extra1.json') as json_file:
    train_data = json.load(json_file)
    annotations = train_data['annotations']
    categories = train_data['categories']
    images = train_data['images']
    info = train_data['info']
    licenses = train_data['licenses']

# In[]]:
for ann in annotations:
    
    ann = annotations[-5000]
    img = cv2.imread('/home/kenny/dgx'+ images[ann['image_id']]['file_name'], 0)
    bbox = ann['bbox']
    cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[0]+bbox[2]), int(bbox[1]+bbox[3])), (255, 0, 0), 2)
    plt.imshow(img, cmap='gray')
    print(categories[ann['category_id']-1]['name'])
    break

# In[]: Analyze
image_ids = []

for ann in annotations:
    image_id = ann['image_id']
    if image_id not in image_ids:
        image_ids.append(image_id)

# In[]: Add extra images to fir images_per_gpu
image_extra = images[0].copy()
image_extra['id'] = len(images)
images.append(image_extra)

ann_extra = annotations[0].copy()
ann_extra['image_id'] = len(images)
ann_extra['id'] = len(annotations)
annotations.append(ann_extra)

# In[]]:
train_data_global = {'annotations': annotations,
                    'categories': categories,
                    'images': images,
                    'info': info,
                    'licenses': licenses}

with open('train_data_3ds_extra1.json', 'w') as outfile:
    json.dump(train_data_global, outfile)

# In[]]:





