#   PySQLite for SQL database..
#   $author:   Ming
#   $date:     Jan.12 2015

import sqlite3

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = 0
    return float(value)

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''
    CREATE TABLE food(
    id      TEXT       PRIMARY KEY,
    desc    TEXT,
    water   FLOAT,
    kcal    FLOAT,
    protein FLOAT,
    fat     FLOAT,
    ash     FLOAT,
    carbs   FLOAT,
    fiber   FLOAT,
    sugar   FLOAT
)
''')

query = 'INSERT INTO food VALUES (?,?,?,?,?,?,?,?,?,?)'

for line in open('ABBREV.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[: fields.count]]
    curs.execute(query, vals)

conn.commit()
conn.close()