# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import re
string = 'my face friend is facfriend and advertisement'
whitelist = re.compile('face|friend|advertisement|is')
timeline = [word for word in string.split(' ') if whitelist.search(word)]
# filter version of this command:
# timeline = filter(lambda word: not blacklist.search(word), string.split())
print(timeline)