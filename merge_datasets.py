import json

dataset_path = '/home/rauf/datasets/ir/'
mipt_dataset_path = dataset_path + 'mipt/'
flir_dataset_path = dataset_path + 'flir/'
mipt_json_file = mipt_dataset_path + 'train.json'
flir_json_file = flir_dataset_path + 'train/thermal_annotations.json'
flir_json_file_val = flir_dataset_path + 'val/thermal_annotations.json'
flir_json_file_video = flir_dataset_path + 'video/thermal_annotations.json'
tokyo_json_file = 'train_tokyo.json'


with open(mipt_json_file, "r") as mipt_read_file, open(flir_json_file, "r") as flir_read_file, open(flir_json_file_val, "r") as flir_read_file_val, open(flir_json_file_video, "r") as flir_read_file_video, open(tokyo_json_file, 'r') as tokyo_read_file:
    mipt_data = json.load(mipt_read_file)
    flir_data = json.load(flir_read_file)
    flir_data_val = json.load(flir_read_file_val)
    flir_data_video = json.load(flir_read_file_video)
    tokyo_data = json.load(tokyo_read_file)

    for img in mipt_data['images']:
        img['file_name'] = 'mipt/' + img['name']

    img_id_offset = len(mipt_data['images'])
    ann_id_offset = len(mipt_data['annotations'])

    for img in tokyo_data['images']:
        img['id'] = img['id'] + img_id_offset
        mipt_data['images'].append(img)
    for ann in tokyo_data['annotations']:
        ann['image_id'] = ann['image_id'] + img_id_offset
        ann['id'] = ann['id'] + ann_id_offset
        mipt_data['annotations'].append(ann)

    img_id_offset += len(tokyo_data['images'])
    ann_id_offset += len(tokyo_data['annotations'])

    for fl_data, fl_fldr in zip([flir_data, flir_data_val, flir_data_video], ['FLIR', 'FLIR', 'FLIR_video']):
        for img in fl_data['images']:
            img['id'] = img['id'] + img_id_offset
            img['file_name'] = fl_fldr + '/' + img['file_name'].split('/')[1]
            mipt_data['images'].append(img)
        for ann in fl_data['annotations']:
            ann['image_id'] = ann['image_id'] + img_id_offset
            ann['id'] = ann['id'] + ann_id_offset

            if ann['category_id'] > 3 or ann['category_id'] == 2 or ann['category_id'] < 0:
                ann_id_offset-=1
                continue
            if ann['category_id'] == 3:
                ann['category_id'] = 2
            mipt_data['annotations'].append(ann)
        img_id_offset += len(fl_data['images'])
        ann_id_offset += len(fl_data['annotations'])

    
    print(img_id_offset)
    print(ann_id_offset)

    print(len(mipt_data['images']))
    print(len(mipt_data['annotations']))
    with open("train_merged_mipt_flir_tokyo_normilized.json", "w") as write_file:
        json.dump(mipt_data, write_file)
