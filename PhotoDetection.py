from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from glob import glob
import os

def main():
    app = ClarifaiApp(api_key='da7f2b917a15410f862954bb04c5cc22')
    #image_set = create_image_set('dataset-resized/metal/', ['metal'])
    #app.inputs.bulk_create_images(image_set)

    #model = app.models.create(model_id="glass", concepts=['glass'])
    #model.train()
    model1 = app.models.get('general')

    url = input("URL of image: ")
    print(model1.predict_by_url(url)['outputs'][0]['data']['concepts'])


def create_image_set(img_path, concepts):
    images = []
    for file_path in glob(os.path.join(img_path, '*.jpg')):
        img = ClImage(filename=file_path, concepts=concepts)
        images.append(img)

    return images

if __name__ == '__main__':
    main()



