import mysqlconnector
import uniprot

'''
All the queries exist in this file
'''
cursor = mysqlconnector.conn.cursor()

cursor.executemany("""INSERT INTO cancer VALUES (%s,%s,%s,%s,%s)""", uniprot.data)
mysqlconnector.conn.commit()
