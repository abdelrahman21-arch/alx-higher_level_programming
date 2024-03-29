#!/usr/bin/python3
"""Module that lists all states from the hbtn_0e_0_usa database According to the supplied name in stdin"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connecting to Db
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    input = sys.argv[4]
    c.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (input,))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
