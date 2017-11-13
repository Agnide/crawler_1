import os

def make_project_directory(directory):
# This is how the exists module is used
    if not os.path.exists(directory):
        print 'Creating directory', directory
        os.makedirs(directory)

    else:
        exit(0)

def create_files(name, base_url):
    queue = name + '/queue.txt'
    crawled = name + '/crawled.txt'
# This is how file existence is checked (isfile)
# These functions are used as shown - os.path.exists('name of dir to check')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# This function is for making and writing content in files, used in function above        
def write_file(filename, data):
    f = open(filename, 'w')
    f.write(data)
    f.close()

# Function to add links to file
# Path = filename (directory)
def add_links(filename, data):
    with open(filename, 'a') as file_name: # Equivalent to file_name = open(filename, 'a')
        file_name.write(data + '\n')

# Function to delete links from file
def delete_links(filename):
    with open(filename, 'w'):
        pass # Just does nothing

# Read file, put links in set
def file_to_set(filename):
    results = set()
    with open(filename, 'r') as f:
        for line in f:
            # Just to replace \n 
            results.add(line.replace('\n', ''))

# Put links in set into file
def set_to_file(links_set, filename):
    delete_links(filename)
    for link in links_set: # Can also add sorted(links_set)
        add_links(filename, link)
        
