# {"image_id": 378092,"id": 631103,"caption": "A couple of young men playing a wii game console at a convention. "}


import json 

with open("../data/coco/annotations/captions_train2014.json", "r") as f:
    data = json.load(f)

#print(data.keys())
#print(data['images'][0])
#print(data['annotations'][0])

image_files = {} # image_id -> filename
for image in data['images']:
    image_files[image['id']] = image['file_name']

#print(len(image_files))
#print(list(image_files.items())[:3])

captions = {} # image_id -> [captions]
for annotation in data['annotations']:
    if annotation['image_id'] in captions:
        captions[annotation['image_id']].append(annotation['caption'])
    else:
        captions[annotation['image_id']] = [annotation['caption']]

#some_id = next(iter(image_files))
#print(image_files[some_id])
#print(captions[some_id])
