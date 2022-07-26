import os
from datetime import datetime
startTime = datetime.now()
Folderpath = '/Users/sakella/Downloads/Images'
#making lists of sizes and paths of the files with maximum sizes
maxSizes, maxFiles = [], []


for pathz, _,files in os.walk(Folderpath):
    for f in tuple(files):
        try:
            fp = os.path.join(pathz, f)
            size = os.path.getsize(fp)
           
            #if there are less than 5 files, even the smallest of sizes will be in the largest files
            if len(maxSizes) <= 4:
                maxSizes.append(size)
                maxFiles.append(fp)
           
            #if there is a large file, remove the smallest file from the lists and replace it with the new one
            elif size > min(maxSizes):
                smallest = min(maxSizes)
                maxSizes[maxSizes.index(smallest)] = size
                maxFiles[maxSizes.index(smallest)] = fp
        except:
            pass
endTime = datetime.now()
# display size
print(maxFiles, maxSizes, endTime-startTime)
