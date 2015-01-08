# A simple application of database of Python..
##  _Vincent He
##  @ Jan.5 2015
##

import sys, shelve

def store_person(db):

    pid = raw_input('Enter unique ID number: ')
    person = {}
    person['name'] = raw_input('Enter name: ')
    person['age'] = raw_input('Enter age: ')
    person['phone'] = raw_input('Enter phone number: ')
    
    db[pid] = person

def lookup_person(db):

    pid = raw_input('Enter ID number: ')
    field = raw_input('What would you like to know? (name/age/phone number)')
    field = field.strip().lower()
    print field.capitalize() + ':' + db[pid][field]
    
def print_help():
    print 'The available commands are:'
    print 'store  : Stores informat about a person'
    print 'lookup : Looks up a person from ID'
    print 'quit   : Save changes and exit'
    print '?      : Print this message'
    
def enter_command():
    cmd = raw_input('Enter command ( ? for help )')
    cmd = cmd.strip().lower()
    return cmd

def main():
    data_base = shelve.open('database.dat')  # address
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(data_base)
            elif cmd == 'lookup':
                lookup_person(data_base)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        data_base.close()
    
if __name__ == '__main__': main()

