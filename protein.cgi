#!/usr/bin/python
print("Content-Type: text/html\n\n")
import cgi
import cgitb
cgitb.enable()
import re
import json
import mysqlconnector



#get form values
form = cgi.FieldStorage()

#Get data from the fields
gene = form.getvalue('search_term')

cursor = mysqlconnector.conn.cursor()

cursor.execute("SELECT cancer.entryname, cancer.length, cancer.description, cancer.GO, pdb.model, pdb.chains,pdb.residues, pdb.atoms FROM cancer, pdb WHERE cancer.id = pdb.protein_id AND entryname LIKe %s", (gene, ))

results = { 'match_count': 0, 'matches': list() }
for (product, length, description, GO, model, chains, residues,atoms) in cursor:
    results['matches'].append({'product': product, 'length': length, 'description': description, 'GO': GO, 'model': model, 'chains': chains, 'residues': residues, 'atoms': atoms})
    results['match_count'] += 1



mysqlconnector.conn.close()

print(json.dumps(results))
