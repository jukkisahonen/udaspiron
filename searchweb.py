import urllib.request
from bs4 import BeautifulSoup


seedpage = 'http://trailwinds.info'
index = []
to_crawl = [seedpage]
crawled = []

def get_page(url):
    with urllib.request.urlopen(url) as response:
        return response.read()


def add_to_index(index, word, url):
    if word not in index:
        index.append([word,[url]])
        print (word)
    else:
        index[index.index[word]].append(url)
        print (url)


while to_crawl:
    url = to_crawl.pop()
    if url not in crawled:
        crawled.append(url)

        page = get_page(url)

        soup = BeautifulSoup(page)
        soup.prettify()

        words = soup.get_text()

        for word in words:
            add_to_index(index,word,url)

        for link in soup.find_all('a'):

            new_url = link.get('href')

            if new_url not in crawled:
                if new_url not in to_crawl:
                    to_crawl.append(new_url)
    if len(crawled) > 10:
        break

