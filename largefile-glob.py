import glob
import os
from datetime import datetime
startTime = datetime.now()
dir_name = '/Users/sakella/Downloads/Images/'
# Get list of files in a directory & sub-directories
list_of_files = filter( os.path.isfile,
                        glob.glob(  dir_name + '/**/*',
                                    recursive=True) )
# Find the file with max size from the list of files
max_file = max( list_of_files,
                key =  lambda x: os.stat(x).st_size)
endTime = datetime.now()
print(max_file, os.stat(max_file).st_size, endTime-startTime)
