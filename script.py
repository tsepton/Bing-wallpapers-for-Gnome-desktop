from html.parser import HTMLParser
from urllib.request import urlopen, urlretrieve
from subprocess import call
import os

bingUrl  = "https://www.bing.com/"
cwd = os.getcwd()

class BingParser(HTMLParser):
    url = "bing.com/"
    def __init__(self):
        self.image_path = ""
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == "div" and ("id", 'bgImgProgLoad') in attrs:
            data = [tuple for tuple in attrs if "data-ultra-definition-src" in tuple]
            self.image_path = data[0][1]

    def get_url(self):
        return "https://www.bing.com" + self.image_path


def main():
    parser   = BingParser()
    response = urlopen(bingUrl)
    html     = response.read().decode('utf8')

    response.close()
    parser.feed(html)
    image_url = parser.get_url()
    urlretrieve(image_url, cwd + '/bing_image')

    image_path = "'" + cwd + "/bing_image'"
    call(["gsettings", "set", "org.gnome.desktop.screensaver", "picture-uri", image_path])
    #call(['rm', cwd+'/bing_image'])

main()
