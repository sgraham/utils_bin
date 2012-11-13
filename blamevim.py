import os
import re
import subprocess
import sys

command = sys.argv[1]
filename = sys.argv[2]
line = sys.argv[3]

filename = filename.replace('\\', '/')
mo = re.search(r'src/cr[0-9]?/(src/.*)', filename)
if command == 'annotate':
  base = 'http://src.chromium.org/viewvc/chrome/trunk/'
  url = base + mo.group(1) + '?annotate=HEAD'
  os.system('start ' + url)
elif command == 'codesearch':
  base = 'https://code.google.com/searchframe#OAMlx_jo-ck/'
  url = base + mo.group(1) + '^&exact_package=chromium^&l=' + line
  os.system('start ' + url)
elif command == 'codereview':
  p = subprocess.Popen('git cl status', stdout=subprocess.PIPE, shell=True)
  for line in p.communicate()[0].splitlines():
    mo = re.match('Issue number: \d+ \((.*)\)', line)
    if mo:
      os.system('start ' + mo.group(1))
      break
  else:
    raise Exception("couldn't get issue number")
else:
  raise Exception("unknown command")

"""

os.chdir(os.path.dirname(sys.argv[1]))

name = sys.argv[1].replace('\\', '/')
line = int(sys.argv[2])
p = subprocess.Popen("git rev-parse --show-toplevel", stdout=subprocess.PIPE,
                     shell=True)
toplevel = p.communicate()[0].strip()
if name.startswith(toplevel):
  name = name[len(toplevel) + 1:] # +1 for trailing / too.
  os.chdir(toplevel)
p = subprocess.Popen("git blame -L %d,%d %s" % (line-5, line+5, name),
                     stdout=subprocess.PIPE, shell=True)
blame_range = p.communicate()[0]
print blame_range

hashes = set()
for line in blame_range.splitlines():
  hash, sep, rest = line.partition(' ')
  if hash not in hashes:
    print '-'*79
    print '-'*79
    print '--', hash
    print '-'*79
    print '-'*79
    p = subprocess.Popen("git show %s" % hash, stdout=subprocess.PIPE,
                         shell=True)
    print p.communicate()[0]
    hashes.add(hash)

"""
