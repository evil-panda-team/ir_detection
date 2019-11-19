from mmdet.apis import init_detector, inference_detector, show_result
import mmcv
import json
import tqdm

config_file = 'my_configs/cascade_rcnn_hrnetv2p_w32_20e.py'
checkpoint_file = 'work_dir/cascade_rcnn_hrnetv2p_w32/latest.pth'


dataset_path = '/home/rauf/datasets/ir/'
mipt_dataset_path = dataset_path + 'mipt/images/'
mipt_json_file = 'test_mipt.json'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

show_res = True
predictions = []
threshold = 0.1

with open(mipt_json_file, "r") as mipt_read_file:
    mipt_data = json.load(mipt_read_file) 
    for img in tqdm.tqdm(mipt_data['images']):
        file_path = mipt_dataset_path + img['file_name']
        result = inference_detector(model, file_path)

        persons = result[0]
        cars = result[1]

        for car in cars:
            pred = {}
            pred['image_id'] = img['id']
            pred['category_id'] = 2
            x = car[0]
            y = car[1]
            w = car[2]-car[0]
            h = car[3]-car[1]
            score = car[4]
            pred['bbox'] = [float(x),float(y),float(w),float(h)]
            pred['score'] = float(score)
            if score >= threshold:
                predictions.append(pred)

        for person in persons:
            pred = {}
            pred['image_id'] = img['id']
            pred['category_id'] = 1
            x = person[0]
            y = person[1]
            w = person[2]-person[0]
            h = person[3]-person[1]
            score = person[4]
            pred['bbox'] = [float(x),float(y),float(w),float(h)]
            pred['score'] = float(score)
            if score >= threshold:
                predictions.append(pred)

        if show_res:
            show_result(file_path, result, model.CLASSES, show=False, out_file='results/' + img['file_name'])


with open("dt.json", "w") as write_file:
    json.dump(predictions, write_file)