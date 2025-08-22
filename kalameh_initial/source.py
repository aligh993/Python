# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import re
from collections import Counter

def words_check(text):
    d = text.split()
    a = []
    for i in d:
        if (len(re.findall("\W|_+", i))) >= (len(re.findall("[a-zA-Z]", i))):
            pass
        else:
            pas = re.sub("\W|_+", "", i).capitalize()
            pas = a.append(pas)
    a = ' '.join(a) 
    return dict(Counter(a.split()))

print(words_check("""hEllO My FriEnDs!!!
thIS is A tEsT For your #p#r#o#b#l#e#m a"""))