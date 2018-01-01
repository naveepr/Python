import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = raw_input('Enter count:')
pos = raw_input('Enter position:')
count=int(count)
while (count>=0):
    print "Retrieving:",url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    position=int(pos)
    # Retrieve all of the anchor tags
    tags = soup('a')

    for tag in tags:
        x = tag.get('href',None)
        if position == 1:
            url=x
            break
        position=position-1
    count=count-1
