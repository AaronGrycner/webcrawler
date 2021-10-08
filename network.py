import requests
from bs4 import BeautifulSoup
from general import *
from usp.tree import sitemap_tree_for_homepage
import time
from PIL import Image

# finds all links on requested page
def find_links(url):

    # this code requests the page, and parses the HTML using Beautiful Soup
    r = ''

    while r == '':
        try:
            r = requests.get(url)
            break
        except requests.exceptions.ConnectionError:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue

    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    links = []

    for link in soup.find_all('a'):
        link = link.get('href')
        checkedLink = check_link(link)
        if checkedLink == None:
            pass
        else:
            links.append(checkedLink)
    return links

# Checks links for domain and repairs links that are truncated or incomplete. Also deletes duplicate links.
def check_link(link):
    a = urlparse(link, allow_fragments=False)

    if link == None:
        return

    # the link points to an outside site
    if project_name not in a.netloc and a.netloc != '':
        return

    # checks for javascript references that get passed from href attributes
    if link == 'javascript:;':
        return

    # if there is no netloc, it is truncated and the link is repaired
    if a.netloc == "":
        link = base_url + link
        a = urlparse(link, allow_fragments=False)

    if 'www.' in a.netloc:
        link = link.replace('www.', '')
        a = urlparse(link, allow_fragments=False)

    # this checks that the link contains https: at the beginning and adds it if not present
    if a.scheme == '':
        link = 'https:' + link
        a = urlparse(link, allow_fragments=False)

    return link

# this function looks for a sitemap and if found, returns the list of pages as a set
def check_for_sitemap(url):
    links = set()
    tree = sitemap_tree_for_homepage(url)

    if 'sub_sitemaps=[]' in str(tree):
        print('no sitemap found, crawling manually')
        return
    else:
        print('sitemap found, adding links')
        for link in tree.all_pages():
            links.add(link._SitemapPage__url)
        return links