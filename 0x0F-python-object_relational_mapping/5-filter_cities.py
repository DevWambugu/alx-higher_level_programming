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
    query = ("""SELECT cities.id, cities.name, states.name
             From cities
	     INNER JOIN states ON cities.state_id = states.id
             WHERE states.name = %s 	
	     ORDER BY cities.id ASC""")
    state_name_searched_bytes = state_name_searched.encode("utf-8")
    cursor.execute(query, (state_name_searched_bytes,))
    for row in cursor:
        print(row[1], end=' ')
    print()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
