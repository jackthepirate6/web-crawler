from urllib.request import urlopen
from Link_handler import linkhandler
from fiand import *

class Crawler:

    project = ''
    base_url = ''
    domain = ''
    queuef = ''
    crawledf = ''
    queuedl = set()
    crawledl = set()

    def __init__(self, project, base_url, domain):
        Crawler.project = project
        Crawler.base_url = base_url
        Crawler.domain = domain
        Crawler.queuef = Crawler.project + '/queue.txt'
        Crawler.crawledf = Crawler.project + '/crawled.txt'
        self.start()
        self.crawlpage('First crawler',Crawler.base_url)
     
    
    @staticmethod
    def start():
        create_dir(Crawler.project)
        create_files(Crawler.project, Crawler.base_url)
        Crawler.queuedl = ftoset(Crawler.queuef)
        Crawler.crawledl = ftoset(Crawler.crawledf)

     
    @staticmethod
    def crawlpage(thread_name, page_url):
        if page_url not in Crawler.crawledl:
            Crawler.push_links_to_queue(Crawler.grablinks(page_url))
            Crawler.queuedl.remove(page_url)
            Crawler.crawledl.add(page_url)
            Crawler.update_files()

    
    @staticmethod
    def grablinks(page_url):
        htmlstring = ''
        try:
            response = urlopen(page_url)
            if 'txt/html' in response.getheader('Content-Type'):
                htmlbytes = response.read()
                htmlstring = htmlbytes.decode("utf-8")
            handler = linkhandler(Crawler.base_url, page_url)
            handler.feed(htmlstring)
        except Exception as e:
            return set()
        return handler.pagelinks()


    @staticmethod
    def push_links_to_queue(links):
        for url in links:
            if (url in Crawler.queuedl) or (url in Crawler.crawledl):
                continue
            if Crawler.domain != domain_name(url):
                continue
            Crawler.queuedl.add(url)

 
    @staticmethod
    def update_files():
        settof(Crawler.queuedl,Crawler.queuef)
        settof(Crawler.crawledl,Crawler.crawledf)
        







