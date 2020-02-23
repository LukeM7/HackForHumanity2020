from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from glob import glob
import os
import json
from test import SortImageName
# name, grade, 3 bullet points, source
dictionary = {'Pepsi': {0: 'D',
                        1: 'PepsiCo has managed to decrease its total climate footprint from 2014 to 2017.'
                           'PepsiCo scores poorly because the brand remains secretive in its sustainability report'
                           ' and refuses to disclose information. PepsiCo mentions target to reduce carbon emissions.',
                        2: 'https://rankabrand.org/soda/Pepsi'},
              'Coke': {0: 'D',
                       1: 'Coca-Cola Company implements measures to reduce emissions, but has still increased in overall climate footprint.'
                          'The company mentions using renewable energy, but is not clear about how much.'
                          'Coca-Cola Company implements measures to purchase its other products, such as coffee, tea and fruits,'
                          ' from sustainable sources',
                       2: 'https://rankabrand.org/soda/Coca-Cola'},
              'Yerba': {0: 'B',
                        1: 'Guayaki harvests yerba in an organic and ecologically friendly manner.'
                            ' Guayaki actively contributes to environmental protection by working to restore 200,000 acres of rainforest. '
                            'The company creates 1,000 living wage jobs for local workers.',
                        2: 'https://magazine.wellwallet.com/gold-indios-guayakis-yerba-mate-ushering-sustainable-economy'},
              'Kettle Brand': {0: 'B',
                               1: 'After cooking chips with vegetable oil, Kettle Brand converts excess oil to biodiesel to fuel their vehicles.'
                                  ' In 2019, Kettle Brand chips cut the amount of materials used in packaging by 43%,'
                                  'reducing greenhouse gas emissions from packaging by 51% and waste from packaging by 2 million pounds.',
                               2: 'https://www.kettlebrand.com/sustainability/'},
              'Fiji': {0: 'A',
                       1: 'B',
                       2: 'C'},
              'Smartwater': {0: 'D',
                             1: 'Coca-Cola Company implements measures to reduce emissions, but has still increased in overall climate footprint.'
                                'The company mentions using renewable energy, but is not clear about how much.'
                                'Coca-Cola Company implements measures to purchase its other products, such as coffee, tea and fruits,'
                                ' from sustainable sources',
                             2: 'https://rankabrand.org/soda/Coca-Cola'}
              }
newArray = []
app = ClarifaiApp(api_key='a83ecce289b64338a8036f3603e8d551')

def main():
    model1 = app.models.get('Brand')
    url = input("URL of image: ")
    output = model1.predict_by_url(url)['outputs'][0]['data']['concepts']
    newJson = json.dumps(output[0])
    completeJson = json.loads(newJson)
    print(completeJson['name'])
    for key in dictionary:
        isfound = False
        if key == completeJson['name']:
            newArray.append(key)
            for size in range(0, 3):
                newArray.append(dictionary[key][size])
            isfound = True
            break
    if isfound:
        print(newArray)
        return newArray
    else:
        print("None found")
        return None

if __name__ == '__main__':
    main()
