# Neural Collaborative Filtering
Content-based Neural Collaborative Filtering: https://github.com/udhavsethi/neural_collaborative_filtering

# Our project is forked from the NCF repository: https://github.com/hexiangnan/neural_collaborative_filtering

## Environment Settings
Keras with Theano backend.
- Keras version:  '1.0.7'
- Theano version: '0.8.0'

## Build and Run ContentNCF with Docker

Build docker image
```
docker build --no-cache=true -t content-ncf .
```

Run docker image:
```
docker run --volume=$(pwd):/home content-ncf python ContentNCF.py --dataset content_pin --epochs 5 --batch_size 256 --num_factors 64 --layers [64,32,16,8] --reg_mf 0 --reg_layers [0,0,0,0] --num_neg 4 --lr 0.001 --learner adam --verbose 1 --out 1
```

### Dataset
content_pin dataset - The dataset contains a mapping of boards, which represents users, to their pins, which represents images. This dataset contains 500 users and 24498 user-image interactions.

content_pin.train.rating:
- Train file.
- Each Line is a training instance: userID\t itemID\t rating\t imageURL

test.rating:
- Test file (positive instances).
- Each line is a testing instance: userID\t itemID\t rating\t imageURL

test.negative
- Test file (negative instances).
- Each line corresponds to a line in test.rating, containing additional 99 negative samples.  
- Each line is in the format: (userID,itemID)\t negativeItemID1\t negativeItemID2 ...

features_n.pkl
- Image feature respresentations with dimensions n*1
- To change the number of feature dimensions, change filename in ContenNCF.py and set num_factors=64 in docker run command.
