# coding=utf-8
""" change_1.py
"""
from __future__ import print_function
import sys, re,codecs
# import json

def read_lines(filein):
 # Notice the indentation
 # there's a lot packed into the next line.
 # We could say:
 #  open file named filein for reading. The file is encoded as utf-8.
 #  Use the variable 'f' for reading from the file. 'f' could be
 #  called the 'file handle'.
 with codecs.open(filein,"r","utf-8") as f:
  # Notice the further indentation
  # Read every line in the file, and strip from the end of each
  # line the line-ending characters '\r\n'
  # And, add each stripped line into the Python list named 'lines'
  lines = [line.rstrip('\r\n') for line in f]
 # Notice we have gone back to 1 character of indentation (same as 'with')
 # print to the 'console' a message indicating how many lines were read
 print(len(lines),"lines read from",filein)
 # the function returns the list of lines
 return lines

def write_lines(fileout,lines):
 # Note we call this function as 'write_lines(fileout,newlines)'.
 # In this function, the function parameter 'lines' will, when
 # called, have the value newlines.
 # open the file, but this time for 'writing'
 with codecs.open(fileout,"w","utf-8") as f:
  # write each line using a for loop
  for line in lines:
   # we will add the 'newline' line break character at the end of the line
   
   f.write(line+'\n')
 print(len(lines),"lines written to",fileout)
 # This function doesn't explicitly return anything.

def line_to_json(line): # not used!
 sfx = "png"
 dir = "files1/"
 # parse the line
 pattern = r'^(kale_Page_)([0-9]+)[ ]+([^ ]+)[ ]+(.*?)$'
 m = re.search(pattern,line)
 if m == None:
  return None
 reffile=m.group(1)
 pagenum= m.group(2)
 reffile = reffile + pagenum;
 code = m.group(3)
 word = m.group(4)
 ipagenum = int(pagenum)
 # logic to compute disppage. This is specific to Kale
 if ((ipagenum > 14) and (ipagenum <= 550)):
  disppage = ipagenum - 14
 elif ((ipagenum > 550) and (ipagenum <= 706)):
  disppage = ipagenum - 550
 elif (ipagenum > 709) :
  disppage = ipagenum - 709
 #
 filename="kale%s.txt" % code 
 # construct python object literal
 d = {
  'dir':dir,
  'sfx':sfx,
  'filename':filename,
  'word':word,
  'pagenum':pagenum,
  'disppage':disppage,
  'code':code
 }
 # convert to json
 json = json.dumps(d,indent = 1)
 return json

def line_to_js(line):
 sfx = "png"
 dir = "files1/"
 # parse the line
 pattern = r'^(kale_Page_)([0-9]+)[ ]+([^ ]+)[ ]+(.*?)$'
 m = re.search(pattern,line)
 if m == None:
  return None
 reffile=m.group(1)
 pagenum= m.group(2)
 reffile = reffile + pagenum;
 code = m.group(3)
 word = m.group(4)
 if False:
  print('dbg: "%s"' % line)
  print(" reffile = %s. pagenum = %s, code= %s" %(reffile,pagenum, code))
 ipagenum = int(pagenum)
 # logic to compute disppage. This is specific to Kale
 if ((ipagenum > 14) and (ipagenum <= 550)):
  disppage = ipagenum - 14
 elif ((ipagenum > 550) and (ipagenum <= 706)):
  disppage = ipagenum - 550
 elif (ipagenum > 709) :
  disppage = ipagenum - 709
 else:
  disppage = ''
 filename="kale%s.txt" % code 
 # construct python object literal
 d = {
  'dir':dir,
  'sfx':sfx,
  'filename':filename,
  'word':word,
  'pagenum':pagenum,
  'disppage':disppage,
  'code':code
 }
 # convert to array of strings representing Javascript literal
 outarr = []
 outarr.append('{') # start js object literal
 names = ['dir','sfx','filename','word','pagenum','disppage','code']
 for name in names:
  out = "'%s':'%s'," %(name,d[name])
  outarr.append(out)
 outarr.append('}, ') # close js literal
 return outarr
    
def make_filetop(lines):
 outlines = []
 # filetop will be an array of objects 
 outlines.append('filetop = [') # start array 
 for iline,line in enumerate(lines):
  jsobjlines = line_to_js(line)
  if jsobjlines == None:
   print('make_filetop error at line %s:\n%s' %(iline+1,line))
   exit(1)
  #  jsobjlinees to one line
  out = '  '.join(jsobjlines)
  outlines.append(out)
 # close the array
 outlines.append('];') # end of filetop
 return outlines

if __name__=="__main__":
 filein = sys.argv[1] # "../files1/kaletop.txt"
 fileout = sys.argv[2] # "filetop.js"  # Javascript variable 'filetop'.
 lines = read_lines(filein)  # array of strings
 linesout = make_filetop(lines) # array of lines - contents of fileout
 write_lines(fileout,linesout)
