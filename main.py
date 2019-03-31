import threading
from queue import Queue
from crawler import Crawler
from fiand import *

Project = 'wiki_ped'
startpage = 'https://www.wikipedia.org/'
domain = domain_name(startpage)
queued_f = Project + '/queue.txt'
crawled_f = Project +'/crawled.txt'
threads = 6
queue = Queue()
Crawler(Project, startpage, domain)

def create_crawlers():
    for _ in range(threads):
        t = threading.Thread(target=task)
        t.daemon = True
        t.start()

def task():
    while True:
        url = queue.get()
        Crawler.crawlpage(threading.current_thread().name, url)
        queue.task_done()

def create_task():
    for link in ftoset(queued_f):
        queue.put(link)
    queue.join()
    do_work()

def do_work():
    queued_l = ftoset(queued_f)
    if(len(queued_l) > 0):
        create_task()

create_crawlers()
do_work()





