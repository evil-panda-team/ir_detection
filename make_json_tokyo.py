import glob
import json

dataset_path = '/home/rauf/datasets/ir/tokyo/'
annotations_folder = dataset_path + 'labels/'
cameras = ['fir', 'mir', 'nir']


img_sizes = {'fir': {'w': 640, 'h': 480},
             'mir': {'w': 320, 'h': 256},
             'nir': {'w': 320, 'h': 256}}


images = []
annotations = []
licenses = []

json_coco_format = {}
counter_img = 0
counter_ann = 0
for cam in cameras:
    for filepath in glob.iglob('{}/*.txt'.format(annotations_folder + cam + '/')):
        with open(filepath) as fp:
            lines = fp.readlines()
            file_nm = filepath.split('/')[-1].split('.')[0]
            image = {
                "file_name": cam + '/' + file_nm + '.png',
                "height": img_sizes[cam]['h'],
                "width": img_sizes[cam]['w'],
                "id": counter_img
            }
            images.append(image)

            for line in lines:
                values = line.split()
                class_id = values[0]
                x_coord = float(values[1]) * img_sizes[cam]['w']
                y_coord = float(values[2]) * img_sizes[cam]['h']
                w_coord = float(values[3]) * img_sizes[cam]['w']
                h_coord = float(values[4]) * img_sizes[cam]['h']
                x = x_coord - w_coord/2
                y = y_coord - h_coord/2
                w = w_coord
                h = h_coord

                cl_id = 0

                if int(class_id) == 0:
                    cl_id = 1
                elif int(class_id) == 1:
                    cl_id = 2
                else:
                    continue

                annotation = {
                    'image_id': counter_img,
                    'category_id': cl_id,
                    'id': counter_ann,
                    'bbox': [x, y, w, h],
                    'area': w * h
                }
                annotations.append(annotation)
                counter_ann += 1
            counter_img += 1


info = {
    "description": "Tokyo Dataset",
    "version": "1.0",
    "year": 2019
}

licenses = [
    {
        "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/",
        "id": 1,
        "name": "Attribution-NonCommercial-ShareAlike License"
    }
]

categories = [
    {"id": 1, "name": 'person'},
    {"id": 2, "name": 'car'}
]

json_coco_format['info'] = info
json_coco_format['images'] = images
json_coco_format['annotations'] = annotations
json_coco_format['licenses'] = licenses
json_coco_format['categories'] = categories

with open('train_tokyo.json', 'w+') as outfile:
    json.dump(json_coco_format, outfile)
