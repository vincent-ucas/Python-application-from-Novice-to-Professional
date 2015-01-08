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

# list all the email address of the head of email.
def list_address():
    addresses = set()
    pat = re.compile(r'[a-z\-\.]+@[a-z\-\.]', re.IGNORECASE)
    for line in fileinput.input('email.txt'):
        for address in pat.findall(line):
            addresses.add(address)
    for address in sorted(addresses):
        print address

if __name__ == '__main__' : list_address()