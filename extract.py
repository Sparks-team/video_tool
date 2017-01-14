import feedparser
import urllib3
import re
from bs4 import BeautifulSoup
import boilerpipe
from boilerpipe.extract import Extractor
import os
import sys
from shutil import copyfile

reload(sys)
sys.setdefaultencoding('utf-8')
def func1():
    global count
    
item = 1
d = feedparser.parse('http://wittyfeed.com/sitemap/feed_rss')

def get_link():
    return d['entries'][item]['link']

def get_author():
    return d['entries'][item]['author']

def get_story_id():
    return d['entries'][item]['guid']

def get_cover_image():
    soup = get_source()
    print(soup)

def get_source():
    source = d['entries'][item]['content'][0]['value']
   # print(source)
    soup = BeautifulSoup(source, 'html.parser')
    return soup

def get_story_title():
    return d['entries'][item]['title']

def get_story_description():
    return d['entries'][item]['description']

def save_story_title():
    story_id = get_story_id()
    story_title = get_story_title()
    title_file = story_id + "_title"
    text_file = open(title_file, "wb")
    text_file.write(story_title)
    text_file.close()

def save_story_description():
    story_id = get_story_id()
    story_description = get_story_description()
    description_file = story_id + "_description"
    text_file = open(description_file, "wb")
    text_file.close()

def get_ext(url):
    filename, file_extension = os.path.splitext(url)
    return file_extension

def get_logo(id):
    # conn_pool = urllib3.PoolManager()
    # url = "http://wittysa.com/img/19.jpg"
    # resp = conn_pool.request('GET',url )
    # full_name = "logo.jpeg"
    src = "wittylogo.png"
    dst = id + "/wittylogo.png"
    copyfile(src, dst)
    # f = open(full_name, 'wb')
    # f.write(resp.data)
    # f.close()


def get_images(folder):
#story_title = soup.html.body.figure.img['src']
    soup = get_source()

    # s = soup.findAll('img')
    s = soup.findAll('img')
    count = len(s)
    connection_pool = urllib3.PoolManager()
    for x in range(0,len(s)):
        caption = s[x].parent.text

        print(caption)
        url = s[x]['src']
        print(url)
        ext = get_ext(url)
        full_caption = folder + "/figcaption/" + str(x) + ".txt"
        fullname = str(x) + ext
        full_name = folder + "/images/" + fullname
        resp = connection_pool.request('GET',url )
       # print(resp)
        t = open(full_caption, 'wb')
        t.write(caption)
        t.close()
        f = open(full_name, 'wb')
        f.write(resp.data)
        f.close()
    resp.release_conn()
    return count


def get_text(txt):
    extractor = Extractor(extractor='ArticleExtractor', url=get_link())
    #print extractor
    extracted_text = extractor.getText()
    #extracted_html = extractor.getHTML()
    #print(extracted_text)

def save_story_text():
    story_main_text = get_text()
    story_maintext_file = get_story_id() + "_maintext"
    text_file = open(story_maintext_file, "wb")
    text_file.close()

#get_cover_image()
# s = get_source()
# print(s)
func1()