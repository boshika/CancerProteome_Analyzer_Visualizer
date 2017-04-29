import MySQLdb

conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="Proteomics" )
cursor = conn.cursor()

cursor.execute("SELECT VERSION()")



