import mysqlconnector
import uniprot
import pdb

'''
All the queries exist in this file
'''
cursor = mysqlconnector.conn.cursor()

# cursor.executemany("""INSERT INTO cancer VALUES (%s,%s,%s,%s,%s)""", uniprot.data)
cursor.executemany("""INSERT INTO pdb VALUES (%s,%s,%s,%s,%s,%s)""", pdb.pdb_data)
mysqlconnector.conn.commit()
