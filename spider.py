from urllib import urlopen
from link_finder import LinkFinder
from main import *

class spider:
# Class variable is same for all instances
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
# Set is used as faster, changes to set recorded on RAM, file changes on hard drives
    queue = set()
    crawled = set()

    def __init__(self, project_name, base_url, domain_name):
        spider.project_name = project_name
        spider.base_url = base_url
        spider.domain_name = domain_name
        spider.queue_file = spider.project_name + '/queue.txt'
        spider.crawled_file = spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider', spider.base_url)

    @staticmethod 
# Used when method doesnt need to be in class as it doesnt use instance variables, can be defined outside class too
    def boot():
        make_project_directory(spider.project_name)
        create_files(spider.project_name, spider.base_url)
        spider.queue = file_to_set(spider.queue_file) # No need to return, it adds to set
        spider.crawled = file_to_set(spider.crawled_file) # Same as above

    @staticmethod
# Thread name argument refers to which spider is crawling    
    def crawl_page(thread_name, page_url):
        if page_url not in spider.crawled:
            print thread_name + ' now crawling ' + page_url
            print 'Queue ' + str(len(spider.queue)) + ' | Crawled ' + str(len(spider.crawled))
            spider.add_links_to_queue(spider.gather_links(page_url))
            spider.crawled.add(page_url)
            spider.update_files()
    
    @staticmethod
    def gather_links(page_url):
        html_string = '' # We'll store the html data after conversion from byte format
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            finder = LinkFinder(spider.base_url, page_url)
            finder.feed(html_string)
        except:
            print 'Error: can not crawl page'
            return set()
        return finder.page_links

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in spider.queue:
                continue
            if url in spider.crawled:
                continue
            if spider.domain_name not in url:
                continue
            spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(spider.queue, spider.queue_file)
        set_to_file(spider.crawled, spider.crawled_file)
        