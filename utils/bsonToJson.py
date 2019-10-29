import bson

from bson.json_util import dumps
from bson.json_util import loads

with open("subset_iccv_board_cate.bson", "rb") as inFile:
    bsonData = inFile.read()

# TODO: doesn't do a clean json dump
jsonData = bson.decode_all(bsonData)

print(jsonData)

