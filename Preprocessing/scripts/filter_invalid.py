import imghdr
from os import listdir
from keras.preprocessing.image import load_img

def filter_invalid(directory):
	files = listdir(directory)
	for name in files:
		filename = directory + '/' + name
		try:
			print("checking {}..".format(filename))
			load_img(filename, target_size=(224, 224))
		except Exception as e:
			print(e)

directory = './Data/pinterest_images/'
filter_invalid(directory)
