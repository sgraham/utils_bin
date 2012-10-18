# Handle file.cc(23) or file.cc:23: and open vim to right line.

import os
import re
import sys

def run(cmd):
  #print cmd
  os.system(cmd)

def open_at(file, line=1):
  if not os.path.exists(file):
    strip_out = ['@', '../../', '..\\..\\']
    for strip in strip_out:
      if file.startswith(strip):
        file = file[len(strip):]
        print "Using modified file path: %s" % file
  run('start gvim.exe --remote-silent +%s "%s"' % (line, file))

def main():
  for arg in sys.argv[1:]:
    mo = re.match('(.*)\((\d+)\)\s*', arg)
    mo2 = re.match('(.*):(\d+):?\s*', arg)
    if mo:
      file = mo.group(1)
      line = mo.group(2)
      open_at(file, line)
    elif mo2:
      file = mo2.group(1)
      line = mo2.group(2)
      open_at(file, line)
    else:
      open_at(arg)

if __name__ == '__main__':
  main()
