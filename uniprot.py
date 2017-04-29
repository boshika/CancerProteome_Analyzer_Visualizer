#!/usr/bin/python3


from collections import defaultdict
import requests
from Bio import ExPASy, SwissProt
import pandas as pd
import StringIO
import mysqlconnector


server = 'http://www.uniprot.org/uniprot'

def do_request(server, ID='', **kwargs):
    # type: (object, object, object) -> object

    params = ''
    req = requests.get('%s/%s%s' % (server, ID, params), params=kwargs)
    if not req.ok:
        req.raise_for_status()
    return req

#p53
req = do_request(server, query='gene:p53 AND reviewed:yes AND organism:Human',
                 format='tab',
                 columns='entry name,length,organism,organism-id,database(PDB),database(HGNC)'
                 )

uniprot_list = pd.read_table(StringIO.StringIO(req.text))
uniprot_list.rename(columns={'Organism ID': 'ID'}, inplace=True)
uniprot_list.set_index('ID', inplace=True)
print(uniprot_list.iloc[:,[0]])
print(uniprot_list.iloc[:,[1]])
print(uniprot_list.iloc[:,[3]])



#myc
req = do_request(server, query='gene:myc AND reviewed:yes AND organism:Human',
                 format='tab',
                 columns='entry name,length,organism,organism-id,database(PDB),database(HGNC)'
                 )

uniprot_list1 = pd.read_table(StringIO.StringIO(req.text))
uniprot_list1.rename(columns={'Organism ID': 'ID'}, inplace=True)
uniprot_list1.set_index('ID', inplace=True)
print(uniprot_list1.iloc[:,[0]])
print(uniprot_list1.iloc[:,[1]])
print(uniprot_list1.iloc[:,[3]])


#errb2
req = do_request(server, query='gene:her2 AND reviewed:yes AND organism:Human',
                 format='tab',
                 columns='entry name,length,organism,organism-id,database(PDB),database(HGNC)'
                 )

uniprot_list2 = pd.read_table(StringIO.StringIO(req.text))
uniprot_list2.rename(columns={'Organism ID': 'ID'}, inplace=True)
uniprot_list2.set_index('ID', inplace=True)
print(uniprot_list2.iloc[:,[0]])
print(uniprot_list2.iloc[:,[1]])
print(uniprot_list2.iloc[:,[3]])


#Epidermal Growth Factor
req = do_request(server, query='gene:egfr AND reviewed:yes AND organism:Human',
                 format='tab',
                 columns='entry name,length,organism,organism-id,database(PDB),database(HGNC)'
                 )

uniprot_list3 = pd.read_table(StringIO.StringIO(req.text))
uniprot_list3.rename(columns={'Organism ID': 'ID'}, inplace=True)
uniprot_list3.set_index('ID', inplace=True)
print(uniprot_list3.iloc[:,[0]])
print(uniprot_list3.iloc[:,[1]])
print(uniprot_list3.iloc[:,[3]])


#Pten
req = do_request(server, query='gene:pten AND reviewed:yes AND organism:Human',
                 format='tab',
                 columns='entry name,length,organism,organism-id,database(PDB),database(HGNC)'
                 )

uniprot_list4 = pd.read_table(StringIO.StringIO(req.text))
uniprot_list4.rename(columns={'Organism ID': 'ID'}, inplace=True)
uniprot_list4.set_index('ID', inplace=True)
print(uniprot_list4.iloc[:,[0]])
print(uniprot_list4.iloc[:,[1]])
print(uniprot_list4.iloc[:,[3]])


cursor = mysqlconnector.conn.cursor()

#should be done using a better way, extracting data from uniprot API and hardcoding it defeats the purpose
data = [(1,'P53',393),(2,'MYC',439), (3, 'ERRB2', 1255),(4, 'EGFR', 490), (5, 'PTEN', 403)]
cursor.executemany("""INSERT INTO cancer VALUES (%s,%s,%s)""",data)
mysqlconnector.conn.commit()
