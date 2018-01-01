fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print "enter the filename properly"
else:
    dic=dict()
    count = 0
    for line in fh:
        if line.startwith('From '):
            lst=line.split()
            str=lst[5]
            dic[str[:2]]=dic.get(str[:2],0)+1
lst1=([(v,k) for k,v in dic.items()])
lst.sort()
for v,k in lst:
    print k, v
