import imghdr
from os import listdir
from keras.preprocessing.image import load_img

# extract features from each photo in the directory
def filter_invalid(directory):
	files = listdir(directory)
	# print(files)
	for name in files:
		filename = directory + '/' + name
		try:
			print("{} done".format(filename))
			load_img(filename, target_size=(224, 224))
		except Exception as e:
			print(e)
		# if not imghdr.what(filename):
		# 	print(filename)

directory = './Data/pinterest_images/'
filter_invalid(directory)
