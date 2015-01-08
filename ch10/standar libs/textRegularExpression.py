##########
#   $author  Vincent
#   $date:   2015-1-8
#   $app:    text regular expression

import fileinput, re

#  find email sender
def find_sender():
    pat = re.compile('From: (.*) <.*?>$')
    for line in fileinput.input('email.txt'):
        m = pat.match(line)
        if m: print m.group(1)

if __name__ == '__main__' : find_sender()