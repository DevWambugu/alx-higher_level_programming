#!/usr/bin/python3
# DevWambugu
# lists all states from the database hbtn_0e_0_usa
# Your script should connect to a MySQL
# server running on localhost at port 3306
# Your script should take 3 arguments
# Results must be sorted in ascending order by states.id
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor:
        print(row)
    cursor.close
    connection.close


if __name__ == "__main__":
    main()
