import re
import numpy as np

def read_data(filename, m, n):
    a = np.zeros([m,n])
    with open(filename) as my_file:
        max_u = 0
        for line in my_file:

            line = re.findall(r"[\w']+", line)

            u = int(line[0])
            i = int(line[1])

            a[u][i] = 1

    a = np.array(a)
    return a

file_test = '../Preprocessing/filtered_data/pinterest.test'
array_test = read_data(file_test, 500+1, 20147+1)
array_test = np.array(array_test)

file_neg = 'check_neg.txt'
f = open(file_neg, "w")
with open(file_test) as my_file:
    for line in my_file:

        line = re.findall(r"[\w']+", line)

        u = int(line[0])
        i = int(line[1])

        f.write("({},{})".format(u, i))
        row = array_test[u]
        row_z = np.where(row == 0)[0]
        np.random.shuffle(row_z)
        count = 0
        for item in row_z:
            f.write("\t{}".format(item))
            count = count + 1
            if count > 10:
                break
        f.write("\n".format())
        print("line done")

f.close()
