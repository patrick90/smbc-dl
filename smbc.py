import re
import urllib
__author__ = 'l'
from bs4 import BeautifulSoup
import urllib2




def extract_all_archival_links():
    tmp=[]
    html_doc = urllib2.urlopen("http://www.smbc-comics.com/archives.php").read()
    html_doc=re.sub("<br>", "", html_doc)
    soup = BeautifulSoup(html_doc)
    a = soup.find_all("p")

    s = BeautifulSoup(str(a[1]))
    links=s.find_all("a")
    for i in links:
        tmp.append("http://www.smbc-comics.com"+i.get("href"))
    return tmp



def save_comic(adres):
    url=urllib2.urlopen(adres)
    page=url.read()
    url.close()
    soup=BeautifulSoup(page)
    comic=soup.find("div", id="comicimage").img.get("src")
    after_comic=soup.find("div", id="aftercomic").img.get("src")
    print(comic)
    file_name = comic.split('/')[-1]
    urllib.urlretrieve(comic, file_name)
    if after_comic!="":
        file_name = after_comic.split('/')[-1]
        urllib.urlretrieve(after_comic, file_name)

def test_all():
    al=extract_all_archival_links()
    i=0
    while(i<100):
        save_comic(al[i])
        i=i+1

def main():
    all=extract_all_archival_links()
    for i in all:
        save_comic(i)

if __name__ == "__main__":
    main()