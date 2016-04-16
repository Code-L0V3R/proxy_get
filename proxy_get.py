# L0VER IN MYANMAR
# 17,4,2016
import base64
import urllib2
import re
print '\n'.join([str(base64.b64decode(i)) for i in re.findall("Proxy\((.+)\)</script>" , urllib2.urlopen('http://proxy-list.org/english/search.php?search=ssl-no&country=any&type=any&port=any&ssl=no').read())])

