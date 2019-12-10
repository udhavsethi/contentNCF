filename = 'temp_500_users_to_images.train'

with open(filename) as f:
    lines = f.readlines()

# remove whitespace characters
lines = [x.strip() for x in lines]

NUM_TEST = 2450

i=0
test_iter=0
while i < len(lines) and test_iter < NUM_TEST:
    tuser_id, timg_id, timg_url = lines[i].split('\t')
    
    print("i: {}, tuser_id: {}, timg_id: {}".format(i, tuser_id, timg_id))
    i = i+10
    test_iter = test_iter+1
