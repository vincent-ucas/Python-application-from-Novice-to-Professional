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
    
    dp[pid] = person

def lookup_person(db)

    pid = raw_input('Enter ID number: ')
    field = raw_input('What would you like to know? (name/age/phone number)')
    field = field.strip().lower()
    print field.capitalize() + ':', \dp[pid][field]
    
finally:
    database.close()
    
if __name___=='__main__':main()
