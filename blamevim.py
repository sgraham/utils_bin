import os
import subprocess
import sys

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
