'''
Uses BioPython's PDB module to parse and extract information from
PDB.
The goal of writing this script is to analysis a model of the protein. 
There are a lot of different models for any given proteins in PDB.
It is almost impossible to analyze all of them in a single go. So this 
generic script would help with analyzing any model that the user is interested
in, at the time of analyzes.
'''

from __future__ import print_function
from Bio import PDB
from Bio.PDB import *

#Using PDB to retrieve model from the list
repository = PDB.PDBList()
repository.retrieve_pdb_file('1TUP', pdir='.')

#Parse the file using mmcif, pdb parser is no longer supported by PDB
parser = MMCIFParser()
p53_1tup = parser.get_structure('P 53 - DNA Binding', '1tup.cif')
