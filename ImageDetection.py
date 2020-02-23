from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from glob import glob
import os
import json
from test import SortImageName

app = ClarifaiApp(api_key='f8413487d8344c80b9d7aa6b78478d47')

def main():

   # image_set = create_image_set('dataset-resized/metal/', ['metal'])
    #app.inputs.bulk_create_images(image_set)

    #model = app.models.create(model_id="glass", concepts=['glass'])
    #model.train()
    model1 = app.models.get('general')

    url = input("URL of image: ")
    output = model1.predict_by_url(url)['outputs'][0]['data']['concepts']
    newJson = json.dumps(output[0])
    return newJson

#def compare(FilePath):
    #model1 = app.models.get('general')
    #temp = model1.predict_by_url(FilePath)['outputs'][0]['data']['concepts']
    #pyj = json.dumps(temp[0])
    #return pyj

def create_image_set(self,img_path, concepts):
    images = []
    for file_path in glob(os.path.join(img_path, '*.jpg')):
        img = ClImage(filename=file_path, concepts=concepts)
        images.append(img)

    return images

if __name__ == '__main__':
    main()
