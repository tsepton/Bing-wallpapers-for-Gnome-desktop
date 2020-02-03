from html.parser import HTMLParser
from urllib.request import urlopen, urlretrieve
from subprocess import call
from pathlib import Path
from datetime import datetime
import os


BING_URL  = "https://www.bing.com/"
IMAGE_FOLDER = str(Path.home()) + '/Pictures/Bing/'
DATE = str(datetime.date(datetime.now()))

class BingParser(HTMLParser):
    url = BING_URL
    def __init__(self):
        self.image_path = ""
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == "div" and ("class", "img_cont") in attrs:
            data = [tuple for tuple in attrs if "style" in tuple]
            background_image = data[0][1]
            background_image = background_image.replace('background-image: url(', '')
            self.image_path = background_image
            #self.image_path = data[0][1]
    """ 
    def handle_starttag(self, tag, attrs):
        if tag == "div" and ("id", 'bgImgProgLoad') in attrs:
            data = [tuple for tuple in attrs if "data-ultra-definition-src" in tuple]
            self.image_path = data[0][1]
    """
    def get_url(self):
        return BingParser.url + self.image_path


def set_current_image(parser, html):
    parser.feed(html)
    image_url = parser.get_url()

    if not os.path.exists(IMAGE_FOLDER):
        os.mkdir(IMAGE_FOLDER)

    urlretrieve( image_url, IMAGE_FOLDER + DATE )
    call(["gsettings", "set", "org.gnome.desktop.screensaver", "picture-uri", IMAGE_FOLDER + DATE])
    call(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", IMAGE_FOLDER + DATE])



def main():
    parser   = BingParser()
    response = urlopen(BING_URL)
    html     = response.read().decode('utf8')
    response.close()

    set_current_image(parser, html)



main()
