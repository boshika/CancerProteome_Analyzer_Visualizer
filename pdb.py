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
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

repository = PDB.PDBList()

#Parse the file using mmcif, pdb parser is no longer supported by PDB
parser = MMCIFParser()

#######################   METHODS ######################

#Number of Residues and atoms on Each Chain
def describe_model(name, pdb):
    print()
    this_list = []
    for model in pdb:
        for chain in model:
            this_list.append('%s - Chain: %s. Number of residues: %d. Number of atoms: %d.' % \
                   (name, chain.id, len(chain), len(list(chain.get_atoms()))))
    return this_list

#for generating 3d Plot
def plot(model):
    fig = plt.figure(figsize=(16, 9))
    fig.suptitle(model, fontsize=20)
    ax3d = fig.add_subplot(111, projection='3d')
    ax_xy = fig.add_subplot(331)
    ax_xy.set_title('X/Y')
    ax_xz = fig.add_subplot(334)
    ax_xz.set_title('X/Z')
    ax_zy = fig.add_subplot(337)
    ax_zy.set_title('Z/Y')
    color = {'A': 'r', 'B': 'g', 'C': 'b', 'D': '0.25', 'E': '0.5', 'F': '0.75', 'G': '1', 'H': '1', 'J': '1'}
    zx, zy, zz = [], [], []
    for chain in model.get_chains():
        xs, ys, zs = [], [], []
        for residue in chain.get_residues():
            ref_atom = next(residue.get_iterator())
            x, y, z = ref_atom.coord
            if ref_atom.element == 'HOH':
                zx.append(x)
                zy.append(y)
                zz.append(z)
                continue
            xs.append(x)
            ys.append(y)
            zs.append(z)
        ax3d.scatter(xs, ys, zs, color=color[chain.id])
        print(color[chain.id])
        ax_xy.scatter(xs, ys, marker='.', color=color[chain.id])

        ax_xz.scatter(xs, zs, marker='.', color=color[chain.id])
        ax_zy.scatter(zs, ys, marker='.', color=color[chain.id])
    ax3d.set_xlabel('X')
    ax3d.set_ylabel('Y')
    ax3d.set_zlabel('Z')
    ax3d.scatter(zx, zy, zz, color='k', marker='v', s=300)
    ax_xy.scatter(zx, zy, color='k', marker='v', s=80)
    ax_xz.scatter(zx, zz, color='k', marker='v', s=80)
    ax_zy.scatter(zz, zy, color='k', marker='v', s=80)
    for ax in [ax_xy, ax_xz, ax_zy]:
        ax.get_yaxis().set_visible(False)
        ax.get_xaxis().set_visible(False)

    fig.savefig('./matplotlib_analysis/pten_1d5r.jpg')
    # fig = plt.show()

####################### P53 1UTP MODEL ANALYSIS #######################

#Using PDB to retrieve model from the list
# repository.retrieve_pdb_file('1TUP', pdir='.')

p53_1tup = parser.get_structure('P 53 - DNA Binding', './protein_models/1tup.cif')

#TOP DOWN ANALYSIS

#chains in itup
p53_itup_model = describe_model('1TUP', p53_1tup)
# print(p53_itup_model)

# #all nonstandard residues except water
residues = []
for residue in p53_1tup.get_residues():
    if residue.id[0] in [' ', 'H_HOH']:
        continue
    residues.append(residue.id)
print(residues)

#Pick a chain and look at its atoms
res = next(p53_1tup[0]['A'].get_residues())
print(res)

# plot(p53_1tup)

####################### MYC 1NKP MODEL ANALYSIS #######################
# repository.retrieve_pdb_file('1NKP', pdir='.')
myc_1nkp = parser.get_structure('MYC - DNA Binding', './protein_models/1nkp.cif')

#chains in 1nkp
myc_1nkp_model = describe_model('1NKP', myc_1nkp)
# print(myc_1nkp_model)

#all nonstandard residues except water
count = 0
for residue in myc_1nkp.get_residues():
    if residue.id[0] in [' ', 'H_HOH']:
        count +=1
print("Most of the residues are HOH: {}".format(count))

#Pick a chain and look at its atoms
res1 = next(myc_1nkp[0]['F'].get_residues())
print(res1)

# plot(myc_1nkp)


####################### ERRB2 1N8Z MODEL ANALYSIS #######################
# repository.retrieve_pdb_file('1N8Z', pdir='.')
errb_1n8z = parser.get_structure('ERRB2-Complexed with Herceptin', './protein_models/1n8z.cif')

#chains in 1n8z
errb_1n8z_model = describe_model('1N8Z', errb_1n8z)
# print(errb_1n8z_model)

#all nonstandard residues except water
residues1 = []
for residue in errb_1n8z.get_residues():
    if residue.id[0] in [' ', 'H_HOH']:
        continue
    residues1.append(residue.id)
print(residues1)

#Pick a chain and look at its atoms
res2 = next(errb_1n8z[0]['A'].get_residues())
print(res2)

# plot(errb_1n8z)

####################### EGFR 1JL9 MODEL ANALYSIS #######################
# repository.retrieve_pdb_file('1JL9', pdir='.')
egfr_1jl9 = parser.get_structure('ERRB2-Complexed with Herceptin', './protein_models/1jl9.cif')

#chains in 1Jl9
egfr_1jl9_model = describe_model('1JL9', egfr_1jl9)
# print(egfr_1jl9_model)

#all nonstandard residues except water
count1 =0
if residue.id[0] in [' ', 'H_HOH']:
        count1 +=1
print("Most of the residues are HOH: {}".format(count1))

#Pick a chain and look at its atoms
res3 = next(egfr_1jl9[0]['A'].get_residues())
print(res3)

# plot(egfr_1jl9)
####################### PTEN 1D5R MODEL ANALYSIS #######################
# repository.retrieve_pdb_file('1D5R', pdir='.')
pten_1d5r = parser.get_structure('PTEN TUMOR SUPPRESSOR', './protein_models/1d5r.cif')

#chains in 1Jl9
pten_1d5r_model = describe_model('1D5R', pten_1d5r)
# print(pten_1d5r_model)

#all nonstandard residues except water
residues2 = []
for residue in pten_1d5r.get_residues():
    if residue.id[0] in [' ', 'H_HOH']:
        continue
    residues2.append(residue.id)
print(residues2)

#Pick a chain and look at its atoms
res4 = next(pten_1d5r[0]['A'].get_residues())
print(res4)

# plot(pten_1d5r)


# should be done using a better way, extracting data from uniprot API and hardcoding it defeats the purpose
# pass this to proteomics datatbase table models
pdb_data = [(1, 'P53 1UTP Model', 'Chain: E. Number of residues: 43. Number of atoms: 442, \
                                   Chain: F. Number of residues: 35. Number of atoms: 449, \
                                   Chain: A. Number of residues: 395. Number of atoms: 1734, \
                                   Chain: B. Number of residues: 265. Number of atoms: 1593, \
                                   Chain: C. Number of residues: 276. Number of atoms: 1610',
                                   'H_ZN=951 H_ZN=952H_ZN=953', 'Residue SER het=  resseq=94 icode=', 1),
            (2, 'MYC 1NKP Model', 'Chain: F. Number of residues: 81. Number of atoms: 447,  \
                                   Chain: G. Number of residues: 86. Number of atoms: 452, \
                                   Chain: H. Number of residues: 79. Number of atoms: 445, \
                                   Chain: J. Number of residues: 84. Number of atoms: 450, \
                                   Chain: A. Number of residues: 179. Number of atoms: 824, \
                                   Chain: B. Number of residues: 158. Number of atoms: 761, \
                                   Chain: D. Number of residues: 165. Number of atoms: 787, \
                                   Chain: E. Number of residues: 160. Number of atoms: 740',
                                   'Most of the residues are HOH: 992', 'Residue DC het=  resseq=101 icode=', 2),
            (3, 'ERRB2 1N8Z MODEL', 'Chain: A. Number of residues: 233. Number of atoms: 1664, \
                                     Chain: B. Number of residues: 233. Number of atoms: 1655, \
                                    Chain: C. Number of residues: 631. Number of atoms: 4571',
                                    'H_NAG=766, H_NAG=738, H_SO4=1001', 'Residue ASP het=  resseq=1 icode=', 3),
            (4, 'EGFR 1JL9 MODEL', 'Chain: A. Number of residues: 47. Number of atoms: 335, \
                                    Chain: B. Number of residues: 47. Number of atoms: 369',
                                    'Most of the residues are HOH: 1', 'Residue CYS he resseq=6 icode', 4),
            (5, 'PTEN 1D5R MODEL', 'Chain: A. Number of residues: 690. Number of atoms: 2968',
                                    'H_TLA=352', 'Residue ARG het  resseq=14 icode', 5)
        ]
