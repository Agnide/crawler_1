from HTMLParser import HTMLParser
from urlparse import urljoin

# Imp. - I'll have to change the class below to composition after finding out HTMLParser file

class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()
        super(LinkFinder, self).__init__()
# The __init__() in the line above is the init in HTMLParser

# To find html header tags in page code
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

# urljoin automaticaly checks and gives full url, even if value is full url and not relative url

    def error(self, message):
        pass
        
