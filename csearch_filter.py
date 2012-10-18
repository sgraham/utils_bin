# Filter for csearch. Line numbers are 0 based, which is bad for editors.
# Should really fix csearch, but oh well.
# Also drop some random crap.
import sys
import re

def main():
  for line in sys.stdin:
    if '.svn-base' in line:
      continue
    if '.svn\\' in line:
      continue
    if 'changelog' in line.lower():
      continue
    if '.js:' in line:
      continue
    if '.html:' in line:
      continue
    sys.stdout.write(
        re.sub(r':([0-9]+):', lambda x: ':%d:' % (int(x.group(1)) + 1), line))

if __name__ == '__main__':
  main()
