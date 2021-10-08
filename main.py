from network import *

crawledFile = project_name + '/crawled.txt'
queueFile = project_name + '/queue.txt'
crawledSet = set()

# the master set of links in queue that will be written to file
linkSet = set()

# initializes the project folder and files if they do not already exist
make_project_dir(project_name)
make_project_files(project_name)

# checks for a sitemap, and if present, automatically adds the list of links to linkSet
try:
    linkSet.update(check_for_sitemap(base_url))
except TypeError:
    print('typerror')
    pass

# initializes the the linkSet from the file of queued links
file_to_set(queueFile, linkSet)
file_to_set(crawledFile, crawledSet)

def crawl():
    # a set for temporary use to avoid changes to linkSet while iterating
    tempSet = set()

    # gets the list of links from linkSet and goes one by one gathering the new links from pages in the list

    linkSet.update(linkSet.difference(crawledSet))
    x = len(linkSet)
    for url in linkSet:
        tempSet.update(find_links(url))
        crawledSet.add(url)
        print(str(len(linkSet)) + ': unique pages found')
        print(str(len(crawledSet)) + ': pages crawled')
        print(str(x) + ': pages in queue')
        print('-------------')
        x = x - 1


    # adds the new links minus those that have already been crawled
    linkSet.update(tempSet.difference(crawledSet))
    for link in linkSet:
        if link not in crawledSet:
            append_file(queueFile, link)
    for link in crawledSet:
        append_file(crawledFile, link)

    tempSet.clear()

while len(linkSet) != 0:
    crawl()








