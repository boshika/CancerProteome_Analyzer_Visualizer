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


####################### P53 1UTP MODEL ANALYSIS #######################

#Using PDB to retrieve model from the list
# repository = PDB.PDBList()
# repository.retrieve_pdb_file('1TUP', pdir='.')

#Parse the file using mmcif, pdb parser is no longer supported by PDB
parser = MMCIFParser()
p53_1tup = parser.get_structure('P 53 - DNA Binding', './protein_models/1tup.cif')

#TOP DOWN ANALYSIS
def describe_model(name, pdb):
    print()
    this_list = []
    for model in pdb:
        for chain in model:
            this_list.append('%s - Chain: %s. Number of residues: %d. Number of atoms: %d.' % \
                   (name, chain.id, len(chain), len(list(chain.get_atoms()))))
    return this_list

#chains in itup
p53_itup_model = describe_model('1TUP', p53_1tup)
print(p53_itup_model)

#all residues except water
residues = []
for residue in p53_1tup.get_residues():
    if residue.id[0] in [' ', 'H_HOH']:
        continue
    residues.append(residue.id)
print(residues)

#atom-related statistics




# should be done using a better way, extracting data from uniprot API and hardcoding it defeats the purpose
# pass this to proteomics datatbase table models
# data = [(1, p53_itup_model)]
