# coding=utf-8
""" makefilecodjs.py
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

def line_to_codeobj(line):
 sfx = "png"
 dir = "files1/"
 # parse the line
 pattern = r'^(kale_Page_)([0-9]+)([ ]*)(.*?)$'
 m = re.search(pattern,line)
 if m == None:
  return None
 reffile=m.group(1)
 pagenum= m.group(2)
 reffile = reffile + pagenum;
 code = m.group(3)  # 0 or more blanks
 word = m.group(4)  #  may be empty string
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
 # construct python object literal
 d = {
  'dir':dir,
  'sfx':sfx,
  # 'filename':filename,
  'word':word,
  'pagenum':pagenum,
  'disppage':disppage,
  # 'code':code
 }
 return d
 
        
def make_filecodearr(lines):
 # return a python array literal
 a = [] # returned array
 for iline,line in enumerate(lines):
  if (len(line) == 0):
   continue # skip blank line
  obj = line_to_codeobj(line)
  if obj == None:
   print('make_filecodearr error at line %s:\n%s' %(iline+1,line))
   exit(1)
  a.append(obj)
 return a

if __name__=="__main__":
 fileout = sys.argv[1] # "filecode.js"
 import filetop
 print('filetop array has length',len(filetop.filetop))
 # print(filetop.filetop) # ok, but not for humans!
 """
 from pprint import pprint
 pprint(filetop.filetop)
 f = codecs.open(fileout,"w","utf-8")
 pprint(filetop.filetop,stream=f)
 f.close()
 print('look at file',fileout)
 exit(1)
"""
 filetopvar = filetop.filetop
 filecodes = {}
 for x in filetopvar:
  code = x['code']
  filein = 'kale' + code
  filepath = '../files1/' + filein + '.txt'
  lines = read_lines(filepath)
  thisfilecode = make_filecodearr(lines)
  filecodes[code] = thisfilecode
 #
 import pprint
 filecode_pp = pprint.pformat(filecodes,indent=1,width=1000)  # pretty printed string representation of filecode
 with codecs.open(fileout,"w","utf-8") as f:
  f.write('filecode = \n')
  f.write(filecode_pp +';\n')  # semicolon is for Javascript

  
