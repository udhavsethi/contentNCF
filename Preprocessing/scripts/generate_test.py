filename = 'pinterest.data'

with open(filename) as f:
    lines = f.readlines()

# remove whitespace characters
lines = [x.strip() for x in lines]

train_file = open("pinterest.train", "w")
test_file = open("pinterest.test", "w")

# Num training samples per test sample
EVERY_NTH_SAMPLE = 20

for i in range(len(lines)):
    user_id, img_id, img_url = lines[i].split('\t')
    if i % EVERY_NTH_SAMPLE == 0:
        test_file.write("{}\t{}\t{}\n".format(user_id, img_id, img_url))
    else:
        train_file.write("{}\t{}\t{}\n".format(user_id, img_id, img_url))


train_file.close()
test_file.close()