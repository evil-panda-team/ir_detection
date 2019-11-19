import json

dataset_path = '/home/rauf/datasets/ir/'
mipt_dataset_path = dataset_path + 'mipt/'
flir_dataset_path = dataset_path + 'flir/'
mipt_json_file = mipt_dataset_path + 'train.json'
flir_json_file = flir_dataset_path + 'train/thermal_annotations.json'
flir_json_file_val = flir_dataset_path + 'val/thermal_annotations.json'
flir_json_file_video = flir_dataset_path + 'video/thermal_annotations.json'

ann_id_offset = 1684
img_id_offset = 413

with open(mipt_json_file, "r") as mipt_read_file, open(flir_json_file, "r") as flir_read_file, open(flir_json_file_val, "r") as flir_read_file_val, open(flir_json_file_video, "r") as flir_read_file_video:
    mipt_data = json.load(mipt_read_file)
    flir_data = json.load(flir_read_file)
    flir_data_val = json.load(flir_read_file_val)
    flir_data_video = json.load(flir_read_file_video)

    for img in mipt_data['images']:
        img['file_name'] = img['name']

    for fl_data in [flir_data, flir_data_val, flir_data_video]:
        for img, ann in zip(fl_data['images'], fl_data['annotations']):
            img['id'] = img['id'] + img_id_offset
            img['file_name'] = img['file_name'].split('/')[1]
            mipt_data['images'].append(img)

            ann['image_id'] = ann['image_id'] + img_id_offset
            ann['id'] = ann['id'] + ann_id_offset

            if ann['category_id'] > 3 or ann['category_id'] == 2 or ann['category_id'] < 0:
                continue
            if ann['category_id'] == 3:
                ann['category_id'] = 2
            mipt_data['annotations'].append(ann)

    with open("train_merged_mipt_flir.json", "w") as write_file:
        json.dump(mipt_data, write_file)
