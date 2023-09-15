#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''
import sys
import MySQLdb


def main():
    '''lists all states from the database hbtn_0e_0_usa'''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=username, password=password, db=database)
    cursor = connection.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities
                   INNER JOIN states ON cities.state_id=states.id
                   ORDER BY cities.id ASC""")
    for row in cursor:
        print(row)
    cursor.close
    connection.close


if __name__ == "__main__":
    main()
