import threading # imports thread functionality
from Queue import Queue
from spider import spider
from domain import *
from main import *

PROJECT_NAME = '' # In caps used for main/unchanging variables
HOMEPAGE = ''
DOMAIN_NAME = GET_DOMAIN_NAME(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS =  # Number, based on OS used, hardware compatibility
queue = Queue()
spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

def crawl():
    queued = file_to_set(QUEUE_FILE)
    if len(queued) > 0:
        print len(queued) + ' links in queue'
        assign()
        
def assign():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    
    
def create_threads():
    for x in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target = work)
        thread.daemon = # True or False depending on whether I need it in background
        thread.start()
        
def work():
    while True:
        url = queue.get()
        Spider.crawled(threading.current_thread().name, url)
        queue.task_done()
        
# Call functions
create_threads()
crawl()