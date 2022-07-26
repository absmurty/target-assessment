import os
from datetime import datetime
startTime = datetime.now()
Folderpath = '/Users/sakella/Downloads/Images'
maxSize, maxFile = 0, '' 
# get size
for path, _, files in os.walk(Folderpath):
    for f in files:
        try:
            fp = os.path.join(path, f)
            size = os.path.getsize(fp)
            if size > maxSize:
                maxSize = size
                maxFile = f
        except:
            pass
endTime = datetime.now()
# display size
print(maxFile, maxSize, endTime-startTime)
