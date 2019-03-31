import os
from urllib.parse import urlparse


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name,"crawled.txt")
    if not os.path.isfile(queue):
        file_writer(queue, base_url)
    if not os.path.isfile(crawled):
        file_writer(crawled, '')


def file_writer(path, data):
    f = open(path,'w')
    f.write(data)

def append_file(path, data):
    with open(path,'a') as file:
        file.write(data+'\n')

def del_f_content(path):
    open(path,'w').close()


def ftoset(file_name):
    results = set()
    f = open(file_name,'rt')
    for line in f:
        results.add(line.replace('\n',''))
    return results


def settof(links, file_name):
    f = open(file_name,"w")
    for l in sorted(links):
        f.write(l+"\n")


def domain_name(url):
    try:
        results = subdomain(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


def subdomain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


