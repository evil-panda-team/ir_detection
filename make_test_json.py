import json

dataset_path = '/home/rauf/datasets/ir/'
mipt_dataset_path = dataset_path + 'mipt/'
mipt_json_file = mipt_dataset_path + 'test_info.json'

with open(mipt_json_file, "r") as mipt_read_file:
    mipt_data = json.load(mipt_read_file)
    for img in mipt_data['images']:
        img['file_name'] = img['name']
    with open("test_mipt.json", "w") as write_file:
        json.dump(mipt_data, write_file)
    
