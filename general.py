import os
from urllib.parse import urlparse


# this variable contains the base url to be crawled
base_url = "https://primates.dev/"

# this code extracts the site name from the URL and stores it in variable "project_name"
o = urlparse(base_url)
x = o.netloc.split('.')
project_name = x[1]

# this code extracts the site name from the URL and stores it in variable "project_name"
o = urlparse(base_url)
x = o.netloc.split('.')
project_name = x[1]

# Function that creates the main project folder
def make_project_dir(path):
    if os.path.exists(path) == False:
        print("Making Home Folder")
        os.makedirs(path)
    else:
        print('Home Folder Already exists')

    if os.path.exists(path + 'images') == False:
        os.makedirs(path + 'images')
    else:
        print('pictures folder already exists')

# Function to create files that store project info, if files do not already exist
def make_project_files(path):
    crawled = path + '/crawled.txt'
    queue = path + '/queue.txt'
    errorLog = path +'/error log.txt'

    if os.path.isfile(crawled) == False:
        print('Making crawled file')
        f = open(crawled, 'w')
        f.write('')
        f.close()

    if os.path.isfile(queue) == False:
        print('Making queue file')
        f = open(queue, 'w')
        f.write(base_url)
        f.close()

    if os.path.isfile(errorLog) == False:
        print('Making Error log')
        f = open(errorLog, 'w')
        f.write('')
        f.close()

    else:
        print("Project files already exist")

def file_to_set(path, set):
    if os.path.isfile(path) == True:
        f = open(path, 'r')
        for line in f:
            set.add(line)
        f.close()
    else:
        print('no data file found to set')

def append_file(path, data):
    if os.path.isfile(path) == True:
        f = open(path, 'a')
        f.write(str(data) + '\n')
        f.close()
    else:
        print('no data file found to append to')

def clear_file(path):
    if os.path.isfile(path) == True:
        f = open(path, 'w')
        f.write('')
        f.close()
    else:
        print('File does not exist')

