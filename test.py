#test.py

import matplotlib
matplotlib.use('Agg')

from matplotlib import pyplot as plt

f=open("./test.log",'r')
lines = f.readlines()

usage=[]

for line in lines:
    line_split = line.split(" ")
    for s in line_split:
        if s=='freshman':
            usage.append(line_split[18])

plt.plot(usage)
plt.show()
plt.savefig('graph.png')


f.close()
