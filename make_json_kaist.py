import glob
import json

dataset_path = '/home/rauf/datasets/ir/kaist/'
annotations_folder = dataset_path + 'annotations/'
images_folder = dataset_path + 'images/'

sets = ['set00','set01','set02','set03']


img_sizes = {'kaist': {'w': 640, 'h': 480}}


images = []
annotations = []
licenses = []

json_coco_format = {}
counter_img = 0
counter_ann = 0
for st in sets:
    for filepath in glob.iglob('{}/**/*.txt'.format(annotations_folder + st + '/')):
        with open(filepath) as fp:
            lines = fp.readlines()
            file_nm = filepath.split('/')[-1].split('.')[0]
            fldr_nm = filepath.split('/')[-2]

            for i, line in enumerate(lines):
                if i == 0:
                    continue

                values = line.split()
                class_id = values[0]

                x = float(values[1])
                y = float(values[2])
                w = float(values[3])
                h = float(values[4])

                cl_id = 1

                annotation = {
                    'image_id': counter_img,
                    'category_id': cl_id,
                    'id': counter_ann,
                    'bbox': [x, y, w, h],
                    'area': w * h
                }
                annotations.append(annotation)
                counter_ann += 1
            if len(lines) > 1:
                image = {
                    "file_name": st + '/' + fldr_nm + '/' + 'lwir/' +  file_nm + '.jpg',
                    "height": img_sizes['kaist']['h'],
                    "width": img_sizes['kaist']['w'],
                    "id": counter_img
                }
                images.append(image)
                counter_img += 1


info = {
    "description": "KAIST Dataset",
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
]

json_coco_format['info'] = info
json_coco_format['images'] = images
json_coco_format['annotations'] = annotations
json_coco_format['licenses'] = licenses
json_coco_format['categories'] = categories

with open('train_kaist.json', 'w+') as outfile:
    json.dump(json_coco_format, outfile)
