#!/usr/bin/env python
# coding: utf-8

import bson
import requests
import json, re
from bson import json_util

pins_bson = open('pinterest_iccv/subset_iccv_board_pins.bson', 'rb').read()
board_to_pins = {}
for obj in bson.decode_all(pins_bson):
    key = obj['board_id']
    val = obj['pins']
    board_to_pins[key] = val
print("Number of users: {}".format(len(board_to_pins)))


im_bson = open('pinterest_iccv/subset_iccv_pin_im.bson', 'rb').read()
pin_to_img = {}
for obj in bson.decode_all(im_bson):
    key = obj['pin_id']
    val = obj['im_url']
    pin_to_img[key] = val
print("Number of pins: {}".format(len(pin_to_img)))


def download_image(img_url, img_id):
    '''
    Download image from url and save as img_id.jpg
    '''
    img_obj = requests.get(img_url, allow_redirects=True)
    open('pinterest_images/{}.jpg'.format(img_id), 'wb').write(img_obj.content)


# Write data to file in format:  user_id img_id img_url
img_to_id = {}
board_to_userid = {}
user_id = 0
img_id = 0

filepath = './users_to_images.train'
f = open(filepath, "w")

for board_id, pins in board_to_pins.items():
    # find user_id corresponding to board_id
    if board_id in board_to_userid:
        user_id = board_to_userid[board_id]
    else:
        board_to_userid[board_id] = user_id
        user_id = user_id + 1
    for pin in pins:
        if pin in pin_to_img:
            img_url = pin_to_img[pin]
            
            # find img_id corresponding to img_url
            if img_url in img_to_id:
                img_id = img_to_id[img_url]
            else:
                img_to_id[img_url]= img_id
                download_image(img_url, img_id)
                img_id = img_id+1            

            # write dataset to file
            f.write("{}\t{}\t{}\n".format(user_id, img_id, img_url))
f.close()
