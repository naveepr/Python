#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def listSpecial(dirname):
    for dir in dirname:
        filenames = os.listdir(dir)
        for filename in filenames:
            match = re.search('.+__.+__.*',filename)
            if match:
                path=os.path.join(dir,filename)
                print os.path.abspath(path)

def copytoDir(dirname, todir):
    topath=os.path.abspath(todir)
    if not os.path.exists(topath):
        os.mkdir(topath)
    for dir in dirname:
        filenames = os.listdir(dir) 
        for filename in filenames:
            match = re.search('.+__.+__.*',filename)
            if match:
                path=os.path.join(dir,filename)
                path= os.path.abspath(path)
                shutil.copy(path,topath) 
         
def ziptoDir(dirname,tozip):
    exe=0
    if -1==tozip.find('.zip'):
        print "tozip file should be .zip extension"
        exit(1)
    cmd='zip -j '+tozip
    for dir in dirname:
        if not os.path.exists(dir):
            continue
        filenames = os.listdir(dir) 
        for filename in filenames:
            match = re.search('.+__.+__.*',filename)
            if match:
                path=os.path.join(dir,filename)
                path= os.path.abspath(path)
                cmd+=' '+path
                exe=1
    if exe:
        print cmd
        (status,output)=commands.getstatusoutput(cmd)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  if todir!='':
    copytoDir(args,todir)    
  elif tozip!='':
    ziptoDir(args,tozip) 
  else:
    listSpecial(args)

if __name__ == "__main__":
  main()
