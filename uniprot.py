#!/usr/bin/python3


from collections import defaultdict
import requests
from Bio import ExPASy, SwissProt
import pandas as pd
import StringIO

server = 'http://www.uniprot.org/uniprot'

def do_request(server, ID='', **kwargs):

    params = ''
    req = requests.get('%s/%s%s' % (server, ID, params), params=kwargs)
    if not req.ok:
        req.raise_for_status()
    return req

req = do_request(server, query='gene:p53 AND reviewed:yes',# AND organism:Human',
                 format='tab',
                 columns='id,entry name,length,organism,organism-id,database(PDB),database(HGNC)',
                 limit='50')

uniprot_list = pd.read_table(StringIO.StringIO(req.text))
uniprot_list.rename(columns={'Organism ID': 'ID'}, inplace=True)
print(uniprot_list)
