
from os import listdir
from pickle import dump
import pickle
import numpy as np
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.models import Model

# extract features from each image in the directory
def extract_features(directory,num_images, dim_images):
    # load the model
    model = VGG16()
    # re-structure the model
    model.layers.pop()
    model = Model(inputs=model.inputs, outputs=model.layers[-1].output)
    print(model.summary())

    features = np.zeros((num_images, dim_images))
    try:
        for name in listdir(directory):
            print('>%s' % name)
            if name == '.DS_Store':
                continue
            # load an image from file
            filename = directory + '/' + name
            image = load_img(filename, target_size=(224, 224))
            # convert the image pixels to a numpy array
            image = img_to_array(image)
            # reshape data for the model
            image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
            # prepare the image for the VGG model
            image = preprocess_input(image)
            # get features
            feature = model.predict(image, verbose=0)
            # get image id
            image_id = int(name.split('.')[0])
            # store feature
            features[image_id] = feature
    except Exception as e:
        print(e)
    return features

n = 20148
d = 4096
directory = './Data/pinterest_images/'
features = extract_features(directory, n, d)

print('Extracted Features: %d' % len(features))
dump(features, open('./Data/features_4096.pkl', 'wb'))
