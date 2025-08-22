# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

from bs4 import BeautifulSoup
import codecs


def process(open):
    count = 0
    f = codecs.open(open, 'r', 'utf-8')
    soup = BeautifulSoup(f, 'html.parser')
    for _ in soup.findAll('a'):
        count += 1
    print(count)
    return count
