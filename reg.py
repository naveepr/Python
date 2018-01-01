import re
try:
    fh = open('regex_sum_318359.txt', 'r')
except:
    print "Please enter the filename properly"
else:
    sum=0
    for line in fh:
        y = re.findall('[0-9]+\s*',line)
        for item in y:
            sum=sum+float(item)
print '%d' %sum
