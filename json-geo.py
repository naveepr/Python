import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'
while True:
    try:
        address = raw_input('Enter location: ')
        if len(address) < 1: 
            raise "Invalid url"
    except e:
        print e.args 
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except:
        js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    break

print "place_id:",js["results"][0]["place_id"]
