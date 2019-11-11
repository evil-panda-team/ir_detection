# -*- coding: utf-8 -*-

import os 

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import sys

sys.path.append('../mmdet2/mmdetection/')

from mmdet.apis import init_detector, inference_detector, show_result
import mmcv
from tqdm import tqdm
import pickle
from mmdet.datasets import IRDataset
import json

# In[]:
#folder_mipt = '/home/kenny/dgx/home/datasets/ir/mipt/'
folder_mipt = '/home/datasets/ir/mipt/'

# In[]:
#with open(folder_mipt + 'train.json') as json_file:
#    train_data = json.load(json_file)
#    annotations_mipt = train_data['annotations']
#    categories_mipt = train_data['categories']
#    images_mipt = train_data['images']
    
with open(folder_mipt + 'test_info.json') as json_file:
    test_data = json.load(json_file)
    categories_mipt = test_data['categories']
    images_mipt = test_data['images']
    
# In[]:
config_file = '../mmdet2/mmdetection/configs/ir_cascade_rcnn_x101_32x4d_fpn_1x.py'
#config_file = '../mmdet2/mmdetection/configs/ir_faster_rcnn_r50_fpn_1x.py'

checkpoint_file = '../mmdet2/mmdetection/work_dirs/ir_cascade_rcnn_x101_32x4d_fpn_1x/latest.pth'
#checkpoint_file = '../mmdet2/mmdetection/work_dirs/ir_mipt_cascade_rcnn_x101_32x4d_fpn_1x/latest.pth'
#checkpoint_file = '../mmdet2/mmdetection/work_dirs/ir_mipt_faster_rcnn_r50_fpn_1x/latest.pth'

model = init_detector(config_file, checkpoint_file, device='cuda:0')

thresh = 0.5

for i,img in tqdm(enumerate(images_mipt)):
    frame = mmcv.imread(folder_mipt + 'images/' + img['name'])
    results = inference_detector(model, frame)
    results = results[:len(IRDataset.CLASSES)]
    o = show_result(frame, results, IRDataset.CLASSES, score_thr = thresh, show = False, out_file = 'vis/{}.png'.format(i))