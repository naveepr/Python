import urllib
import xml.etree.ElementTree as ET

try:
    address = raw_input('Enter location: ')
    assert(len(address) <1), 'url invlaid'
except Exception as inst:
    print "Exception raised", inst
    exit(0)

url = address
count=0
sum=0

print 'Retrieving ', url
uh = urllib.urlopen(url)
data = uh.read()
print "Retrieved %d characters"%len(data)
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
for item in lst:
    sum=sum+int(item.find('count').text)
print "Count:",len(lst)
print "Sum:",sum
