# Filter for csearch. Line numbers are 0 based, which is bad for editors.
# Should really fix csearch, but oh well.
import sys
import re
for line in sys.stdin:
  sys.stdout.write(
      re.sub(r':([0-9]+):', lambda x: ':%d:' % (int(x.group(1)) + 1), line))
