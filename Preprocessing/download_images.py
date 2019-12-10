#!/usr/bin/env python
# coding: utf-8

import requests
import os.path

def download_image(img_id, img_url):
    '''
    Download image from url and save as img_id.jpg
    '''
    img_obj = requests.get(img_url, allow_redirects=True)
    open('pinterest_images/{}.jpg'.format(img_id), 'wb').write(img_obj.content)


filename = '500_users_to_images.train'
with open(filename) as f:
    lines = f.readlines()

# remove whitespace characters
lines = [x.strip() for x in lines]

# imgid_to_url = {}

for line in lines:
    user_id, img_id, img_url = line.split('\t')
    if os.path.isfile('pinterest_images/{}.jpg'.format(img_id)):
    # if image is already downloaded:
        print("Image already saved for image id: {}".format(img_id))
    else:
        # imgid_to_url[img_id] = img_url
        print("Downloading image for image id: {}".format(img_id))
        download_image(img_id, img_url)