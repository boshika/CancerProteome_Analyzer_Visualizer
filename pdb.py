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
from pymol import cmd
pymol.finish_launching()





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

# #all residues except water
# residues = []
# for residue in p53_1tup.get_residues():
#     if residue.id[0] in [' ', 'H_HOH']:
#         continue
#     residues.append(residue.id)
# print(residues)
#
# cmd.fetch(' 1TUP', async = False)
# cmd.disable(' all')
# cmd.enable(' 1TUP')
# cmd.hide(' all')
# cmd.show(' sphere', 'name zn')
# cmd.scene(' S2', action =' store', view = 0, frame = 0, animate =-1)
# cmd.set(' ray_trace_frames', 0)
# cmd.mset( 1, 500)
# cmd.frame(0)
# cmd.scene('S0')
# cmd.mview()
# cmd.frame(60)
# cmd.set_view((-0.175534308, -0.331560850, -0.926960170, 0.541812420, 0.753615797,
#               -0.372158051, 0.821965039, -0.567564785, 0.047358301, 0.000000000,
#               0.000000000, -249.619018555, 58.625568390, 15.602619171, 77.781631470,
#               196.801528931, 302.436492920, -20.000000000))
# cmd.mview()
# cmd.frame(90)
# cmd.set_view((-0.175534308, -0.331560850, -0.926960170, 0.541812420, 0.753615797,
#               -0.372158051, 0.821965039, -0.567564785, 0.047358301, -0.000067875,
#               0.000017881, -249.615447998, 54.029174805, 26.956727982, 77.124832153,
#               196.801528931, 302.436492920, -20.000000000))
# cmd.mview()
# cmd.frame( 150)
# cmd.set_view((-0.175534308, -0.331560850, -0.926960170, 0.541812420, 0.753615797, -0.372158051,
#               0.821965039, -0.567564785, 0.047358301, -0.000067875, 0.000017881, -55.406421661,
#               54.029174805, 26.956727982, 77.124832153, 2.592475891, 108.227416992, -20.000000000))
# cmd.mview()
#
#

















            # should be done using a better way, extracting data from uniprot API and hardcoding it defeats the purpose
# pass this to proteomics datatbase table models
# data = [(1, p53_itup_model)]
