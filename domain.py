from urlparse import urlparse

def get_sub_domain_name(url):
# Try statements are needed in network type python applications
    try:
        return urlparse(url).netloc
    except:
        return ''

def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
# This returns the second to last and element before that. Relative url is last element
    except:
        return ''

