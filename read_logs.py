#read the log files and sort them according to file name. Then integrate them to on file.

import os

path = os.path.abspath('.')
path_list = os.listdir(path + '/logs/')
os.chdir(path + '/logs/')
if os.path.exists('CTP.log'):
    os.rename('CTP.log','CTP-0.log')
if os.path.exists('output.log'):  #remove old output file
     os.remove('output.log')
path_list = os.listdir(path + '/logs/')

#read logs
with open('output.log', 'w') as outfile:
    for filename in path_list:
        with open(filename) as infile:
            outfile.write(infile.read().rstrip()+'\n')

logfile = open('output.log', 'r')           
line = logfile.readlines()
count = len(line)
delttime = [1.0, 1.0, 1.0]
#read time point
pretime = [float(line[0][11:13]), float(line[0][14:16]), float(line[0][17:23])]
for i in range(1, count):
    curtime = [float(line[i][11:13]), float(line[i][14:16]), float(line[i][17:23])]
    for j in range(0, 3):
        delttime[j] = curtime[j] - pretime[j]
    pause = delttime[0]*3600 + delttime[1]*60 + delttime[2]
    if abs(pause) > 5:
        print("%s  log interuption occur in line: %d" % (delttime, (i+1)))

    pretime = curtime

input("Press Enter")

