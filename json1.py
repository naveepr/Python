import json
import urllib

try:
    url=raw_input("Enter the url: ")
    if len(url)<=0:
        raise 
except Exception:
    print "Enter proper url"
    exit(1)
else:
   print "Retreiving",url
   input = urllib.urlopen(url).read()
   print "Retrieved %d characters" %len(input)
   try:
    js=json.loads(str(input))
   except:
      exit(1) 

   #print json.dumps(js, indent=4)
   sum=0
   comments=js['comments']
   for item in comments:
       sum+=item["count"]

   print "Sum:",sum
