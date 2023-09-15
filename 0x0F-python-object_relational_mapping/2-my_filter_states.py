#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''
import sys
import MySQLdb


def main():
    '''lists all states from the database hbtn_0e_0_usa'''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]
    connection = MySQLdb.connect(host="localhost", port=3306,
                                 user=username, password=password, db=database)
    cursor = connection.cursor()
    query = ("SELECT * FROM `states` WHERE `name` LIKE BINARY '{}'
             ORDER BY `id`".format(state_name_searched))
    cursor.execute(query)
    for row in cursor:
        print(row)
    cursor.close
    connection.close


if __name__ == "__main__":
    main()
