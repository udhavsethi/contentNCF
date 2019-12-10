infile = open('500_users_to_images.train', 'r')
outfile = open('pinterest.data', 'w')

for line in infile.readlines():
    user_id, img_id, img_url = line.strip().split('\t')
    dec_user_id = str(int(user_id) - 1)
    outfile.write("{}\t{}\t{}\n".format(dec_user_id, img_id, img_url))

infile.close()
outfile.close()
