# Handle file.cc(23) and open vim to right line.

import os
import re
import sys

def run(cmd):
  #print cmd
  os.system(cmd)

def main():
  for arg in sys.argv[1:]:
    mo = re.match('(.*)\((\d+)\)\s*', arg)
    if mo:
      file = mo.group(1)
      line = mo.group(2)
      run('start gvim.exe --remote-send %sgg --remote-silent "%s"' % (line, file))
    else:
      run('start gvim.exe --remote-silent "%s"' % arg)

if __name__ == '__main__':
  main()
